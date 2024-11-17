import subprocess
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
print("此程序由 DigitalTrailBlazer 团队提供技术支持")
time.sleep(1)
print("HackBlazer的调用程序")
time.sleep(1)
front_loaded_suffixPY = input("suffix <<")
if front_loaded_suffixPY == "":
    front_loaded_suffixPY = ".py"
    suffixPY = front_loaded_suffixPY
    print("以默认后缀名为 '.py' !")
print(front_loaded_suffixPY)
time.sleep(1)

while True:
    mainprogramcall = input("mainprogramcall <<")
    mainprogramcall1 = ["invoker -hackblazer","invoker -hb","invoker -HackBlazer","invoker -HB","invoker -HACKBLAZER"]
    if mainprogramcall in mainprogramcall1:#调用HackBlazer程序
        mainprogramcall_input_invoker = input("是否调用HackBlazer (y/n)")
        mainprogramcall2_y = ["y","yes","Y","YES"]
        mainprogramcall3_n = ["N","NO","n","no"]
        if mainprogramcall_input_invoker in mainprogramcall2_y:#调用HackBlazer  -  y
            file_path = ("HackBlazerSTARTPG" + front_loaded_suffixPY)
            if os.path.exists(file_path):#检查文件是否存在
                print("文件正常")
                print("正在调用HackBlazer")
                time.sleep(1)
                subprocess.call(["python","HackBlazerSTARTPG" + front_loaded_suffixPY])
            else:#文件不正常
                print("文件不正常")
        if mainprogramcall_input_invoker in mainprogramcall3_n:#调用HackBlazer  -  n
            print("已取消调用HackBlazer")
    if mainprogramcall == "suffix":#更改后缀名
        front_loaded_suffixPY = input("suffix <<")
        print("已更改后缀名为 " + front_loaded_suffixPY)
        print("需要重启程序")
        subprocess.call(["python","HBuse"+front_loaded_suffixPY])
    target_strings3 = ["cls", "clear", "clear screen", "cls screen"]
    if mainprogramcall in target_strings3:#清屏
        os.system('cls' if os.name == 'nt' else 'clear')
    if mainprogramcall == "exit()":
        print("已退出")
        sys.exit()