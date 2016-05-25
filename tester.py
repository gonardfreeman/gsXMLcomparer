# coding: utf-8
from lxml import etree
from StringIO import StringIO

estimateTypes = {'ssr':'{2B0470FD-477C-4359-9F34-EEBE36B7D346}',
	'objSmeta':'{2B0470FD-477C-4359-9F34-EEBE36B7D345}',
	'locSmeta':'{2B0470FD-477C-4359-9F34-EEBE36B7D340}'}
class Parser(object):
	def __init__(self, fileName, allTypes={}):
		self.fileName = fileName
		self.allTypes = {}

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
		

def choser(self):
	pass


a = Choser('01-01.xml')
a.docType('01-01.xml')
a.choser()
