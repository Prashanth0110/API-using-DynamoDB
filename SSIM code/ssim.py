import re
import json
a=0
f = open("C:/Users/jayan/OneDrive/Desktop/Prashanth/ssim/raw.txt",'r')
lines = f.readlines()
print("Hi Lets Start")
for line in lines:
    patt=re.compile(r"^3")
    matches = patt.finditer(line)
    for match in matches:
        a=a+1
        Act="1"
        occ="0"
        seat = line[172:182]
        name = line[2:4]
        fltnbr = line[5:9]
        intV1 = line[9:11]
        legnum1 = line[11:13]
        sdep = line[36:39]
        sarr = line[54:57]
        depTh =line[43:45]
        depTm =line[45:47]
        arrTh = line[57:59]
        arrTm = line[59:61]
        depD = line[14:21]
        arrD = line[21:28]
        dictionary = {
        "FlightLegKey":{"S": name+"::"+fltnbr+"::"+Act+"::"+depD},"docType":{"S":"OpsFltLeg"+"::"+sdep+"::"+Act+"::"+sarr+"::"+occ+"::"+occ},"ActiveInd":{"S":Act},"CarrIataCd":{"S": name},"FlightNumber":{"S": fltnbr},"intVarNum":{"S": intV1},"LegNum":{"S": legnum1},
        "Departure":{"S": sdep},"Arrival":{"S": sarr},"DepTime":{"S": depTh+":"+depTm},"ArrTime":{"S": arrTh+":"+arrTm},
        "DepDate":{"S": depD},"ArrDate":{"S": arrD},"DepGate":{"S":"HOLD"},"ArrGate":{"S":"HOLD"},"LclDepDtm": {"S": depD+"T"+depTh+":"+depTm},"LclArrDtm": {"S": arrD+"T"+arrTh+":"+arrTm},"origOccurNbr": {"S": occ},"SeatConfig": {"S": seat}
        }
        
        data={"FlightLegKey":{"S": name+"::"+fltnbr+"::"+Act+"::"+depD},"docType":{"S":"SchedFltLeg"+"::"+sdep+"::"+sarr+"::"+Act},"ActiveInd":{"S":Act},"CarrIataCd":{"S": name},"FlightNumber":{"S": fltnbr},"intVarNum":{"S": intV1},"LegNumm":{"S": legnum1},
        "Departure":{"S": sdep},"Arrival":{"S": sarr},"DepTime":{"S": depTh+":"+depTm},"ArrTime":{"S": arrTh+":"+arrTm},
        "DepDate":{"S": depD},"ArrDate":{"S": arrD},"DepGate":{"S":"HOLD"},"ArrGate":{"S":"HOLD"},"LclDepDtm": {"S": depD+"T"+depTh+":"+depTm},"LclArrDtm": {"S": arrD+"T"+arrTh+":"+arrTm},"origOccurNbr": {"S": occ},"SeatConfig": {"S": seat}}
        
        with open("C:/Users/jayan/OneDrive/Desktop/Prashanth/ssim/file7.json",'a') as k:
            json.dump(dictionary,k,indent=3)
            k.write(",")
            json.dump(data,k,indent=3)
            k.write(",")
        if(a<20):
            print("Processing")
        if(1980<a<2000):
            print(" Still Processing")
               

print("Completed")
            
        