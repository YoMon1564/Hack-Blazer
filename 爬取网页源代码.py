import requests

print("<DigitalTrailBlazer>")
def crawl_webpage_source(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出异常

        return response.text
    except requests.exceptions.RequestException as e:
        print(f"爬取网页时出错: {e}")
        return None


def save_to_txt(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == "__main__":
    url = input("请输入要爬取的网页地址: ")
    choice = input("请选择操作（1. 打印至终端；2. 下载至指定txt文件）: ")

    source_code = crawl_webpage_source(url)
    if source_code:
        if choice == '1':
            print(source_code)
        elif choice == '2':
            file_path = input("请输入要保存的txt文件路径及文件名: ")
            save_to_txt(source_code, file_path)
            print(f"已成功将网页源代码保存至 {file_path}")