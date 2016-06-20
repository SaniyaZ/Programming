# -*- coding: utf-8 -*-

import re
import lxml.html
import lxml.etree
import codecs

# открываем файл books.xml и записываем его содержимое в переменную some_xml
f = codecs.open('books.xml')
some_xml = f.read().decode('utf-8')
f.close()

# строим дерево с помощью метода fromstring, дальше с помощью xpath находим
# все теги book, вложенные в тег catalog
tree = lxml.etree.fromstring(some_xml)
results = tree.xpath('/catalog/book')

# results -- это массив. печатая его длину. мы узнаём, сколько тегов book нашлось
print len(results)

# находим все теги name, вложенные в теги book, которые вложены в тег catalog
names = tree.xpath('/catalog/book/title')

# для каждого тега распечатываем текст, лежащий внутри него
for el in names:
    print el.text

# а вот так можно доставать значение атрибута
print u'\n-------------\n'
ids = tree.xpath('/catalog/book[@id]')
for i in ids:
    print i.get(u'id')
