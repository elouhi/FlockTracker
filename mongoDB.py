#!/usr/bin/env/ python3
import pymongo, models, os, sys, pprint
# --smallfiles
# mongod --dbpath /home/cabox/workspace/Chicken_Feed --fork --logpath /home/cabox/workspace/Chicken_Feed/monGodb/mongoLog.log --nojou
#import subprocess

#C:\Program Files\MongoDB\Server\4.0\bin 
# subprocess.call(['./test.sh']) # Thanks @Jim Dennis for suggesting the []

def setCol(x):
	collection = db[x]
	return collection

def post(x):	
	result = db.collection.insert_one(x)
	print(result + "\n")
	
def getOne(x):
	doc = db.collection.find_one({'farmName': x})
	print(doc)
	return doc

def getAll(x):
	docs = db.collection.find({'farmName': x})
	print(docs)
	return docs

def printCollection(x):
	cursor = collection.find({})
	for document in cursor: pprint(document)
		
