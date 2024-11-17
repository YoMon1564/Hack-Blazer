import time
import subprocess
import platform
import sys
import os
import tkinter as tk

os.system('cls' if os.name == 'nt' else 'clear')

front_loaded_suffixPY = input("suffix <<")

if front_loaded_suffixPY == "":
    front_loaded_suffixPY = ".py"
    suffixPY = front_loaded_suffixPY
    print("以默认后缀名为 '.py' !")
print(f"后缀为{front_loaded_suffixPY}")

time.sleep(0.5)
print("正在检查 DigitalTrailBlazer-hackblazer协议 是否异常")
time.sleep(0.5)
file_path2 = ("DigitalTrailBlazer-hackblazer协议" + front_loaded_suffixPY)
if os.path.exists(file_path2):
    print("正常")
else:
    print("异常")
    sys.exit()

time.sleep(0.5)
def on_mousewheel(event):
    # 根据鼠标滚轮方向滚动文本框的视图
    text_widget.yview_scroll(int(-1 * (event.delta / 120)), "units")
def agree():
    root.destroy()
def decline():
    print("已为您退出该程序")
    os.system('cls' if os.name == 'nt' else 'clear')
    root.destroy()
    sys.exit()
root = tk.Tk()
root.title("协议")
root.geometry("800x500")
# 用于标记用户是否已经做出选择的变量
choice_made = False
def enable_program_continue():
    global choice_made
    choice_made = True
text_widget = tk.Text(root)
text_widget.pack(fill=tk.BOTH, expand=True)
text_widget.insert(tk.END, "<DigitalTrailBlazer>\n")
text_widget.insert(tk.END, """
HackBlazer免责声明
用户在使用本软件前应仔细阅读本免责声明，继续使用表示用户接受所有条款。
本软件的使用受限于用户已获得合法授权，开发者不对用户授权的合法性进行审查，用户自行对因授权问题导致的法律后果负责。
本软件可能存在未知漏洞或错误，尽管开发者尽力改进，但对于因这些问题导致的用户数据丢失、系统损坏或其他不良后果，开发者不承担责任。
用户不得将本软件用于任何非法目的，如网络犯罪、恶意攻击、未经授权的系统入侵等，否则将依法承担全部责任。
本软件仅供合法的安全测试、网络研究、企业内部安全评估等授权场景使用，未经授权用于其他目的属于用户违规行为。
在使用本软件进行操作时，用户应采取合理措施防止对目标系统造成损害，因用户疏忽造成的损失由用户自行承担。
对于因不可抗力（如自然灾害、战争、政府行为、网络故障等超出开发者控制范围的情况）导致的软件问题或用户损失，开发者不承担责任。
本软件的使用许可仅授予用户个人或特定授权实体，未经许可不得分发、共享、出租、出售本软件，否则用户承担侵权责任。
用户不得利用本软件对政府机构、军事设施、关键基础设施（能源、通信、金融等）进行未经授权的访问或攻击，否则自行承担法律后果。
本软件不保证与所有的操作系统、硬件设备或其他软件完全兼容，因兼容性问题导致的问题，开发者不承担责任。
用户使用本软件产生的任何直接或间接损失，包括但不限于经济损失、数据损失、业务中断等，开发者不承担赔偿责任。
开发者不承担因用户使用本软件对第三方造成损害而引发的任何责任，包括但不限于第三方索赔、诉讼等。
用户不得使用本软件收集、存储或传播违反隐私法规的个人信息，若有违反，用户承担责任。
若用户修改本软件或创建衍生作品且未获得开发者书面同意，将承担知识产权相关法律责任。
本软件仅作为一种工具提供，用户应对其使用行为和相关决策负责，开发者不对用户的决策失误承担责任。
用户不得使用本软件干扰或破坏其他软件、网络服务的正常运行，如有违反，自行承担后果。
对于因软件更新、升级或停用导致的用户不便或损失，开发者不承担责任，用户应自行备份数据。
用户在使用本软件过程中若遇到技术问题，开发者可提供有限支持，但不保证问题一定能解决。
本软件中的任何信息、数据或功能仅作为参考，用户不应完全依赖，因依赖产生的问题开发者不负责。
开发者不承担因用户在软件使用过程中违反道德准则或行业规范而产生的任何后果。
本软件可能会受到网络环境的影响，如网络延迟、丢包等，开发者不对由此产生的问题负责。
用户不得使用本软件对教育机构、医疗机构、公益组织等特殊保护对象进行未经授权的渗透测试。
若用户利用本软件进行商业间谍活动、不正当竞争等违法商业行为，将依法承担责任。
本软件的知识产权归开发者所有，用户不得删除、掩盖或篡改软件中的知识产权标识。
用户不得使用本软件故意制造虚假信息、误导用户或进行欺诈活动，否则承担法律责任。
在使用本软件进行渗透测试等操作时，应遵守相关的安全标准和规范，因违反导致的问题用户负责。
开发者有权根据法律法规、技术发展等情况对软件进行修改或终止服务，用户应接受。
""")
# 绑定鼠标滚轮事件
text_widget.bind("<MouseWheel>", on_mousewheel)
agree_button = tk.Button(root, text="我同意", command=lambda: [agree(), enable_program_continue()])
agree_button.pack(pady=20)
decline_button = tk.Button(root, text="我拒绝", command=lambda: [decline(), enable_program_continue()])
decline_button.pack()
# 主循环，等待用户做出选择
while not choice_made:
    root.update()

os.system('cls' if os.name == 'nt' else 'clear')
print("您已同意本协议")
print("""
---------------------------------------------------------------------------------------
      """)
