import re
def input_num(tp, titl):
    tptxt = ""
    reptn = ""

    if tp.upper() in ("N") :
        tptxt = "양의 정수"
        reptn = "(\\+|,)"
    elif tp.upper() in ("I") :
        tptxt = "정수"
        reptn = "(\\+|-|,)"
    elif tp.upper() in ("F") :
        tptxt = "숫자"
        reptn = "(\\+|-|\\.|,)"
    else :
        return 0, False

    inp = input(f"{titl if titl else tptxt} 입력 : ").strip()
    if not str(re.sub(reptn, "", inp)).isdecimal() :
        print(f"{tptxt}가 아닙니다.")
        return 0, False

    val = int(inp.replace(",",""))
    if tp.upper() in ("N") and val < 1 :
        print("0보다 큰수를 입력하세요.")
        return 0, False
    
    return val, True

print("\n#1")
inpn1, chk = input_num("N","")
if chk :
    for i in range(inpn1):
        print("Hello World!")

print("\n#2")
inpn1, chk = input_num("N","")
if chk :
    for i in range(inpn1):
        print((i+1)*3, end = " ")

print("\n#3")
tot = 0
while(True) :
    inpn1, chk = input_num("N","")
    if chk :
        if inpn1 == 0 : break
        tot += inpn1
print(f"정수의 합 : {tot}")

print("\n#4")
inpn1, chk = input_num("N","")
if chk :
    print(f"[{inpn1} 단]")
    for i in range(9,0,-1):
        print(f"{inpn1} X {i} = {inpn1*i:3d}")

print("\n#5")
inpn1, chk = input_num("N","입력할 숫자")
if chk :
    i = 1
    tot = 0
    while(True) :
        inpn2, chk = input_num("I",f"숫자{i}")
        if chk :
            tot += inpn2
            if i == inpn1 : break
            i += 1
    print(f"평균 : {tot / inpn1}")

print("\n#6")
i = 1
tot = 0
while(True) :
    inpn2, chk = input_num("N",f"숫자{i}")
    if chk :
        tot += inpn2
        if i == 5 : break
        i += 1
print(f"합계 : {tot}")

print("\n#7")
for i in range(5) :
    print(f"{'o '*i}*")

print("\n#8")
for i in range(1, 100) :
    if i%7==0 or i%9==0 : print(i)

print("\n#9")
inp1 = input("5개의 단어를 입력 : ")
for wrd in inp1.split(",") :
    if len(wrd.strip()) >= 5 : print(wrd.strip(), end=" ")

print("\n#10")
print("구구단1")
for i in range(2, 10, 2):
    print("[ ", i , " ]   단")
    for j in range(1, i + 1):
        print("   {:2d} *{:2d} = {:2d}".format(i,j,i*j))

print("구구단2")
for i in range(1, 10):
    if i%2 != 0 : continue
    print("[ ", i , " ]   단")
    for j in range(1, 10):
        if j > i : break
        print("   {:2d} *{:2d} = {:2d}".format(i,j,i*j))
print("fin")
