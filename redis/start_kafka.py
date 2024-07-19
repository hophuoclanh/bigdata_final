from redis import Redis
from rq import Queue
import subprocess
from tasks import start_kafka


r = Redis(host="192.168.80.69", port="6379")
q = Queue("83", connection=r)


q.enqueue(f=start_kafka)


