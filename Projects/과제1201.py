import requests
import xml.etree.ElementTree as ET

# address= 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ggg.xml'
address= "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
parm = {"key":"0e889e4899cc42991307980aa0210145", "targetDt":"20250101"}
res = requests.get(address,parm )
# res.encoding = 'utf-8'
# print(res.text)
# f_data = list(filter(lambda x:x["rankOldAndNew"] == "NEW", dict(res.json())["boxOfficeResult"]["dailyBoxOfficeList"]))
f_data = [x for x in dict(res.json())["boxOfficeResult"]["dailyBoxOfficeList"] if x["rankOldAndNew"] == "NEW"]

print(f_data)


# for i in i_data :
#     print(i)
# print(len(f_data))





