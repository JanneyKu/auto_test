from celery_task import add
# res=add(1, 2)  # 同步调用
res=add.delay(3,4)  # 把任务提交到redis，系统返回任务uuid：b20f827d-dcf5-4fdf-a646-5abb963dc1d3
print(res)
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
                        
原文链接：https://blog.csdn.net/chinawangfei/article/details/125441684
