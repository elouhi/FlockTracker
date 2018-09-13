#!/usr/bin/env/ python3
import math, os, datetime, sys
#All of the independent functions in another function need to be run at the time of calling 
#dependent function for accurate estimates. Each function assumes one hopper per house

#Rate of Ingestion
#455 Lb's of feed are eaten per thousand birds per 24 hours
rOI = 455/24 #Rate of feed eaten per thousand birds per hour

#Feed Rate of Ingestion
#Returns the amount of feed in Lb's per (numBirds)/1000 per hour
def calc_F_ROI(numBirds):
    return (numBirds/1000)*rOI

#Total Feed Remaining
#Returns the "TotalAmount" of feed remaining in hopper at the time the function is called
#Param: Hop dict (DateTime, Amount) (List[-1)
def calc_TotalF_Rem(hop, F_ROI):
    diffDate = (datetime.datetime.now() - (hop[0]['DateTime']))
    diffHours = diffDate.days * 24 + diffDate.seconds // 3600
    print("First Hop datetime: ",  hop[0]['DateTime'])
    print("diffDate: ", diffDate)
    print("diffHours: ",diffHours)
    return hop[-1]['TotalAmount'] - (diffHours * F_ROI)

#Hours Since most recent feedAdd
def calc_H_Since_Last(hop):
    diffDate = (datetime.datetime.now()) - (hop[-1]['DateTime'])
    diffHours = diffDate.days * 24 + diffDate.seconds // 3600
    print("Last Hop datetime: ",  hop[-1]['DateTime'])
    print("diffDate: ", diffDate)
    print("diffHours: ",diffHours)
    return diffHours

#Time Till Empty
#Returns the hours left until hopper is empty
def calc_TTE(F_Rem, F_ROI):
    return (F_Rem/F_ROI)

#Estimated Empty Date/Time
#Returns the estimated date and time the hopper will be empty based on last date/time the hopper
#was filled (last inedx of hop#[]). 
def calc_E_EDT(TTE):
    return datetime.timedelta(hours=TTE) + datetime.datetime.now()

#Hours Out Difference
#Returns a + or - value for the number of hours difference (over or under) between
#the scheduled time the flock is going out, and the estimated date/time the hopper
#will be empty (E_EDT)
#+ means the hopper will have left over feed in it at the time of flock extraction
#- means hopper will not have enough food to make it to extraction date/time
def calc_hr_OD(dateTimeOut, E_EDT):    
    return E_EDT - dateTimeOut["TimeOut"]

#Estimated Feed Return
#Amount of feed left in bin by flock extraction date/time based on number of hours (+/-) left
#and F_ROI. If number is positive, then that amount in Lb's needs to be ordered to have a 
#Zero feed return. If negative then that is going to be the amount of feed in Lb'sleft over
#after flock extraction 
def calc_E_FRet(hr_OD, F_ROI):
    return (hr_OD.days * 24 + hr_OD.seconds // 3600) * F_ROI




