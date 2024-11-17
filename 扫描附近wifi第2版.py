import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # 等待扫描完成
    scan_results = iface.scan_results()
    return scan_results

import tkinter as tk
from tkinter import ttk

def update_wifi_list():
    wifi_list.delete(*wifi_list.get_children())  # 清空表格
    results = scan_wifi()
    for result in results:
        wifi_list.insert("", "end", values=(result.bssid, result.ssid, result.signal))

root = tk.Tk()
root.title("WiFi Scan")

label = tk.Label(root, text="<DigitalTrailBlazer>")
label.pack(pady=20)

# 创建表格
wifi_list = ttk.Treeview(root, columns=("Address", "Name", "Signal"), show="headings")
wifi_list.heading("Address", text="Address")
wifi_list.heading("Name", text="Name")
wifi_list.heading("Signal", text="Signal")
wifi_list.pack(fill=tk.BOTH, expand=True)

# 定时刷新
root.after(5000, update_wifi_list)  # 每5秒刷新一次

root.mainloop()

import threading

def scan_wifi_thread():
    while True:
        update_wifi_list()
        root.after(5000)  # 每5秒刷新一次

thread = threading.Thread(target=scan_wifi_thread)
thread.daemon = True
thread.start()
