import time
import re

print("\n#1")
req = input("입력 : ")
req2 = req.replace(" ","").replace("\t","")
if req2 == "안녕" :
    print("안녕하세요.")
elif req2 == "안녕하세요" :
    print("안녕하세요.")
elif req2 in ("지금몇시야?", "지금몇시예요?") :
    print(f"지금은 {time.localtime().tm_hour}시 입니다.")
else :
    print(req)

print("\n#2")
inp = input("점수 입력 : ")
if inp.isdecimal() :
    req = int(inp)
    for i in range(2,6):
        print(f"{req}은 {i}로나누어 떨어지는 숫자", end ="")
        print("가 아닙니다.") if req%i else print(" 입니다.") 
else :
    print("정수가 아닙니다.")

#################################################################################

print("\n#1")
inp = input("숫자 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp)).isdecimal() :
    print(f"절대값 : {abs(int(inp.replace(",","")))}")
else :
    print("정수가 아닙니다.")

print("\n#2")
inp1 = input("숫자1 입력 : ")
inp2 = input("숫자2 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp1 + inp2)).isdecimal() :
    inpn1 = int(inp1.replace(",",""))
    inpn2 = int(inp2.replace(",",""))
    res = inpn1 if inpn1 < inpn2 else inpn2
    print(f"작은수 : {res}")
else :
    print("정수가 아닙니다.")

print("\n#3")
inp1 = input("숫자1 입력 : ")
inp2 = input("숫자2 입력 : ")
inp3 = input("숫자3 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp1 + inp2 + inp3)).isdecimal() :
    inpn1 = int(inp1.replace(",",""))
    inpn2 = int(inp2.replace(",",""))
    inpn3 = int(inp3.replace(",",""))
    max = inpn1
    max = max if inpn1 > inpn2 else inpn2
    max = max if inpn1 > inpn3 else inpn3
    print(f"max : {max}")
else :
    print("정수가 아닙니다.")

print("\n#4")
inp1 = input("숫자1 입력 : ")
inp2 = input("숫자2 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp1 + inp2)).isdecimal() :
    print(f"max : {abs(int(inp1.replace(",","")) - int(inp2.replace(",","")))}")
else :
    print("정수가 아닙니다.")

print("\n#5")
inp1 = input("숫자1 입력 : ")
inp2 = input("숫자2 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp1 + inp2)).isdecimal() :
    inpn1 = int(inp1.replace(",",""))
    inpn2 = int(inp2.replace(",",""))
    res = (inpn1 - inpn2) if inpn1 > inpn2 else (inpn2 - inpn1)
    print(f"max : {res}")
else :
    print("정수가 아닙니다.")

print("\n#6")
saved_id = "python"
saved_pw = "1234"
inp1 = input("ID 입력 : ").strip()
inp2 = input("패스워드 입력 : ").strip()
if saved_id == inp1 and saved_pw == inp2:
    print("로그인 성공")
else :
    print("로그인 실패")

print("\n#7")
inp1 = input("숫자1 입력 : ")
if str(re.sub("(\\+|\-|\,)", "", inp1)).isdecimal() :
    inpn1 = int(inp1.replace(",",""))
    if 0<=inpn1<50 :
        print("낮음")
    elif 50<=inpn1<80 :
        print("보통")
    elif 80<=inpn1<100 :
        print("높음")
    else :
        print("범위를 벗어남")
else :
    print("정수가 아닙니다.")

print("\n#8")
inp1 = input("문장 입력 : ")
if inp1.lower().find("error") >= 0 :
    print("오류 포함")
else :
    print("정상")

print("\n#9")
inp1 = input("숫자1 입력 : ")
inp2 = input("숫자2 입력 : ")
inp3 = input("숫자3 입력 : ")
if str(re.sub("(\\+|\-|\,)", "",(inp1 + inp2 + inp3))).isdecimal() :
    inpn1 = int(inp1.replace(",",""))
    inpn2 = int(inp2.replace(",",""))
    inpn3 = int(inp3.replace(",",""))
    max = inpn1
    max = max if inpn1 > inpn2 else inpn2
    max = max if inpn1 > inpn3 else inpn3
    evg = (inpn1 + inpn2 + inpn3) / 3
    print(f"가장 큰 값 : {max}")
    print(f"평균 : {evg}")
    print(f"{'통과' if evg >= 70 else '불합격'}")
    print(f"{'정수 평균' if evg.is_integer() else '실수 평균'}")
else :
    print("정수가 아닙니다.")

print("\n#10")
inp1 = input("파일명 입력 : ").strip()
if inp1 in ("2025") : print("올해 파일")
if inp1.startswith("report") : print("보고서 유형")
if inp1.endswith(".csv") : print("CSV 데이터 파일")

print("\n#11")
visited = '오늘 방문자 수는 350명이었고, 어제는 280명이었다.'
val1 = int(re.findall(r'\d+',visited.split(",")[0])[0])
val2 = int(re.findall(r'\d+',visited.split(",")[1])[0])
print(f"차이 : {abs(val1 - val2)}")
print("증가" if val1 > val2 else "감소" if val1 < val2 else "")

print("\n#12")
inp1 = input("문장 입력 : ").strip()
txt  = ", 감탄 문장" if inp1.endswith("!") else ""
txt += ", 의문 문장" if inp1.endswith("?") else ""
txt += ", 긴 문장" if len(inp1) >= 30 else ""
txt += ", 숫자 포함 문장" if len(re.findall(r'\d+',inp1)) else ""
print(txt[2:])