print("此程序由 DigitalTrailBlazer 团队提供技术支持")
time.sleep(1)

print("""
 <DigitalTrailBlazer>
======================
     此程序仅供教学
  切勿用于任何非法活动
======================
""")

time.sleep(0.5)
system_name = platform.system()
if system_name != "Windows":
    print("当前系统不是Windows系统")
else:
    print("当前使用的系统为Windows系统")

time.sleep(0.5)
versionnumber = "computer client side [1.1.2] - Chinese"
print(f"您使用的版本为 <DigitalTrailBlazer> HackBlazer - [{versionnumber}]")

time.sleep(0.5)
while True:
    try:
        program = input("<DigitalTrailBlazer>HackBlazer <<")
        if program == "check -m -l":#查看指定的库是否下载
            subprocess.call(["python","查看指定的库是否下载" + suffixPY])
        if program == "check -all -v":#查看所有内置病毒
            subprocess.call(["python","查看所有内置病毒" + suffixPY])
        if program == "check -wifi key/csdn":#查找wifi的密码
            subprocess.call(["python","csdn-查找wifi的密码" + suffixPY])
        if program == "check -m -web":#查找网段
            subprocess.call(["python","查找网段" + suffixPY])
        if program == "open cal":#打开计算机
            subprocess.call(["python","打开计算机" + suffixPY])
        if program == "find -r -ip":#查找真实ip
            subprocess.call(["python","查找真实ip" + suffixPY])
        if program == "use -ddos/1":#启用DDoS攻击 第1版
            subprocess.call(["python","DDoS攻击 第1版" + suffixPY])
        if program == "find -vul -ip":#查找指定ip的漏洞
            subprocess.call(["python","查找指定ip的漏洞" + suffixPY])
        if program == "check -m -ip":#查找我的ip
            subprocess.call(["python","查找我的ip" + suffixPY])
        if program == "use -ddos/2":#启用DDoS攻击 第2版
            subprocess.call(["python3","DDoS攻击 第2版" + suffixPY])
        if program == "check -internet card":#查看当前网卡
            subprocess.call(["python3","查看当前网卡" + suffixPY])
        if program == "req -web code":#爬取网页源代码
            subprocess.call(["python3","爬取网页源代码" + suffixPY])
        if program == "check -web":#查看指定网站的状态
            subprocess.call(["python","查看指定网站的状态" + suffixPY])
        target_strings1 = ["use -ddos/github", "use -ddos/gh", "use -ddos/GH", "use -ddos/GitHub", "use -ddos/GITHUB"]
        if program in target_strings1:#启用GH的DDoS攻击
            subprocess.call(["python","GH-DDoS攻击" + suffixPY])
        target_strings2 = ["web tools/github", "web tools/gh", "web tools/GH", "web tools/GitHub", "web tools/GITHUB"]
        if program in target_strings2:#启用GH的网络工具
            subprocess.call(["python","GH-网络工具" + suffixPY])
        if program == "listen -ip":#监听指定IP主机
            subprocess.call(["python","监听ip主机" + suffixPY])
        if program == "open game1":#启动内置小游戏---1
            subprocess.call(["python","game1" + suffixPY])
        if program == "use -ddos/3":#启用DDoS攻击 第3版
            subprocess.call(["python","DDoS攻击 第3版" + suffixPY])
        if program == "send file -ip host [run]":#向指定ip主机发送文件并运行
            subprocess.call(["python","发送指定文件至指定IP并运行" + suffixPY])
        if program == "scan -n -wifi/2":#扫描附近wifi 第2版
            subprocess.call(["python","扫描附近wifi第2版" + suffixPY])
        if program == "scan -n -wifi/3":#扫描附近wifi 第3版
            subprocess.call(["python","扫描附近wifi第3版" + suffixPY])
        if program == "help":#查看HackBlazer的所有代码
            subprocess.call(["python","帮助" + suffixPY])
        if program == "scan -m -lan":#扫描局域网和局域网内部活跃IP
            subprocess.call(["python","扫描局域网和局域网内部活跃IP" + suffixPY])
        if program == "req -web ip":#爬取网站的IP
            subprocess.call(["python","爬取网站IP" + suffixPY])
        target_strings5 = ["use -ddos-py3/gh", "use -ddos-py3/gh", "use -ddos-py3/GH", "use -ddos-py3/GitHub", "use -ddos-py3/GITHUB"]
        if program in target_strings5:#启用GH的DDoS攻击
            subprocess.call(["python","GH-DDos" + suffixPY])
        target_strings6 = ["use -sql","use -Sql","use -SQl","use -SQL"]
        if program in target_strings6:#使用GH-sqlnmap
            subprocess.call(["python","GH-sqlnmap" + suffixPY])
        if program == "use -new cmd":#使用新的cmd终端
            subprocess.call(["python","创建新的cmd" + suffixPY])
        target_strings3 = ["cls", "clear", "clear screen", "cls screen"]
        if program in target_strings3:#清屏
            os.system('cls' if os.name == 'nt' else 'clear')
        target_strings4 = ["hackblazer -version","hb -version","HackBlazer -version","HB -version","hackblazer version","hb version","HackBlazer version","HB version","version","vs","VS","VerSion","VERSION"]
        if program in target_strings4:#查看版本
            print(f"您使用的版本为 <CipherBreakers> HackBlazer - computer client side[{versionnumber}] - 中文版")
        if program == "rep -video":#爬取视频
            subprocess.call(["python","爬取视频" + suffixPY])
        if program == "exit()":#退出
            print("已为您退出该程序")
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
    except Exception as e:
        print(f"发生错误：{e}")