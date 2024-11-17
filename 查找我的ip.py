import socket

print("<DigitalTrailBlazer>")
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"获取本机IP地址时出错: {e}")
        return None


if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print(f"本机IP地址是: {local_ip}")