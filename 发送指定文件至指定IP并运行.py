import socket
import os

print("DigitalTrailBlazer")
timeout = input("请输入超时时间(秒) <<")
def send_file_to_desktop(ip, port, file_path):
    try:
        # 创建socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)  # 设置超时时间
        sock.connect((ip, port))
        
        # 发送文件内容
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                sock.sendall(data)
        
        print(f"文件 {file_path} 已成功发送到 {ip}:{port}")
    except Exception as e:
        print(f"发送文件时出错: {e}")
    finally:
        sock.close()

def check_ip_validity(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def check_port_validity(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"端口 {port} 在 {ip} 上是开放的")
            return True
        else:
            print(f"端口 {port} 在 {ip} 上未开放")
            return False
    except Exception as e:
        print(f"检查端口时出错: {e}")
        return False
    finally:
        sock.close()

def main():
    while True:
        ip = input("请输入目标IP地址: ")
        if not check_ip_validity(ip):
            print("IP地址无效，请重新输入")
            continue
        
        port = input("请输入目标端口号: ")
        try:
            port = int(port)
            if port < 0 or port > 65535:
                raise ValueError
        except ValueError:
            print("端口号无效，请输入一个0到65535之间的整数")
            continue
        
        if not check_port_validity(ip, port):
            confirm = input("端口未开放，是否继续？(y/n): ")
            if confirm.lower() != 'y':
                print("程序已退出")
                return
        
        file_path = input("请输入要发送的文件路径: ")
        if not os.path.exists(file_path):
            print("文件不存在，请重新输入")
            continue
        
        send_file_to_desktop(ip, port, file_path)
        break

if __name__ == "__main__":
    main()
