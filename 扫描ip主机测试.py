import nmap
import time

print("<DigitalTrailBlazer>")
def scan_vulnerabilities(ip):
    nm = nmap.PortScanner()
    try:
        # 执行全面的扫描，包括版本检测和脚本扫描以查找漏洞
        print(f"开始对 {ip} 进行扫描，请稍候...")
        start_time = time.time()
        nm.scan(ip, arguments='-sV -sC')

        total_hosts = len(nm.all_hosts())
        scanned_hosts = 0

        print(f"对 {ip} 的扫描结果：")
        with open(f"{ip}_scan_results.txt", "w") as f:
            for host in nm.all_hosts():
                scanned_hosts += 1
                progress = scanned_hosts / total_hosts * 100
                print(f"扫描进度：{progress:.2f}%", end="\r")

                f.write(f"主机：{host}\n")
                if 'tcp' in nm[host]:
                    for port in nm[host]['tcp']:
                        f.write(f"  端口 {port}：{nm[host]['tcp'][port]['name']} {nm[host]['tcp'][port]['product']} {nm[host]['tcp'][port]['version']}\n")
                        if 'script' in nm[host]['tcp'][port]:
                            f.write(f"    脚本结果：{nm[host]['tcp'][port]['script']}\n")

            print()  # 换行，避免下一次输出覆盖进度信息

        end_time = time.time()
        print(f"扫描完成，耗时：{end_time - start_time:.2f} 秒。扫描结果已保存到 {ip}_scan_results.txt 文件中。")
    except nmap.PortScannerError as e:
        if "not found" in str(e):
            print(f"未找到Nmap程序，请确保Nmap已正确安装并在系统路径中可被找到。错误信息：{e}")
        elif "insufficient privileges" in str(e):
            print(f"权限不足，无法执行扫描操作。请以具有足够权限的用户身份运行程序。错误信息：{e}")
        else:
            print(f"执行Nmap扫描时出现错误：{e}")
    except Exception as e:
        print(f"扫描过程中出现其他错误：{e}")


if __name__ == "__main__":
    ip = input("请输入要扫描的IP地址：")
    scan_vulnerabilities(ip)