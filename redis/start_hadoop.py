from redis import Redis
from rq import Queue
import subprocess
from tasks import start_hadoop

r = Redis(host="192.168.80.69", port="6379")
q = Queue("67", connection=r)


q.enqueue(f=start_hadoop)


