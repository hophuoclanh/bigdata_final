from redis import Redis
from rq import Queue
import subprocess
from tasks import read_delta


r = Redis(host="192.168.80.69", port="6379")
q = Queue("61", connection=r)


q.enqueue(f=read_delta)
