
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
        reptn = "(\\+|-|\\.|,)"
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
data = []
while (True) :
    inpn1, chk = input_num("N","양의 정수" + str(len(data) + 1) + " 입력 : ")
    if chk : data.append(inpn1)
    if len(data) >= 5 : break
    
print("최대값 :", max(data))
print("최소값 :", min(data))
print("총  합 :", sum(data))
print(data)

print("\n#2")
inpn1, chk = input_num("N","")
if chk :
    data = []
    for i in range(inpn1) : data.append(input("문자 " + str(i) + " 입력 : ").strip())
    for i in range(inpn1) : print(i, " : ", data[i])

print("\n#3")
inpn1, chk = input_num("N","학생의 수를 입력하시오")
if chk :
    score_list = []
    while (True) :
        indata, chk = input_num("N","학생 " + str(len(score_list) + 1) + "의 성적을 입력하세요")
        if chk : 
            if 0 < int(indata) < 100 :
                score_list.append(indata)
            else :
                print("잘못된 성적입니다. 다시 입력하시오.")
            if len(score_list) >= inpn1 : break

    for i in range(inpn1) : print(f"학생 {i+1}의 성적 : ", score_list[i])
    print(f"성적 평균은 {sum(score_list)/inpn1:.2f} 입니다.")


print("\n#4")
list1 = [10, 20, 30, 40, 50]
list2 = [ 1, 2 , 3 , 4 , 5 ]
list3 = [list1[n] + list2[(n + 1) * -1] for n in range(len(list1))]
for i in list3 : print(i)

print("\n#5")
scores = [85, 90, 78, 92, 68]
print(f"평균 점수 : {sum(scores)/len(scores):.2f}")
print(f"가장 높은 점수 : {max(scores)}")
print(f"가장 낮은 점수 : {min(scores)}")
scores.sort(reverse=True)
print("오름차순으로 정렬 : ", scores)
print("80점 이상 : ", [n for n in scores if n >= 80])
scores = [n + 5 for n in scores]
print("5점씩 올리 : ", scores)

print("\n#6")
point1 = (2, 3)
point2 = (5, 7)
print(f"point1의 x좌표 : {point1[0]}")
print(f"point2의 y좌표 : {point2[1]}")
print(f"두 좌표 간의 거리 : {((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(1/2)}")

print("\n#7")
phone_book = {
"홍길동": "010-1234-5678",
"김철수": "010-9876-5432",
"이영희": "010-5555-6666"
}
phone_book.update({"박민수" : "010-1111-2222"})
print(phone_book)
phone_book.update({"김철수" : "010-9999-0000"})
print(phone_book)
phone_book.pop("이영희")
print(phone_book)
print(list(phone_book.keys()))
print(list(phone_book.values()))
name = input("사용자로 이름 입력 : ").strip()
print("전화번호 : ", phone_book.get(name))

print("\n#8")
data = [0] * 10
seq = 1
while (True) :
    inpn1, chk = input_num("N","(1부터 100이하의 정수) - " + str(seq) + " 입력 : ")
    if chk : 
        if 0 < int(inpn1) < 100 :
            vl = (int(inpn1) - 1) // 10
            seq +=1
            data[vl] += 1
        else :
            print("잘못된 숫자입니다. 다시 입력하시오.")
            
        if seq > 10 : break

for i in range(len(data)) : print(f"{(i * 10) + 1:2d} - {(i * 10) + 11:3d} : {'*' * data[i]}")

print("\n#9")
seq = 10
data = [0] * seq
while (True) :
    chk = input("\n좌석을 예약하시겠습니까( 1(Y) 또는 0(N) )? ").strip().upper()
    if chk in ("1", "Y") :
        print("\n", "-"*35, "\n 좌석 번호 :", end = " ")
        for i in range(seq) : print(i + 1, end = " ")
        print("\n", "-"*35, "\n 예약 상태 :", end = " ")
        for i in data : print(i, end = " ")

        while (True) :
            inpn1, chk = input_num("N","\n몇번째 좌석을 예약하시겠습니까?")
            if chk : 
                vl = int(inpn1)
                if 0 < vl <= 10 :
                    if data[vl - 1] == 0 : data[vl - 1]  = 1
                    else : print("죄송합니다. 이미 예약된 좌석입니다. 다른 좌석을 선택해 주세요.")
                    break
                else :
                    print("잘못된 숫자입니다. 다시 입력하시오.")

    elif chk in ("0", "N") : 
        print("예약을 종료합니다.")
        break
    
print("\n#10")
cls_scr = []
cls = 1
while (True) :
    inpn1, chk = input_num("N",f"[{cls}반] 인원 수 입력 : ")
    if chk :
        mem  = int(inpn1)
        mem_scr = []
        cnum = 1
        while (True) :
            inpn1, chk = input_num("N",f"[{cls}반 {cnum:2d}번] : ")
            if chk : 
                scor = int(inpn1)
                if 0 <= scor < 100 :
                    mem_scr.append(scor)
                    cnum += 1
                else :
                    print("잘못된 숫자입니다. 다시 입력하시오.")
            
            if cnum > mem : break
        cls_scr.append(mem_scr)
        cls += 1
        
    print()
    if cls > 3 : break

print("--- Python Programming 성적표 ----")
for i in range(0, len(cls_scr)) :
    prt = f" [{i + 1}반] "
    for j in cls_scr[i] : prt += f"{j:2d} "
    print(prt +f"[평균 : {sum(cls_scr[i])/len(cls_scr[i]):.1f}]")
    
print("-----------------------")
    
print("\n#11")
class1 = {"홍길동", "김철수", "이영희", "박민수"}
class2 = {"이영희", "김철수", "최지훈", "정은비"}
    
print("전체 참여자 명단(중복제거) : ", class1.union(class2))
print("두 반 모두 참여한 학생 : ", class1.intersection(class2))
print("1반만 참여한 학생 : ", class1.difference(class2))
print("2반만 참여한 학생 : ", class2.difference(class1))
    
print("전체 참여자 명단(중복제거) : ", class1 | class2)
print("두 반 모두 참여한 학생 : ", class1 & class2)
print("1반만 참여한 학생 : ", class1 - class2)
print("2반만 참여한 학생 : ", class2 - class1)
