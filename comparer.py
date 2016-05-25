# coding: utf-8
from lxml import etree
import os

class Parser(object):
	def __init__(self):
		pass

dirName = raw_input('Enter dir name: ')
ROOT_PATH=os.path.dirname(__file__)
for filename in os.listdir(ROOT_PATH+'\\'+dirName):
	if not filename.endswith('.xml'): continue
	fullname = os.path.join(ROOT_PATH+'\\'+dirName, filename)
	tree = etree.parse(fullname)
	r = tree.xpath('//Chapters/Chapter/Summary')
	z = {}
	for i in r:
		z[i.get('Caption').encode('utf8')] = i.get('Total')
	for i in z.keys():
		if i == 'Итого с учетом "Локальные сметные расчеты"':
			print z[i]