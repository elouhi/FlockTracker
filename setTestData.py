#!/usr/bin/env/ python3
import chickenExcel, models, inputLogic, mongoDB
import openpyxl, os, sys, pprint, datetime, json, traceback, pymongo
# perl -i.bak -pe "s/\t/' 'x(4-pos()%4)/eg" file.py "Removes tab/indent errors"
# setTestData.py: Creates a test db and collection and fills it with data
def main():
    #Checks to see if openpyxl is installed
    try:
        import openpyxl
    except ImportError as iE:
        print("Python Excel module 'openpyxl' not found")
        sys.exit(1) 
        
    pp = pprint.PrettyPrinter(indent=4)
    wb = openpyxl.Workbook()
    fileName = input("Name File: \n")
    ws = wb.active
    ws.title = input("Enter Name of First Farm:\n")   
    numOfHouses = inputLogic.intValidation(input("Enter Number of Houses on Farm: \n"))   
    #Creates mongo DB
    client = pymongo.MongoClient()
    db = client.chicken_db_test
    collection = db[str(ws.title)]
    #Lists for storing house OBJ and Dict
    houses = []
    houseObjs = [] #List for the House objects in OOP form
    try:    
        if numOfHouses is None: sys.exit(0)#Testing
        for i in range(int(numOfHouses)): 
#             houses.append(inputLogic.houseInput(house))
#             print(houses[i].dateTimeRet(), sep="\n")
#             houses.append(inputLogic.testData(house))
            house = models.House() 
            house.farmName = str(ws.title)
            house = inputLogic.testData(house)
            houseObjs.append(house) #Adds house obj to list
            print("Pre-mongo format: \n")
            houseDict = house.connectTime()
            pp.pprint(houseDict)
#             houses.append(houseDict)#Adds houseDict object to list for DB insertion
#             pp.pprint(db.collection.find_one({'farmName': house.farmName}))

# Converts House model to Mongo Model
            print("Mongo House Model: \n")
            m_House = models.MongoHouse()
            m_House.convertToMongo(house)
            houses.append(m_House.__dict__)
            pp.pprint(m_House.__dict__)
            
#         print("Post mongo format: \n")
        db.collection.ensure_index('farmName')
        db.collection.create_index([('dateTimeDict.TimeIn', 1),  ('dateTimeDict.TimeOut', 1)])
        db.collection.insert_many(houses)

    except Exception as e:
        print("Unexpected error: \n")
        print(e)
        print(traceback.format_exc())   
        raise
        
#     #Adds objects headers to .xlsx Worksheet
#     header = []
#     for k, v in vars(house).items():
#         header.append(k)    
#         ws.append(header)
        
#     pp.pprint(tuple(ws.rows))
#     chickenExcel.printWSTerminal(wb)
    #for row in new_data: ws.append(row)
    #print(models.objToDict(houseOne)+"\n")
    # chickenExcel.saveNewName(fileName, wb)
    # chickenExcel.printWSTerminal(wb)
# if __name__=="__main__":
main()