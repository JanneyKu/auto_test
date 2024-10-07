from celery import Celery
backend='redis://127.0.0.1:6379/1'  # 结果存储
broker='redis://127.0.0.1:6379/2'   # 消息中间件
# app=Celery(‘任务名’, broker=’xxx’, backend=’xxx’)
app=Celery('test', broker=broker, backend=backend) # 传一个字符串，相当于名字
 
 
@app.task
def add(a, b):  # 很耗时的任务
    import time
    time.sleep(3)
    return a + b
