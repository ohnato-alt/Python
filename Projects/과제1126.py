# import pandas as pd
# fread = pd.read_excel(r"C:\Users\Admin\MBCA\exceltest.xlsx")

# from openpyxl import load_workbook
# fread = load_workbook(r"C:\Users\Admin\MBCA\exceltest.xlsx")
# # ws = fread.shared_strings
# # aa = 
# # print(list(fread.sheetnames).index("sheet1"))
#         #  .["sheet1"])
# print(str(fread.worksheets[fread.sheetnames.index("Sheet3")].cell(1,1).value))
 

# with open("C:\\Users\\Admin\\MBCA\\test.txt", "a", encoding="utf-8", newline ="\r\n") as f_test :
#     f_test.writelines(["test", "dddd","cxcx"])
#     print(f_test.detach())

import re
import random
import datetime
import urllib.request as req

# print(random.sample([2,5,6,7], 3))
# ss = datetime.datetime.now()
# print(ss)
# print(datetime.datetime.now().timestamp())

# url = 'https://www.naver.com/'
# try :
#         resp = req.urlopen(url)
# except req.HTTPError:
#         print()
# htm = str(resp.read().decode('utf-8'))
# p1 = htm.find('연합뉴스')
# print(htm[p1: p1 +100])

# import datetime
# print(datetime.datetime.now())
# print((datetime.datetime.now() - datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
s = [1,2,3]
print(list(x for x in s if x > 1 ))