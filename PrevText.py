import olefile

f = olefile.OleFileIO('C:/Users/SSAFY/Downloads/21대 국회의원 공약이행현황/057.220831_더불어민주당 부산북강서갑_전재수 의원실_21대 국회의원 공약이행 및 의정활동 평가.hwp')

#PrvText 스트림 내의 내용을 읽기
encoded_text = f.openstream('PrvText').read()

#인코딩된 텍스트를 UTF-16으로 디코딩
data = encoded_text.decode('UTF-16')
print(data)