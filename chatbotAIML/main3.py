import aiml
import os
import csv
import json
from janome.tokenizer import Tokenizer

t = Tokenizer("userdic.csv", udic_enc="utf8")

f = open('wolftest.json', 'r')

jsonData = json.load(f)

j_change = json.dumps(jsonData, sort_keys = True, indent = 4, ensure_ascii=False)

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel準備OK
while True:
    message = jsonData["text"]["@value"]
    message = " ".join(t.tokenize(message, wakati=True))

    if message == "quit":

        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print(bot_response.replace(" ",""))
        f.close()
        break
