import socket
import time

print("<DigitalTrailBlazer>")
def send_udp_requests(ip, port, speed):
    # 创建UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet_count = 0
    try:
        while True:
            # 构造一个简单的测试数据包，这里可以根据实际需求修改数据包内容
            data = b"Test UDP Packet"
            sock.sendto(data, (ip, port))

            packet_count += 1
            print(f"已发送第 {packet_count} 个数据包到 {ip}:{port}")

            time.sleep(1 / speed)
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        sock.close()


if __name__ == "__main__":
    ip_address = input("请输入IP地址: ")
    port_number = int(input("请输入端口号: "))
    request_speed = int(input("请输入请求速度（每秒请求次数）: "))

    send_udp_requests(ip_address, port_number, request_speed)