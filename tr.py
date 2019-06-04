import csv
import json
import sys
import codecs
def trans(path):
 jsonData = codecs.open(path, 'r', 'utf-8')
 # csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
 # csvfile = open(path+'.csv', 'wb') # python2下
 csvfile = open(path+'.csv', 'w', newline='') # python3下
 writer = csv.writer(csvfile, delimiter='\t')
 keys=['id', 'name', 'category', 'price', 'count', 'type', 'address', 'link', 'x', 'y']
 writer.writerow(keys)
 i = 1
 for dic in jsonData:
  dic = json.loads(dic[0:-1])
  x = dic['coordinates'][0]
  y = dic['coordinates'][1]
  writer.writerow([str(i),dic['name'],dic['category'],dic['price'],dic['count'],dic['type'],dic['address'],dic['link'],x,y])
  i += 1
 jsonData.close()
 csvfile.close()
if __name__ == '__main__':
 path = str("E:\\PycharmProjects\\UmenBigJSONTOCSV\\test.json")
 print (path)
 trans(path)