#!/usr/bin/env/ python3
import models, os, sys, pprint, re, traceback, random, datetime

pp = pprint.PrettyPrinter(indent=4)
def houseInput(house):
    try:  
        house.houseNum = intValidation(input("Enter House Number: \n"))
        #Input time and date, due to the un-orderd nature of dictionaries in Python
        #IfElse statments were used to perform the input logic   
        for k, v in house.dateTimeDict.items():
            if k is "TimeIn":
                print(k)
                for key in v:
                    if key is "Time": v[key] = lenValidation(intValidation(input("Enter %s In in 'HHMM' integer format: \n" % key)), 4)
                    else: v[key] = lenValidation(intValidation(input("Enter %s In in two digit integer format: \n" % key)), 2)
            else:
                print(k)
                for key in v:
                    if key is "Time": v[key] =  lenValidation(intValidation(input("Enter %s Out in 'HHMM' integer format: \n" % key)), 4)
                    else: v[key] = lenValidation(intValidation(input("Enter %s Out in two digit integer format: \n" % key)), 2)           
#NEED TO PUT FLOATING POINT VALIDATION
        house.hop1 = float(input("Enter decimal value for number of pounds (lbs) of feed in Hopper 1: \n"))
        house.hop2 = float(input("Enter decimal value for number of pounds (lbs) of feed in Hopper 2: \n"))   
        house.numBirds = intValidation(input("Enter the number of birds for house #%d \n" % house.houseNum))              
    except ValueError as e:
        print("Error On input for houseInput().\n")
        print(e)
        print(traceback.format_exc())   
    return house

#Validates input for integers
def intValidation(x):    
    if re.match("^[a-z]*$", x):
        raise ValueError("No letters allowed.")
    else: return abs(int(x))
        
#Validates input for charachters a-z        
def charValidation(x):
    if not re.match("^[a-z]*$", x):
        raise ValueError("Only letters allowed.")
    else: return x

#Validates the input for a specific length 
def lenValidation(x, y):
    if len(str(x)) != y:
        raise ValueError("Input is not equal to %d digits." % y)
    else: return x

#Testing data
def testData(house):
    try:
        for i in range(3):
            house.addFeed(round(random.uniform(28000, 42000), 2), 1, 3-i)
    #         house.addFeed(round(random.uniform(3000, 10000), 2), 2)
        house.numBirds = random.randint(15000, 20000) 
        house.houseNum = 2
        house.dateTimeDict["TimeIn"] = datetime.datetime(2018, 9, 1, 8, 0, 0, 0).replace(minute=0, second=0, microsecond=0)
        house.dateTimeDict["TimeOut"]= datetime.datetime.now().replace(minute=0, second=0, microsecond=0)  
    except:
        raise 
    return house