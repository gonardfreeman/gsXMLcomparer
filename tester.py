# coding: utf-8
# -*- mode: python -*-
from lxml import etree
import os

class Parser(object):
	def __init__(self, fileName, allTypes={}):
		self.fileName = fileName
		self.allTypes = {}
		self.estimateTypes = {'ssr':'{2B0470FD-477C-4359-9F34-EEBE36B7D346}',
		'objSmeta':'{2B0470FD-477C-4359-9F34-EEBE36B7D345}',
		'locSmeta':'{2B0470FD-477C-4359-9F34-EEBE36B7D340}'}

	def parser(self):
		tree = etree.parse(self.fileName)
		return tree

	
		
class Choser(Parser):
	def docType(self, name):	
		r = self.parser().xpath('//Document')
		for i in r:
			self.allTypes[name] = i.get('DocumentType')
		
	def obj(self):
		r = self.parser().xpath('//Chapters/Chapter/Summary')
		z = {}
		for i in r:
			z[i.get('Caption').encode('utf8')] = i.get('Total')
		for i in z.keys():
			if i == 'Итого с учетом "Локальные сметные расчеты"':
				print z[i]

	def choser(self, fName):
		if self.estimateTypes['objSmeta'] == self.allTypes[fName]:
			self.obj()

if __name__ == '__main__':
	dirName = raw_input('Enter dir name: ')
	ROOT_PATH=os.path.dirname(__file__)
	for filename in os.listdir(ROOT_PATH+'\\'+dirName):
		if not filename.endswith('.xml'): continue
		fullname = os.path.join(ROOT_PATH+'\\'+dirName, filename)
		a = Choser(fullname)
		a.docType(fullname)
		a.choser(fullname)
		