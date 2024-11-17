import requests

print("<DigitalTrailBlazer>")
def check_website_status(url):
    try:
        response = requests.get(url)
        print(f"网站状态码: {response.status_code}")
        if response.status_code == 200:
            print("网站可以正常访问")
        elif response.status_code == 404:
            print("页面未找到")
        elif response.status_code == 500:
            print("服务器内部错误")
        else:
            print("其他状态码")
    except requests.RequestException as e:
        print(f"访问网站出错: {e}")
if __name__ == "__main__":
    url = input("请输入网站地址: ")
    check_website_status(url)