import aiml
import os
import csv
from janome.tokenizer import Tokenizer

t = Tokenizer("userdic.csv", udic_enc="utf8")

count = 0
with open('village_g18.csv', encoding="utf-8")as f:
    for line in f:
        count += 1

with open('village_g18.csv', encoding="utf-8")as f:
    reader = csv.reader(f)
    l = [row for row in reader]

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel準備OK
while True:
    message = l[count - 2][3]
    message = " ".join(t.tokenize(message, wakati=True))

    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print(bot_response.replace(" ",""))
        break
