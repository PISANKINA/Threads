import os
import subprocess
import sys
import time

create_hamster_sync = os.path.join(os.path.dirname(__file__), "./CreateHamsterSync.py")
create_hamster_queue = os.path.join(os.path.dirname(__file__), "./CreateHamsterQueue.py")
create_hamster_lock = os.path.join(os.path.dirname(__file__), "./CreateHamsterLock.py")
pipes = []

command_sync = [sys.executable, create_hamster_sync]
command_queue = [sys.executable, create_hamster_queue]
command_lock = [sys.executable, create_hamster_lock]
pipe_sync = subprocess.Popen(command_sync)
pipe_queue = subprocess.Popen(command_queue)
pipe_lock = subprocess.Popen(command_lock)
pipes.append(pipe_sync)
pipes.append(pipe_queue)
pipes.append(pipe_lock)

while pipes:
    start_time = time.time()
    #print('START ', time.time() - start_time)
    pipe = pipes.pop()
    pipe.wait()
    print('Выполнено за время: ', time.time() - start_time)
