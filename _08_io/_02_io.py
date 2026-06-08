# open('파일경로', 모드(r,w,a), **options)
#- 지정된 경로의 파일을 여는 파이썬 내장 함수
#- 열린 파일에 지정된 모드 동작 수행을 할 수 있다.
f = open('helloworld.txt','r',encoding='utf-8')
text = f.read()
print(text)
f.close() #