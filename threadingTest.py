import threading
import time


def thread_job():
    # print("This is thread %s" % threading.current_thread())
    print("T start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T stop\n")


def main():
    thread1 = threading.Thread(target=thread_job, name="T1")
    thread1.start()
    # thread1.join()
    print("all done!\n")

    # thread2 = threading.Thread(target=thread_job())
    # thread2.start()

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


if __name__ == '__main__':
    main()
