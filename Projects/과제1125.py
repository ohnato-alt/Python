import re
def input_num(tp : str, titl : str):
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
        reptn = "(\\+|-|.|,)"
    else :
        return 0, False

    inp = input(f"{titl if titl else tptxt + '입력 : '} ").strip()
    if not str(re.sub(reptn, "", inp)).isdecimal() :
        print(f"{tptxt}가 아닙니다.")
        return 0, False

    val = int(inp.replace(",",""))
    if tp.upper() in ("N") and val < 1 :
        print("0보다 큰수를 입력하세요.")
        return 0, False
    return val, True

print("\n#1")
def new_max(*data) :
    if len(data) == 0 : return 0
    rtn : int = data[0]
    if len(data) > 1 :
        for i in data[1:] :
            if i > rtn : rtn = i
    return rtn

def new_min(*data) :
    if len(data) == 0 : return 0
    rtn : int = data[0]
    if len(data) > 1 :
        for i in data[1:] :
            if i < rtn : rtn = i

    return rtn

print(new_max(32,3,66,44,5))
print(new_min(32,3,66,44,5))

print("\n#2")
def cel_to_fah(Cel) :
    return 1.8*Cel+32

def fah_to_cel(Fah) :
    return (Fah-32) / 1.8

print(cel_to_fah(20))
print(fah_to_cel(68))

print("\n#3")
def gugu(val1, val2) : 
    for i in range(min(val1, val2), max(val1, val2) + 1):
        print("[ ", i , " ]   단")
        for j in range(1, 10):
            print("   {:2d} *{:2d} = {:2d}".format(i,j,i*j))

gugu(6,3)

print("\n#4")
def fibonacci_call(num1 : int, num2 : int, rem : int) :
    if rem < 2 : return
    num3 = num1 + num2
    print("," + str(num2), end = "")
    rem -= 1
    fibonacci_call(num2, num3, rem)
     

def fibonacci(rem : int) :
    print("0", end = "")
    fibonacci_call(0, 1, rem)

inpn1, chk = input_num("N", "")
if chk : fibonacci(inpn1)

