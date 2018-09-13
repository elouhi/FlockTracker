#!/usr/bin/env/ python3
import datetime, jsonpickle
class House:
	dateTimeDict ={}
	def __init__(self,farmName = None, houseNum = None, numBirds = None):
		self.farmName=farmName or None
		self.houseNum=houseNum or None	
		self.numBirds=numBirds or None
		self.hop1 = []
		self.hop2 = []

# 	def __repr__(self):
# 		return str(self.__dict__)

# 	def dateTimeRet(self):
# 		return self.dateTimeDict

# 	def serialize(self):
# 		return jsonpickle.encode(self)

	def connectTime(self):
		dict = self.__dict__
		dict["dateTimeDict"] = self.dateTimeDict
		return dict
# 	Day param is for testing
	def addFeed(self, amount, hopNum, day):
# 		localtime = time.localtime(time.time())
		localtime = datetime.datetime.now()
		if hopNum is 1: 
# 			self.hop1.append({'DateTime':localtime, 'Amount':amount})
			self.hop1.append({'DateTime':(datetime.datetime.now()-datetime.timedelta(days=day)).replace(minute=0, second=0, microsecond=0), 'Amount':amount})
# 				{'Date':{
# 				'Month': localtime.tm_mon, 'Day':localtime.tm_mday, 'Year': localtime.tm_year
# 			} , 'TimeHr':localtime.tm_hour, 'TimeM': localtime.tm_min, 'TimeS':localtime.tm_sec, 'Amount':amount})
			runningTotal = 0
			for v in self.hop1:
				runningTotal+=v['Amount']
				v['TotalAmount']=runningTotal
		elif hopNum is 2:
# 			self.hop2.append({'DateTime':localtime, 'Amount':amount})
			self.hop2.append({'DateTime':(datetime.datetime.now()-datetime.timedelta(days=day)).replace(minute=0, second=0, microsecond=0), 'Amount':amount})
			runningTotal = 0
			for v in self.hop2:
				runningTotal+=v['Amount']
				v['TotalAmount']=runningTotal
	def convertToHouse(self, m_House):
		self.dateTimeDict = {'TimeIn': datetime.datetime(m_House['dateTimeDict']['TimeIn']['Year'], 
														m_House['dateTimeDict']['TimeIn']['Month'], m_House['dateTimeDict']['TimeIn']['Day'],
														m_House['dateTimeDict']['TimeIn']['TimeHr']),
							 'TimeOut': datetime.datetime(m_House['dateTimeDict']['TimeOut']['Year'], 
														m_House['dateTimeDict']['TimeOut']['Month'], m_House['dateTimeDict']['TimeOut']['Day'],
														m_House['dateTimeDict']['TimeOut']['TimeHr'])
							}
		self.farmName = m_House['farmName']
		self.houseNum = m_House['houseNum']
		self.numBirds = m_House['numBirds']
		if m_House['hop1']:
			for d in m_House['hop1']:
				dict = {}
				for k, v in d.items():
					if k == 'DateTime':
						dict['DateTime'] = datetime.datetime(v['Year'], v['Month'], v['Day'], v['TimeHr']).replace(minute=0, second=0, microsecond=0)
					else:dict[k] = d[k]
				self.hop1.append(dict)
		if m_House['hop2']:
			for d in m_House.hop2:
				dict = {}
				for k, v in d.items():					
					if k == 'DateTime':
						dict['DateTime'] = datetime.datetime(k['Year'], k['Month'], k['Day'], k['TimeHr']).replace(minute=0, second=0, microsecond=0)
					else: dict[k] = d[k]
				self.hop2.append(dict)

		
# class House:
# 	def __init__(self):	
# 		self.hop1 = []
# 		self.hop2 = []
# 	dateTimeDict = {}
# 	def __repr__(self):
# 		return str(self.__dict__)

# 	def dateTimeRet(self):
# 		return self.dateTimeDict
# 	def serialize(self): 
# 		return jsonpickle.encode(self)
# 	def connectTime(self):
# 		dict = self.__dict__
# 		dict["dateTimeDict"] = self.dateTimeDict
# 		return dict		
# 	#day param is for testing
# 	def addFeed(self, amount, hopNum, day):
# # 		localtime = time.localtime(time.time())
# 		localtime = datetime.datetime.now()
# 		if hopNum is 1: 
# # 			self.hop1.append({'DateTime':localtime, 'Amount':amount})
# 			self.hop1.append({'DateTime':(datetime.datetime.now()-datetime.timedelta(days=day)).replace(minute=0, second=0, microsecond=0), 'Amount':amount})
# # 				{'Date':{
# # 				'Month': localtime.tm_mon, 'Day':localtime.tm_mday, 'Year': localtime.tm_year
# # 			} , 'TimeHr':localtime.tm_hour, 'TimeM': localtime.tm_min, 'TimeS':localtime.tm_sec, 'Amount':amount})
# 			runningTotal = 0
# 			for v in self.hop1:
# 				runningTotal+=v['Amount']
# 				v['TotalAmount']=runningTotal
	
# 		elif hopNum is 2:
# # 			self.hop2.append({'DateTime':localtime, 'Amount':amount})
# 			self.hop2.append({'DateTime':(datetime.datetime.now()-datetime.timedelta(days=day)).replace(minute=0, second=0, microsecond=0), 'Amount':amount})
# 			runningTotal = 0
# 			for v in self.hop2:
# 				runningTotal+=v['Amount']
# 				v['TotalAmount']=runningTotal

	
class MongoHouse:
	dateTimeDict ={}
	def __init__(self,farmName = None, houseNum = None, numBirds = None):
		self.farmName=farmName or None
		self.houseNum=houseNum or None	
		self.numBirds=numBirds or None
		self.hop1 = []
		self.hop2 = []

	def convertToMongo(self, house):
		self.dateTimeDict = {'TimeIn': {'Month': house.dateTimeDict['TimeIn'].month, 'Day':house.dateTimeDict['TimeIn'].day, 'Year': house.dateTimeDict['TimeIn'].year
			 , 'TimeHr':house.dateTimeDict['TimeIn'].hour},
							'TimeOut': {'Month': house.dateTimeDict['TimeOut'].month, 'Day':house.dateTimeDict['TimeOut'].day, 'Year': house.dateTimeDict['TimeOut'].year
			, 'TimeHr':house.dateTimeDict['TimeOut'].hour}
							}
		self.farmName = house.farmName
		self.houseNum = house.houseNum
		self.numBirds = house.numBirds
		if house.hop1:
			for d in house.hop1:
				dict = {}
				for k, v in d.items():					
					if k is 'DateTime':
						dict['DateTime'] = {'Month': v.month, 'Day': v.day, 'Year': v.year, 'TimeHr': v.hour}
					else:
						dict[k] = d[k]
				self.hop1.append(dict)
		if house.hop2:
			for d in house.hop2:
				dict = {}
				for k, v in d.items():					
					if k is 'DateTime':
						dict['DateTime'] = {'Month': v.month, 'Day': v.day, 'Year': v.year, 'TimeHr': v.hour}
					else:
						dict[k] = d[k]
				self.hop2.append(dict)
