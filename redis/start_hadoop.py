import os
import subprocess


def start_hadoop():
   try:
       os.chdir("/home/holanh/Documents/big_data/hadoop-3.4.0/")
       subprocess.run("./sbin/start-all.sh")
       print("hadoop on")
   except:
       print("Already on")
