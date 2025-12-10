import time
import os
import re
#print(int(input("ch :  ")) ** 2)

#print(bool(0), end="")
#time.sleep(0.5)


# time.sleep(2)
# for i in range(0, 10):
#     time.sleep(0.5)
#     os.system('cls')
#     print("progress >> ", "#"*i)
# print("progress fin")


os.system('cls')
# print("구구단")
# for i in range(1, 10):
#     print("[ ", i , " ]   단")
#     for j in range(1, 10):
#         time.sleep(0.1)
#         print("   {:2d} *{:2d} = {:2d}".format(i,j,i*j))
# print("fin")

# print(time.tzname[1])
# a = "HELLO"
# print(a[1:1])
# s = a.find("f")

# match 2 :
#     case 1 | 2 |3 :
#         print("a")

# if 2 in (1,2,3):
#     print("a")
# print(re.findall(r'\d+',"오늘 방문자 수는 350명이었고")[0])

# ㄴ = [1]
# print(ㄴ.pop(-1))
# print(ㄴ.pop)

# l = (10, 'scccc',2123)
# d = (121, 'uuuu',5667)
# s = [12, 'sdfsd']
# print(l[0:1] + l[1:2])
# print(l[0:0] + tuple(s))

# class list(list):
#     def __init__(self, lt):
#         # 부모 클래스의 __init__ 메소드를 호출하여 name 초기화
#         super().__init__(lt)
        
#     def pop(self, *idx):
#         if len(idx) == 0 and len(self) > 0:
#             return self.pop()
#         if len(idx) == 1 and len(self) > idx[0] and idx[0] >= 0 :
#             return self.pop(idx[0])
#         return None

#     # def npop(self):
#     #     if len(self) > 0 :
#     #         return self.pop()
#     #     return None
# aa = list([1,   2.5 ] )
# print(aa.pop())



# my_list = [1,   2.5 ]
# has_number = any(isinstance(item, (str)) for item in my_list)
# print(has_number)
# isinstance()

# ee = list(range(10))
# print(ee)

# ts = {'a' : 'x', 's' : 'c', 'd' : 'c'}
# ss= list(enumerate( ts.values()))
# # for i in ts.items():
# print(ts.keys({'x'} ))14
# ts.update({'aa':'yy'})
# print(ts )
# 4000
# 3
# print(f"{11/3:.2f}")

# ss = ["aa", 2,5,6]
# sum(ss[1:])

hours1 = [3, 6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
hours2 = [int(i) for i in range(3, 25, 3)]
# print(hours1.)
print(hours1)
print(hours2)
if hours1 == hours2 :
    print(hours1 + hours2)

