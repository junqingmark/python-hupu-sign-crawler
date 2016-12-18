# -*- coding: utf-8 -*-

import urllib

import re



def getHtml(url):

	page = urllib.urlopen(url)
	html = page.read()
	return html



def getSignInPage(html):

	reg = r'<div class="sign"><hr class="hr2" size="1" />(.+?)</div>'

	#reg = r'uname="(.+?)"'

	signre = re.compile(reg)

	signlist = re.findall(signre, html)

	signlistNocopy = set(signlist)

	for signurl in signlistNocopy:

		if signurl.find('QQ') != -1 or signurl.find(u'代购') != -1 or signurl.find(u'微信') != -1 or signurl.find(u'篮球') != -1:
			continue
		else:
			print(signurl)

def getLinkInPage(html):
	reg = r'a id="" href="(.+?)"'
	signre = re.compile(reg)
	signlist = re.findall(signre, html)
	for signurl in signlist:
		HTML = getHtml("http://bbs.hupu.com" + signurl)
		getSignInPage(HTML.decode("gbk","ignore"))
		#print(signurl)

for i in range(1, 11):

	#html = getHtml("http://bbs.hupu.com/18039279-" + str(i) + ".html")
	if i == 1:
		html = getHtml("http://bbs.hupu.com/bxj")
	else:
		print("====This is page " + str(i) + "====")
		html = getHtml("http://bbs.hupu.com/bxj-" + str(i))
	
	getLinkInPage(html)



#print (html.decode("gbk","ignore"))

