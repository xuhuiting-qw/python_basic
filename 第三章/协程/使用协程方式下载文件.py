import aiohttp
import asyncio

async def download_picture(url,session):
    print(f'开始下载：{url}')
    # 发送网络请求，获取这张图片  请求发出去后，要等待服务器把数据返回，等的这段时间就是IO等待
    response = await session.get(url)
    # 等待数据 （图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是IO等待）
    content = await response.read()
    print('下载完毕')
    with open(url[-10:],'wb') as file:
        file.write(content)
    # 释放链接资源（告诉 aiohttp ，这个链接我不用了，你可以回收了）
    await response.release()


async def main():
    url_list = [
        'https://i0.hdslb.com/bfs/new_dyn/27b9bc0fcf395d0eebcb4d8e2b2af19c520765199.jpg'
    ]
    # 创建会话对象（发请求的工具）
    session = aiohttp.ClientSession()
    # 创建多个协程对象
    coroutines = [download_picture(url,session) for url in url_list]
    # 将多个协程对象交给事件循环
    await asyncio.gather(*coroutines)
    # 关闭会话
    await session.close()


asyncio.run(main())