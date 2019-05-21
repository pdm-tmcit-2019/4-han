
import sys
import re
from janome.tokenizer import Tokenizer


t = Tokenizer("chatbotAIML/userdic.csv", udic_enc="utf8")

args = sys.argv

filename =  args[1]

fi = open(filename , 'r',  encoding='utf8')
fo = open(filename + ".aiml" , 'w',  encoding='utf8')

line = fi.readline()

while line:
	m = re.search("\<pattern\>.*\<\/pattern\>",line)
	if m != None:
		str = m.group(0).replace("\<pattern\>","").replace("\<\/pattern\>","")
		rstr = " ".join(t.tokenize(str, wakati=True))
		fo.write(line.replace(str,rstr))
	else:
		fo.write(line)
	line = fi.readline()

fi.close()
