# -*- coding: utf-8 -*-
from params_ import *


def save_file(topsites):
    with open("out.txt", "w", encoding="utf-8") as f:
        for site in topsites:
            f.write(u'\nВыравнивание по размеру текста %s:\n\n' % (site.name))
            top = site.get_top()
            for i in range(len(top[0])):
                try:
                    f.write(u'%d) %s - %s\n' % (i + 1, top[0][i].text, top[1][i].text))
                except AttributeError:
                    f.write(u'%d) %s - Неизвестный автор\n' % (i + 1,top[0][i].text))

livelib = LiveLib('post1950_big80+.xls')
readrate = ReadRate('post1950_big90+.xls')
libs = Libs('post1950_verybig100+.xls')
libs = Libs('source_post1950_wordcount.xls')

save_file([livelib, readrate, libs])
