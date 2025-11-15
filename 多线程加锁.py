import threading
import time

# 添加进程互斥锁

# 进程是系统进行资源调度的最小单位
# 线程是cpu调度的最小单位


lock = threading.Lock()
global_sum = 0

def myadd1():
    global global_sum
    for i in range(1,1000000):
        # 添加锁
        lock.acquire_lock()
        global_sum += i
    #     释放锁
        lock.release_lock()
    print('myadd1',global_sum)

def myadd2():
    global global_sum
    for i in range(1,1000000):
        # 添加锁
        lock.acquire_lock()
        global_sum += i
    #     释放锁
        lock.release_lock()
    print('myadd2',global_sum)

if __name__ == '__main__':
    thread1 = threading.Thread(target=myadd1)
    thread2 = threading.Thread(target=myadd2)

    thread1.start()
    thread2.start()

    time.sleep(1)
    print(f"主进程{global_sum}")