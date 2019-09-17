from concurrent.futures.thread import ThreadPoolExecutor
import concurrent.futures
from queue import Queue

from Hamster import HamsterGenerator


def generate(i):
    hamster_generator = HamsterGenerator(i)
    hamster = hamster_generator.CreateHamster()
    return hamster
    #print(hamster.name, hamster.count_hair)


work_queue = Queue()
for i in range(0, 100):
    work_queue.put(i)


with concurrent.futures.ThreadPoolExecutor() as executor:
    future_hamster = {}

    """
    {}
    { 'key' : 'value', 'key2' : 'value2'}
    """

    while not work_queue.empty():
        i = work_queue.get()
        future_hamster[executor.submit(generate, i)] = i

    while future_hamster:
        done, not_done = concurrent.futures.wait(future_hamster, return_when=concurrent.futures.FIRST_COMPLETED)

        for future in done:
            i = future_hamster[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (i, exc))
            #else:
             #   print(data.name, data.count_hair)

            del future_hamster[future]

'''executor = ThreadPoolExecutor()
executor.submit(generate(i))'''
