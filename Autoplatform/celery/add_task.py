from celery_task import add
# res=add(1, 2)  # 同步调用
res=add.delay(3,4)  # 把任务提交到redis，系统返回任务uuid：b20f827d-dcf5-4fdf-a646-5abb963dc1d3
print(res)

