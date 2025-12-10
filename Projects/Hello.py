# import time
import os

os.system('cls')
# print(os.cpu_count())
# def recu(val):
#     time.sleep(0.1)
#     print(val)
#     if val > 0:
#         recu(val - 1)
#     return val

# recu(5)
import threading
import time

from tkinter import *
import os

os.system('cls')
#[1]. 화면부터 구성
window= Tk()
window.title('성적처리 프로그램')
window.resizable(False, True)
window.geometry('400x500-200+50')

#[2]. [이름,국어,영어,수학] 성적을 입력하기 위한 위젯만들기
frame1= Frame(window, padx=10, pady=10) #여백
frame1.pack(fill='x')

class Worker(threading.Thread):
    def __init__(self, name, event):
        super().__init__(name=name)
        self.event = event  # Event 객체를 받아옴

    def run(self):
        print(f"{self.name} is starting work")
        time.sleep(3)  # 작업 시뮬레이션 (3초 동안 대기)
        print(f"{self.name} has finished work")
        self.event.set()  # 작업 완료 후 Event를 set → 다른 스레드에 신호 보냄


class Waiter(threading.Thread):
    def __init__(self, name, event):
        super().__init__(name=name)
        self.event = event  # 같은 Event 객체를 받아옴

    def run(self):
        print(f"{self.name} is waiting for event")
        self.event.wait()  # Event가 set될 때까지 대기 (block)
        print(f"{self.name} has noticed that the event was set")


# if __name__ == "__main__":
#     event = threading.Event()  # Event 객체 생성

#     worker = Worker("Worker", event)  # Event를 공유
#     waiter = Waiter("Waiter", event)

#     worker.start()
#     waiter.start()

#     worker.join()
#     waiter.join()

#     print("Main thread has completed")
# ll = Label(frame1, text='국어', font=('',14) )
# ll.grid(row=1, column=0, padx=10, pady=10)
# label_kor= []
# label_kor.append(ll)
# # label_kor.grid(row=1, column=0, padx=10, pady=10)
# # label_kor= Label(frame1, text='국어', font=('',14) ) #글꼴, 글자크기
# # label_kor.grid(row=1, column=0, padx=10, pady=10)
# window.mainloop()
ss = ['d',1]
aa , bb= *ss
print(aa)