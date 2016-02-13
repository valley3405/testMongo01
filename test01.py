#!/usr/bin/python
#encoding:utf-8

import pymongo

#连接数据库实例
conn = pymongo.MongoClient('localhost', 27017)

#打开数据库
db = conn.test1

#打开数据表/聚集/collection
account = db.account

#向表/collection/聚集中插入数据
account.insert({"name": "mike", "active_time": "20130408"})

#更新记录
account.update({"name": "mike"}, {"$set": {"active_time": "20130408120000"}})

#查看一条记录
account.find_one()

#查看聚集的所有key
account.find_one().keys()

#查看记录总数
account.find().count()

#打印所有记录
for i in account.find():
	print i

#打印特定记录
for i in account.find({'name':'mike'}):
	print i


#获取聚集列表
db.collection_names()


