import threading
from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures

from Hamster import HamsterGenerator

hamsters = {}


class HamsterGeneratorLock:

    def __init__(self):
        self.__mutex = threading.RLock()

    def generate(self, i):
        hamster_generator = HamsterGenerator(i)
        hamster = hamster_generator.CreateHamster()
        #self.__mutex.acquire()
        with self.__mutex:
            hamsters[i] = hamster
            #hamsters.append(hamster)
        #self.__mutex.release()


with concurrent.futures.ThreadPoolExecutor() as executor:
    hamster_generator_lock = HamsterGeneratorLock()

    for i in range(0, 100):
        executor.submit(hamster_generator_lock.generate, i)

#for i in hamsters:
#    print(i, hamsters[i].name)
