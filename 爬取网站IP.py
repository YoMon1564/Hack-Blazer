import socket

website_url = input("请输入网站地址 <<")
try:
    ip_address = socket.gethostbyname(website_url)
    print(f"网站 {website_url} 对应的IP地址是: {ip_address}")
except socket.gaierror as e:
    print(f"解析网站地址 {website_url} 出现错误: {e}")