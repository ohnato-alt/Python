# #1
# pi = 3.141592
# r = int(input("구의 반지름 : "))
# print(f"부피 : {4/3*pi*r**3:.10f}")
# print(f"면적 : {4*pi*r**2:.5f}")

# #2
# w = int(input("밑변 : "))
# h = int(input("높이 : "))
# print(f"빗변 : {(w**2 + h**2)**(1/2)}")

################################################################
print("\n#1")
n1 = int(input("숫자1 : "))
n2 = int(input("숫자2 : "))
print(f"몫 : {n1//n2}  나머지 : {n1%n2}")

print("\n#2")
pi = 3.141592
r = int(input("구의 반지름 : "))
print(f"부피 : {4/3*pi*r**3:.10f}")
print(f"면적 : {4*pi*r**2:.5f}")

print("\n#3")
exc = 1480
m = int(input("달러 $"))
print(f"원화  ₩{exc*m}")

print("\n#4")
n1 = int(input("숫자1 : "))
n2 = int(input("숫자2 : "))
n3 = int(input("숫자3 : "))
print(f"합 : {n1+n2+n3}  평균 : {(n1+n2+n3)/3}")

print("\n#5")
hh = int(input("시 : "))
mm = int(input("분 : "))
ss = int(input("초 : "))
print(f"{hh*3600+mm*60+ss}초 경과")

print("\n#6")
pri = int(input("구입한 상품의 가격 : "))
inc = int(input("손님한테 받은 금액 : "))
print(f"받은 돈 : {inc} 상품 가격 : {pri}")
print(f"부가세 : {int(pri*0.1)} 잔돈 : {int(inc-(pri*1.1))}")

print("\n#7")
x1 = int(input("좌 상단의 x 좌표 : "))
y1 = int(input("좌 상단의 y 좌표 : "))
x2 = int(input("우 하단의 x 좌표 : "))
y2 = int(input("우 하단의 y 좌표 : "))
print(f"두 점이 이루는 직사각형의 넓이는 {abs(x1 - x2) * abs(y1 - y2)}입니다.")


################################################################
print("\n#1")
s1 = input("문자열1 : ")
s2 = input("문자열2 : ")
print(f"{s1} {s2}")
print(f"{s2}"*3)

print("\n#2")
sentence = "I love Python programming"
str = "Python"
idx = sentence.find(str)
print(f"{sentence[idx:idx + len(str)]}")
