import requests

def download_picture(url):
    print(f'开始下载：{url}')
    # 发送网络请求，获取这张图片
    response = requests.get(url)
    print('下载完毕')
    with open(url[-10:],'wb') as file:
        file.write(response.content)


def main():
    url_list = [
        'https://i0.hdslb.com/bfs/new_dyn/27b9bc0fcf395d0eebcb4d8e2b2af19c520765199.jpg'
    ]
    for n in url_list:
        download_picture(n)

main()