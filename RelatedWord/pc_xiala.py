#coding:utf-8
import requests,re,sys
while 1:
	url = 'http://suggestion.baidu.com/'
	print '---------------------------------PC-xiala'
	word = raw_input()
	keyword = word.decode('gbk').encode('utf-8')
	if word == 'over':
		sys.exit()
	payload = {'wd':'%s'%keyword}
	r = requests.get(url,params=payload)	
	kw = re.findall(r'"(.*?)"', r.content.replace(',',''))
	for k in kw:
		print k