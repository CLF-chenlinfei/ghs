import re

def load_cookies():
	cookie_json = {}
	try:
		with open('cookie.txt','r',encoding = 'utf-8') as cookies_file:
			cookie = cookies_file.read().replace(" ", "")
			for i in re.findall(r".*?=.*?;", cookie):
				rl = re.match(r'(.*?)=(.*?);', i)
				cookie_json[rl.group(1)] = rl.group(2)
	except:
		return False
		# print('cookies读取失败')
	else:
		return cookie_json

load_cookies()