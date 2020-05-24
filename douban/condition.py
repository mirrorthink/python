import threading
import time
import random

gMoney = 1000
gcondition = threading.Condition()
gTotleTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gcondition.acquire()
            if gTimes >= gTotleTimes:
                gcondition.release()
                break
            gMoney += money
            print('%s生产了%d元钱，剩余%d元钱'%( threading.current_thread(), money, gMoney))
            gTimes += 1
            gcondition.notify_all()
            gcondition.release()
            time.sleep(0.5)


class Comsumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gcondition.acquire()
            # if gMoney >= money:
            #     gMoney -= money
            #     print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            # else:
            #     if gTimes >= gTotleTimes:
            #         gcondition.release()
            #         break
            #         print('%s消费了%d元钱，剩余%d元钱,不足！'% (threading.current_thread(), money, gMoney))
            while gMoney < money:
                if gTimes >= gTotleTimes:
                    gcondition.release()
                    return
                print('%s准备消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
                gcondition.wait()
            gMoney -= money
            print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gcondition.release()
            time.sleep(0.5)


def main():
    for x in range(3):
        t = Comsumer(name='消费线程%d'%x)
        t.start()

    for x in range(3):
        t = Producer(name='生产线程%d'%x)
        t.start()


if __name__ == '__main__' :
    main()