#!/usr/bin/env/ python3
import chickenExcel, models, inputLogic, mongoDB, algorithms, chickenGUI
import openpyxl, os, sys, pprint, datetime, json, traceback, pymongo, tkinter
#print(os.path.dirname(os.path.abspath(__file__))+"/"+fileName)
# Main application 
def main():
    #Checks to see if openpyxl is installed
    try:
        import openpyxl
    except ImportError as iE:
        print("Python Excel module 'openpyxl' not found")
        sys.exit(1)
    
#     PPrint is used for interal testing output formatting
    pp = pprint.PrettyPrinter(indent=4)
#     wb = openpyxl.Workbook()
#     fileName = input("Name File: \n")
#     ws = wb.active
#     numOfHouses = inputLogic.intValidation(input("Enter Number of Houses on Farm: \n"))   
    #Connects to a mongo DB
    client = pymongo.MongoClient()
    db = client.chicken_db_test
    farmName =str(input("Enter Name of Farm:\n") )
    collection = db[farmName]

    houseObjs = [] #List for the House objects in OOP form
    try: 
        house = models.House() 
    
        print("Post mongo format: \n")
        cursor = db.collection.find({"farmName":farmName})
        for key in cursor:
            house.convertToHouse(key)
            houseObjs.append(house) #Adds house obj to list
            pp.pprint(house.__dict__)
            
            print("NumBirds: {0} \n".format(house.numBirds))
            F_ROI = algorithms.calc_F_ROI(house.numBirds)
            print("Last Fill of Hop1: {} ".format(house.hop1[-1]))
#             print(key["hop2"][-1])
            h1_F_Rem=algorithms.calc_TotalF_Rem((house.hop1), F_ROI)
#             h2_F_Rem=algorithms.calc_F_Rem((key ["hop2"]), F_ROI)
            print("Feed Rate of Ingestion: {0:.2f} Lb's/hr \n".format(F_ROI))
            print("Estimated Feed Remaining in Hop 1 after last fill: {0:.2f} Lb's \n".format(h1_F_Rem))
#             print("Feed Remaining in Hop 2: {0:.2f} Lb's \n".format(h2_F_Rem, F_ROI))
            TTE_h1=algorithms.calc_TTE(h1_F_Rem, F_ROI)
            print("Time Till Hop1 is empty: {0:.2f} Hr's".format(TTE_h1))
            E_EDT_h1=algorithms.calc_E_EDT(TTE_h1)
            print("Estimated date Hop1 will be empty: {0}".format(E_EDT_h1))
            hr_OD= algorithms.calc_hr_OD(house.dateTimeDict, E_EDT_h1)
            print("Number of hours over, or under extraction date/time: {}".format(hr_OD))
            E_FRet = algorithms.calc_E_FRet(hr_OD, F_ROI)
            print("Amount of feed left by flock extraction: {0:.3f} Lb's".format(E_FRet))
            

    except Exception as e:
        print("Unexpected error: \n")
        print(e)
        print(traceback.format_exc())   
        raise
main()
