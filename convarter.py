
import sys
import re
from janome.tokenizer import Tokenizer


if len(sys.argv) < 3:
	print('useage: python converter.py [input file] [output file]')
	exit()

t = Tokenizer("chatbotAIML/userdic.csv", udic_enc="utf8")

args = sys.argv

filename_i =  args[1]
filename_o =  args[2]


fi = open(filename_i , 'r',  encoding='utf8')
fo = open(filename_o , 'w',  encoding='utf8')

line = fi.readline()

while line:
	m = re.search("\<pattern\>.*\<\/pattern\>",line)
	if m != None:
		str = m.group(0).replace("<pattern>","").replace("</pattern>","")

		rstr = " ".join(t.tokenize(str, wakati=True))
		fo.write(line.replace(str,rstr))
	else:
		fo.write(line)
	line = fi.readline()

fi.close()
