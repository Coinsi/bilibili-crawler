
import asyncio
import time
from typing import List

import aiotieba as tb
from aiotieba.logging import get_logger as LOG


BDUSS = "dGSG40bk5PRjZ4T0E5M0ZZU1VEbHBndzFEc09jUFpQbGpvZXZQdWRsSlRZb0ptRVFBQUFBJCQAAAAAAAAAAAEAAACJCkV0xbXR1LCutcSz0MW1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFPVWmZT1VpmWD"


async def crawler(fname: str):
    """
    获取贴吧名为fname的贴吧的前32页中浏览量最高的10个主题帖

    Args:
        fname (str): 贴吧名
    """

    start_time = time.perf_counter()
    LOG().info("Spider start")

    # thread_list用来保存主题帖列表
    thread_list: List[tb.typing.Thread] = []

    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client(BDUSS) as client:
        # asyncio.Queue是一个任务队列
        # maxsize=8意味着缓冲区长度为8
        # 当缓冲区被填满时，调用Queue.put的协程会被阻塞
        task_queue = asyncio.Queue(maxsize=8)
        # 当is_running被设为False后，消费者会在超时后退出
        is_running = True

        async def producer():
            """
            生产者协程
            """

            for pn in range(32, 0, -1):
                # 生产者使用Queue.put不断地将页码pn填入任务队列task_queue
                await task_queue.put(pn)
            # 这里需要nonlocal来允许对闭包外的变量的修改操作（类似于引用传递和值传递的区别）
            nonlocal is_running
            # 将is_running设置为False以允许各消费协程超时退出
            is_running = False

        async def worker(i: int):
            """
            消费者协程

            Args:
                i (int): 协程编号
            """

            while 1:
                try:
                    # 消费者协程不断地使用Queue.get从task_queue中拉取由生产者协程提供的页码pn作为任务
                    # asyncio.wait_for会等待作为参数的协程执行完毕直到超时
                    # timeout=1即把超时时间设为1秒
                    # 如果超过1秒未获取到新的页码pn，asyncio.wait_for(...)将抛出asyncio.TimeoutError
                    pn = await asyncio.wait_for(task_queue.get(), timeout=1)
                    LOG().debug(f"Worker#{i} handling pn:{pn}")
                except asyncio.TimeoutError:
                    # 捕获asyncio.TimeoutError以退出协程
                    if is_running is False:
                        # 如果is_running为False，意味着不需要再轮询task_queue获取新任务
                        LOG().debug(f"Worker#{i} quit")
                        # 消费者协程通过return退出
                        return
                else:
                    # 执行被分派的任务，即爬取pn页的帖子列表
                    threads = await client.get_threads(fname, pn)
                    # 这里的nonlocal同样是为了修改闭包外的变量thread_list
                    nonlocal thread_list
                    thread_list += threads

        # 创建8个消费者协程
        workers = [worker(i) for i in range(8)]
        # 使用asyncio.gather并发执行
        # 需要注意这里*workers中的*意为将列表展开成多个参数
        # 因为asyncio.gather只接受协程作为参数，不接受协程列表
        await asyncio.gather(*workers, producer())

    LOG().info(f"Spider complete. Time cost: {time.perf_counter()-start_time:.4f} secs")

    # 按主题帖浏览量降序排序
    thread_list.sort(key=lambda thread: thread.view_num, reverse=True)
    # 将浏览量最高的10个主题帖的信息打印到日志
    for i, thread in enumerate(thread_list[0:1000], 1):
        LOG().info(f"Rank#{i} view_num:{thread.view_num} title:{thread.title}")


# 执行协程crawler
asyncio.run(crawler("孙笑川"))