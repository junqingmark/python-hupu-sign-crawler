# -*- coding: utf-8 -*-

import urllib

import re



def getHtml(url):

	page = urllib.urlopen(url)
	html = page.read()
	return html



def getSign(html):

	reg = r'<div class="sign"><hr class="hr2" size="1" />(.+?)</div>'

	#reg = r'uname="(.+?)"'

	signre = re.compile(reg)

	signlist = re.findall(signre, html)

	signlistNocopy = set(signlist)

	for signurl in signlistNocopy:

		if signurl.find('QQ') != -1 or signurl.find(u'代购') != -1:
			continue
		else:
			print(signurl)



for i in range(2, 41):

	html = getHtml("http://bbs.hupu.com/18039279-" + str(i) + ".html")

	getSign(html.decode("gbk","ignore"))



#print (html.decode("gbk","ignore"))

