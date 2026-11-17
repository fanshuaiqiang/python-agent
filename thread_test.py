import threading

import concurrent


def thread_function(i):
    print(f"Thread {i} is running")


if __name__ == '__main__':
    for i in range(5):
        th = threading.Thread(target=thread_function, args=(i,))
        th.start()
        print(f"Thread {i} has been started", th.native_id)

    concurrent.threadPoolExecutor.thread(max_workers=5)