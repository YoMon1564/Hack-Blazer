import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

def create_main_window():
    root = tk.Tk()
    root.title("req video")
    root.geometry("600x300")

    label = tk.Label(root, text="<DigitalTrailBlazer>")
    label.pack(pady=10)

    # 创建输入框
    url_label_url = tk.Label(root, text="video url")
    url_label_url.pack(pady=5)
    url_entry1 = tk.Entry(root, width=50)
    url_entry1.pack(pady=10)

    # 创建按钮
    start_button = tk.Button(root, text="Start", command=lambda: start_crawling(url_entry1.get()))
    start_button.pack(pady=20)

    root.mainloop()


def start_crawling(url):
    try:
        response = requests.get(url, stream=True)  # 设置stream为True以分块获取数据，提高效率和节省内存
        response.raise_for_status()
        # 这里简单以获取视频的第一帧画面作为示意（不同视频格式获取首帧方式不同，此为简单模拟）
        first_frame_data = None
        for chunk in response.iter_content(chunk_size=1024):
            if first_frame_data is None:
                first_frame_data = chunk
            else:
                first_frame_data += chunk
            # 简单判断是否达到一定长度，认为获取到首帧，实际情况更复杂需根据视频格式解析判断
            if len(first_frame_data) > 1024 * 1024:  # 示例阈值，可调整
                break

        # 使用PIL库打开获取到的数据（模拟为图片数据）
        image = Image.open(first_frame_data)
        photo = ImageTk.PhotoImage(image)

        # 创建新窗口显示视频的首帧画面（示意）
        new_window = tk.Toplevel()
        new_window.title("视频首帧画面")
        new_window.geometry("400x300")

        video_label = tk.Label(new_window, image=photo)
        video_label.image = photo  # 避免图片被垃圾回收，需保持引用
        video_label.pack(pady=20)

    except requests.RequestException as e:
        messagebox.showerror("错误", f"爬取视频时出错: {e}")


if __name__ == "__main__":
    create_main_window()
    