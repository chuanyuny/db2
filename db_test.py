#-*- coding:utf-8 -*-
'''使用python连接数据库,把数据库中的内容输出到txt文档中'''
from pymysql import cursors,connect
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
def write_txt(content):
	fo=open('read.txt','a+')
	fo.writelines(content)
	fo.close()

#连接数据库
conn=connect(host='127.0.0.1',user='root',password='123456',db='guest',charset='utf8mb4',cursorclass=cursors.DictCursor)

try:
	with conn.cursor() as cursor:
		sql="SELECT id,name,status,address,start_time,has_not_signed,has_signed,jiabin_sum FROM sign_event"
		cursor.execute(sql)
		result=cursor.fetchall()

		for each in result:
			list1=[]
			list1.append(str(each['id']))
			list1.append(each['name'].encode('utf-8'))
			if str(each['status'])=='1':
				list1.append('True')
			else:
				list1.append('False')
			# list1.append(str(each['status']))
			list1.append(each['address'].encode('utf-8'))
			list1.append(str(each['start_time']))
			list1.append('sign')
			list1.append(str(each['jiabin_sum']))
			list1.append(str(each['has_signed']))
			list1.append(str(each['has_not_signed']))
			# print list1
			str1=" ".join(list1)
			write_txt(str1)
			write_txt('\n')
finally:
	conn.close()
 




