import socket
import threading

print("<DigitalTrailBlazer>")
def get_local_network_segment():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        subnet_mask = None
        interfaces = socket.if_nameindex()
        for interface_name, interface_index in interfaces:
            if interface_name.startswith('Ethernet') or interface_name.startswith('Wi-Fi'):
                interface_info = socket.if_addresses(interface_index)
                for info in interface_info:
                    if info[0] == socket.AF_INET:
                        subnet_mask = info[2][0]
                        break
                if subnet_mask:
                    break
        if subnet_mask is None:
            return None
        ip_parts = [int(x) for x in ip.split('.')]
        mask_parts = [int(x) for x in subnet_mask.split('.')]
        network_parts = [ip_parts[i] & mask_parts[i] for i in range(4)]
        return '.'.join(map(str, network_parts)) + '/24'
    except Exception as e:
        return None

def scan_local_network(network_segment):
    found_devices = []
    def scan_ip(ip):
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            found_devices.append((ip, hostname))
        except socket.herror:
            pass
    threads = []
    for i in range(1, 255):
        ip = f"{network_segment[:-3]}{i}"
        t = threading.Thread(target=scan_ip, args=(ip,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return found_devices

if __name__ == "__main__":
    segment = get_local_network_segment()
    if segment:
        print(f"本地局域网网段为：{segment}")
        devices = scan_local_network(segment)
        for ip, name in devices:
            print(f"IP: {ip}, Name: {name}")
    else:
        print("无法确定本地局域网网段。")