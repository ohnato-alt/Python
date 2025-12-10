
print("\n#1")
message = 'Python is fun!'
print("출력 문자열의 길이 : ",len(message))
print("첫 번째 문자 : ",message[0])
print("마지막 문자 : !",message[-1])

print("\n#2")
whitespace_string = " PYTHON "
print(f"[{whitespace_string.strip()}]")

print("\n#3")
print("Python is a great language".find('great') >= 0)

print("\n#4")
tel1 = input("첫번째 자리 입력(3자리) : ")
tel2 = input("두번째 자리 입력(3~4자리) : ")
tel3 = input("세번째 자리 입력(4자리) : ")
print(f"입력된 전화번호는 [ {tel1}-{tel2}-{tel3} ] 입니다.")

print("\n#5")
mail = input("메일 주소 입력(@포함) : ")
idx = mail.find("@")
if idx >= 0 :
    print(f"입력된 메일주소명 : {mail[0:idx - 1]}\n메일서버 이름 : {mail[idx+1:]}")
else:
    print("메일주소가 아닙니다.")

print("\n#6")
message ='''
올해 신년 기자회견에서 저는 AI 연구와 AI 산업이 국가 경쟁력을 좌우할 것이라고 말씀드립니다.
정부는 공공 서비스에 ai를 적극 도입해 행정 효율성을 높일 계획입니다.
특히 의료AI 분야와 재난 대응 AI 시스템은 국민 안전을 지키는 데 중요한 역할을 할 것입니다.
교육 영역에서는 ai 기반 맞춤형 학습과 AI 튜터링 서비스를 확대하겠습니다.
중소기업의 생산성을 높이기 위해 AI 자동화와 AI 데이터 분석 지원 사업을 강화합니다.
산업 전반의 데이터·AI 생태계를 정비해 혁신 기반을 구축하겠습니다.
국방 분야에서도 ai 기술을 활용해 보다 정교한 위협 대응 체계를 마련하겠습니다.
또한 교통·에너지 관리에 AI 예측 모델을 적용해 효율성을 높이겠습니다.
정부는 AI 윤리 기준과 AI 안전 규범을 마련해 기술 발전이 책임 있게 이루어지도록 하겠습니다.
끝으로, ai 혁신이 모두에게 혜택이 될 수 있도록 포용적 성장을 이루겠습니다.
'''
print(f"총 글자수 : {len(message.strip())}")
print(f"총 글자수2 : {len(message.strip().replace(" ","").replace("\n",""))}")
print(f"AI 글자수 : {message.lower().count('ai')}")
