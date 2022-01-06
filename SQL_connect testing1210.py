import pymysql 

#python連線到MySQL
connect = pymysql.connect(
host = "34.134.228.74", #網域名,資料庫連線上沒有http,http是給網路連線用的
user = "'sam",
passwd = "rootroot",

charset = "utf8", #不能有-
port = 3306 , #預設端口是3306
)

cur = connect.cursor() #操作變數>開始

print('Success') 

connect.close() #連線關閉