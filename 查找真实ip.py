import socket

print("<DigitalTrailBlazer>")
def get_canonical_ip(ip):
    try:
        # 尝试解析 IP 地址，如果成功则返回输入的 IP，因为它已经是正式 IP
        socket.inet_aton(ip)
        return ip
    except socket.error:
        try:
            # 如果输入不是正式 IP，则尝试通过域名解析获取正式 IP
            canonical_name = socket.gethostbyname(ip)
            return canonical_name
        except socket.gaierror:
            return "无法确定有效的 IP 地址"

ip = input("请输入 IP 地址或域名：")
print("真实IP为: ",get_canonical_ip(ip))
print(get_canonical_ip(ip))