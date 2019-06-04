#-*-coding:utf-8-*-
import csv
import json
import sys
import codecs
import os
import csv
import json



#tips = input("输入json文件解压后所在路径(如C:\\Umen\\error_rate\\)，回车运行:")

error_json_folder  = input("输入json文件解压后所在路径(如C:\\Umen\\error_rate)，回车运行:")
if error_json_folder[-1:]!='\\':
    error_json_folder+='\\'
path = os.listdir(error_json_folder)

csvfile = open('result.csv', 'w', newline='')  # python3下
writer = csv.writer(csvfile, delimiter=',')

keys = ['app', 'date', 'all_ver_rate', 'ver_1', 'ver_1_rate', 'ver_2', 'ver_2_rate', 'ver_3', 'ver_3_rate']
writer.writerow(keys)


for app in path:
    if app[-3:]== "txt" or app[-3:]== "TXT" or app[-3:]== "json" or app[-3:]== "JSON":
        fullpath = error_json_folder + app
        appname = app[:-4]
        # 非标准json，所以加头加尾，来框起来
        with open(fullpath,'r+') as fs:
            content = fs.read()
            fs.seek(0,0)
            if(content[0]!='['):
                 fs.write('['+content+']')
        print("Now csv is: "+  fullpath)

        jsonData = open(fullpath, 'r').read()

        dic = json.loads(jsonData)

        for singleline in dic:
            writer.writerow([appname, singleline['date'], singleline['all_ver_rate'], singleline['ver_1'], singleline['ver_1_rate'], singleline['ver_2'], singleline['ver_2_rate'],
                       singleline['ver_3'],singleline['ver_3_rate']])











    # x = json.loads("E:\\PycharmProjects\\UmenBigJSONTOCSV\\error_rate\\一起学网校Android.txt",strict=False)
    # f = csv.writer(open("test.csv", "wb+"))
    # # # Write CSV Header, If you dont need that, remove this line
    # f.writerow(["app","pk", "model", "codename", "name", "content_type"])
    # # for x in x:
    # #     f.writerow([appname,
    # #                 x["pk"],
    # #                 x["model"],
    # #                 x["fields"]["codename"],
    # #                 x["fields"]["name"],
    # #                 x["fields"]["content_type"]])
    #
    #
    #
    #
    #         # now_pic = str(files[i])
    #         # app_name = now_pic[:-4]
    #         #print(now_pic[:-4])
    #
    # # path=str(sys.argv[1]) # 获取path参数
    # # print (path)
    # # trans(path)