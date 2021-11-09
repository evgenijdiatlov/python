import threading
import time
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

def thread_function(name):
    print("Thread: starting "+str(name))
    time.sleep(2)
    print("Thread: finishing "+str(name))

if __name__ == "__main__":
    start = time.time()
    threads = list()
    for index in range(10):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    index = 0
    for thread in threads:
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
        index += 1
    print(time.time() - start)
    logging.info("Main    : threads Done")
    