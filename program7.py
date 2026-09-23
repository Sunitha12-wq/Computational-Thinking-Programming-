import threading
import queue
import time

storage = queue.Queue(maxsize=5)

def producer():
    for number in range(1, 11):
        storage.put(number)
        print(f"Added: {number}")
        time.sleep(0.5)

    storage.put(None)  # Signal that production is finished

def consumer():
    while True:
        value = storage.get()

        if value is None:
            break

        print(f"Removed: {value}")
        storage.task_done()
        time.sleep(1)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Adding and Removing Completed")