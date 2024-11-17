import socket
import ipaddress
import subprocess

print("<CipherBreakers>")

def get_local_ip():
    """获取本机的局域网IP地址"""
    try:
        # 创建一个UDP套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到公共DNS服务器
        sock.connect(('8.8.8.8', 80))
        # 获取本地IP地址
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception as e:
        print(f"获取本地IP地址时出错: {e}")
        return None

def scan_network(network):
    """扫描指定网络中的活跃IP地址"""
    active_ips = []
    try:
        # 创建一个IP网络对象
        net = ipaddress.ip_network(network, strict=False)
        for ip in net.hosts():
            try:
                # 使用ping命令检查IP是否活跃
                response = subprocess.run(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if response.returncode == 0:
                    active_ips.append(str(ip))
            except Exception as e:
                print(f"扫描IP {ip} 时出错: {e}")
    except ValueError as e:
        print(f"网络地址格式错误: {e}")
    return active_ips

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print(f"本机局域网IP地址: {local_ip}")
        
        # 假设本机IP在192.168.1.x网段
        network = f"{local_ip.split('.')[0]}.{local_ip.split('.')[1]}.0.0/24"
        print(f"正在扫描网络: {network}")
        
        active_ips = scan_network(network)
        if active_ips:
            print("活跃的IP地址:")
            for ip in active_ips:
                print(ip)
        else:
            print("未发现活跃的IP地址。")
    else:
        print("无法获取本机局域网IP地址。")