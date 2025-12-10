import re
import keyboard 
import time

# def input_num(tp : str, titl : str, req : bool):
def input_num(*arg):
    tp   = ""
    titl = ""
    req  = True
    if len(arg) == 0 : return 0, False
    if len(arg) > 0  : tp   = str(arg[0])
    if len(arg) > 1  : titl = str(arg[1])
    if len(arg) > 2  : req  = bool(arg[2])
    
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

    while(req) :
        inp = input(f"{titl if titl else tptxt + '입력 : '} ").strip()
        if not str(re.sub(reptn, "", inp)).isdecimal() :
            print(f"{tptxt}가 아닙니다.")
            if req : continue
            else : return 0, False

        val = int(inp.replace(",",""))
        if tp.upper() in ("N") and val < 1 :
            print("0보다 큰수를 입력하세요.")
            if req : continue
            else : return 0, False
        return val, True

def wate_key(keys : list[str], titl : str):
    if len(keys) < 1 : exit
    for s in keys : 
        if not(isinstance(s, str)) : quit()
        if len(s) != 1 : exit
    if titl.strip() != "" : print(titl)
    keys = [ s.upper() for s in keys]
    while True :
        # time.sleep(0.1)
        pressed_key = keyboard.read_key().upper()
        for s in keys :
            if s == pressed_key :
                return pressed_key

