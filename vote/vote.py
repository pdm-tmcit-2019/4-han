import json
import codecs
import random

list3 = [[0 for i in range(7)] for j in range(15)]
f = open( "noon.jsonld", "r", encoding="utf-8")
f2 = open( "noonVote.jsonld", "r", encoding="utf-8")

json_data  = json.load(f)
json_data2 = json.load(f2)
ans = [0 for i in range(7)]

for i in range(15):
   isMine = json_data['character'][i]['isMine']
   if isMine == True:
       continue
   list3[i][0] = isMine
   status = json_data['character'][i]['status']
   if status != 'alive':
       continue
   list3[i][1] = status
   id1 = json_data['character'][i]['@id']
   list3[i][2] = id1
   id2 = json_data['character'][i]['id']
   list3[i][3] = id2
   en = json_data['character'][i]['name']['en']
   list3[i][4] = en
   ja = json_data['character'][i]['name']['ja']
   list3[i][5] = ja
   image = json_data['character'][i]['image']
   list3[i][6] = image

print("list3 = {0}".format(list3))

while ans[1] != 'alive':
    ans = random.choice(list3)

f.close()

json_data2['character']['@id'] = ans[2]
json_data2['character']['id'] = ans[3]
json_data2['character']['name']['en'] = ans[4]
json_data2['character']['name']['ja'] = ans[5]
json_data2['character']['image'] = ans[6]

with open('answer.jsonld', 'w', encoding="utf-8") as f2:
    json.dump(json_data2, f2, ensure_ascii=False, indent=4)

f2.close()
