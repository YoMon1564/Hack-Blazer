import requests
from bs4 import BeautifulSoup

print("<DigitalTrailBlazer>")
# 设置请求超时时间（秒）
REQUEST_TIMEOUT = 8


def detect_xss_vulnerability(url):
    try:
        payload = "<script>alert('XSS');</script>"
        response = requests.get(url, params={'input': payload}, timeout=REQUEST_TIMEOUT)
        soup = BeautifulSoup(response.text, 'html.parser')
        if payload in soup.prettify():
            print(f"在 {url} 检测到跨站脚本漏洞（XSS）")
            return True
        print(f"在 {url} 未检测到跨站脚本漏洞（XSS）")
        return False
    except requests.exceptions.RequestException as e:
        print(f"检测XSS漏洞时出错: {e}")
        return False


def check_for_missing_elements(url):
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # 这里假设检测是否存在某个关键的 <meta> 元素，比如用于设置字符编码的
        meta_encoding_element = soup.find('meta', {'charset': True})
        if not meta_encoding_element:
            print(f"在 {url} 可能存在潜在漏洞，未检测到关键的 <meta> 元素（用于设置字符编码）。")
            return True
        print(f"在 {url} 未发现因关键 <meta> 元素缺失导致的潜在漏洞。")
        return False
    except requests.exceptions.RequestException as e:
        print(f"检查元素缺失漏洞时出错: {e}")
        return False


if __name__ == "__main__":
    target_ip = input("ip <<")
    target_url = f"http://{target_ip}/"  # 假设目标IP上有Web服务，这里是对应的URL

    detect_xss_vulnerability(target_url)
    check_for_missing_elements(target_url)