from tasks import TaskQueue, Task

tq = TaskQueue('neuromancer-seung-import','pull-queue')

for i in range(100):
    t = Task()
    t.chunk_path = '0-1024_0-1024_0-100.npz'
    t.chunk_encoding = 'npz'
    t.info_path = 'snemi3d/segmentation/info'
    tq.insert(t)
