# -*- coding: UTF-8 -*-
import re
import sys

r = 75
src = 'rem'
des = 'upx'
filename = 'index.css'
def main():
    f = open(filename, 'r')
    text = f.read()
    f.close()

    def rate(matched):
        value = float(matched.group('v')[:-len(src)])
        #print(str(value * r) + des)
        return str(value * r) + des

    text = re.sub('(?P<v>-*\d*\.*\d+?'+src+')', rate, text)

    f = open(filename+'.out', 'w')
    f.write(text)
    f.close()

if(len(sys.argv) != 5):
    print('usage: python css.py filename srcUnit rate desUnit')
    print('example: python css.py index.css rem 75 px')
else:
    filename = sys.argv[1]
    src = sys.argv[2]
    r = float(sys.argv[3])
    des = sys.argv[4]
    main()
