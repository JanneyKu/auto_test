from celery_task import app  # 自己写的app
from celery.result import AsyncResult  # celery模块下的
id = 'b20f827d-dcf5-4fdf-a646-5abb963dc1d3'
if __name__ == '__main__':
    a = AsyncResult(id=id, app=app)
    if a.successful():
        result = a.get()  # task中return的数据:7
        print(result)
    elif a.failed():
        print('任务失败')
    elif a.status == 'PENDING':
        print('任务等待中，尚未被执行')
    elif a.status == 'RETRY':
        print('任务异常后正在重试')
    elif a.status == 'STARTED':
        print('任务已经开始被执行')
