
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import module.oescm as cm
import os

class MasData :
    cdata = pd.DataFrame()
    def __init__(self) :
        self.cdata = pd.DataFrame()
        
    def file_read(self) :
        root = tk.Tk()
        root.withdraw() 
        filename = filedialog.askopenfilename(
            title="파일을 선택해 주세요", # 대화 상자 제목 설정
            initialdir=os.getcwd(),     # 초기 디렉터리를 현재 작업 폴더로 설정
            filetypes=(
                ("엑셀파일", "*.xls;*.xlsx"),  # 표시할 파일 형식 필터링
                ("모든 파일", "*.*")
            )
        )
        self.input_file(filename)

    def input_file(self, filename) :
        if filename.strip() != "" :
            self.cdata = pd.read_excel(filename)
            print("파일을 읽었습니다.")

    def input_term(self) :
        if len(self.cdata) > 0 :
            idata = {}
            for c in self.cdata.columns :
                if c == "월" :
                    val, fl = cm.input_num("N", c + "를 입력 하세요. : ")
                    if fl : idata.update({c : [str(val) + c]})
                else :
    # 월	평균기온(°C)	최고기온(°C)	최저기온(°C)	강수량(mm)	습도(%)
                    val, fl = cm.input_num("F", c + "를 입력 하세요. : ")
                    if fl : idata.update({c : [val]})
            self.cdata = pd.concat([self.cdata, pd.DataFrame(idata)])

mdata = MasData()

while(True) :
    
    os.system('cls')
    key = cm.wate_key(['D','F', 'I', 'Q', 'T'],"작업 선택 --- 내용보기 : D , 파일입력 : F, 추가입력 : I, 종    료 : Q")

    if key == "D" :
        print(mdata.cdata)
        os.system("pause")
    elif key == "F" :
        mdata.input_file("C:/Users/Admin/MBCA/seoul_weather_2025.xlsx")
        # mdata.file_read()
        os.system("pause")
    elif key == "I" :
        mdata.input_term()
    elif key == "Q" :
        break
    










# Tkinter 기본 창 생성 및 숨기기
# 파일 대화 상자만 필요하므로 메인 Tk 창은 숨깁니다.

# 파일 선택 대화 상자 열기
# 선택된 파일 경로는 filename 변수에 저장됩니다.

# C:/Users/Admin/MBCA/seoul_weather_2025.xlsx