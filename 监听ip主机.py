import socket
import threading
import tkinter as tk
from tkinter import ttk
import signal
import time
import sys

# 检查单个端口是否开放
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        return False
    except Exception:
        return False
    finally:
        sock.close()


# 监听单个主机的多个端口
def monitor_host_ports(host, ports):
    results = []
    for port in ports:
        open_status = check_port(host, port)
        results.append((port, open_status))
    return results


# 监听多个主机的多个端口
def monitor_multiple_hosts_ports(hosts, ports):
    all_results = []
    for host in hosts:
        host_results = monitor_host_ports(host, ports)
        all_results.extend([(host, port, status) for port, status in host_results])
    return all_results


# 更新GUI显示结果
def update_gui(results):
    for row in treeview.get_children():
        treeview.delete(row)
    for result in results:
        if len(result) == 2:
            host, (port, status) = result
            treeview.insert("", "end", values=(host, port, status))
        elif len(result) == 3:
            host, port, status = result
            treeview.insert("", "end", values=(host, port, status))


# 持续监听的函数
def continuous_monitoring():
    global running
    while running:
        start_time = time.time()
        results = monitor_multiple_hosts_ports(hosts, ports)
        update_gui(results)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # 如果更新时间小于5秒，等待剩余时间，以保证大致每5秒更新一次
        if elapsed_time < 5:
            time.sleep(5 - elapsed_time)


# 定义处理Ctrl+C信号的函数，增强退出功能
def handle_ctrl_c(signal, frame):
    print("接收到Ctrl+C，正在退出程序...")
    global running
    running = False
    global monitor_thread
    if monitor_thread.is_alive():
        monitor_thread.join(timeout=3)  # 最多等待3秒让线程结束
        if monitor_thread.is_alive():
            print("监听线程未能及时停止，强制退出...")
            sys.exit(1)  # 强制退出程序
    root.destroy()
    print("程序已成功退出。")


# 创建GUI窗口
root = tk.Tk()
root.title("网络端口监听")

# 获取用户输入的透明度值（0 - 1之间）
try:
    alpha_value = float(input("请输入窗口透明度（0 - 1之间）："))
    if 0 <= alpha_value <= 1:
        root.attributes('-alpha', alpha_value)
    else:
        print("输入的透明度值不在有效范围内，使用默认值0.7。")
        root.attributes('-alpha', 0.7)
except ValueError:
    print("输入无效，使用默认值0.7。")
    root.attributes('-alpha', 0.7)

root.configure(bg='#333333')

label = tk.Label(root, text="<DigitalTrailBlazer>")
label.pack(pady=20)

# 创建表格
treeview = ttk.Treeview(root, columns=("主机", "端口", "状态"), show="headings")
treeview.heading("主机", text="主机")
treeview.heading("端口", text="端口")
treeview.heading("状态", text="状态")
treeview.pack()

# 获取用户输入的主机和端口信息
hosts_input = input("请输入要监听的主机，多个主机用逗号分隔: ")
hosts = [host.strip() for host in hosts_input.split(',')]
ports_input = input("请输入要监听的端口，多个端口用逗号分隔: ")
ports = [int(port.strip()) for port in ports_input.split(',')]

# 启动监听线程
running = True
monitor_thread = threading.Thread(target=continuous_monitoring)
monitor_thread.start()

# 注册Ctrl+C信号处理函数
signal.signal(signal.SIGINT, handle_ctrl_c)

root.mainloop()