# coding: utf-8
from lxml import etree

tree = etree.parse('01-02.xml')
r = tree.xpath('//Chapters/Chapter/Summary')
z = {}
for i in r:
	z[i.get('Caption').encode('utf8')] = i.get('Total')
for i in z.keys():
	if i == 'Итого с учетом "Локальные сметные расчеты"':
		print z[i]
