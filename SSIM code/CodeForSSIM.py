import json
f = open("raw.txt")
df = f.readlines()
lst = list()
dic ={}
for lines in df :
    if(lines.startswith('1')):
        RecType=lines[0:1]
        TitleOfContnts=lines[1:35]
        SerialNum=lines[194:200]
        dic  = {'RecType':RecType, 'TitleOfContnts':TitleOfContnts, 'SerialNum':SerialNum}
        val = (TitleOfContnts, SerialNum)
        lst.append(val)
        sons = json.dumps(dic, indent=6)
        print(sons)
        with open("ffile.json",'a') as k:
            k.write(sons)
    elif(lines.startswith('2')):
        RecType=lines[0:1]
        TimeMode=lines[1:2]
        Airline=lines[2:5]
        ValidityPeriod=lines[14:28]
        CreationDate=lines[28:35]
        TitleOfData=lines[35:52]
        SellDate=lines[64:71]
        ScheduleStatus=lines[71:72]
        CreatorRef=lines[72:75]
        ENET=lines[188:190]
        CreationTime=lines[190:194]
        SerialNum=lines[194:200]
        dic  = {'RecType':RecType, 'TimeMode':TimeMode, 'Airline':Airline, 'ValidityPeriod':ValidityPeriod, 'CreationDate':CreationDate, 
                'TitleOfData':TitleOfData,'ScheduleStatus':ScheduleStatus, 'SellDate':SellDate, 'CreatorRef':CreatorRef, 'EN/ET':ENET, 
                'CreationTime':CreationTime, 'SerialNum':SerialNum}
        val = (RecType, TimeMode, Airline, ValidityPeriod, CreationDate, TitleOfData, ScheduleStatus, SellDate, CreatorRef, ENET)
        lst.append(val)
        sons = json.dumps(dic, indent=6)
        print(sons)
        with open("ffile.json",'a') as k:
            k.write(sons)
    elif(lines.startswith('3')):
        RecType=3
        FltNum=lines[5:9]
        itnV=lines[9:11]
        legN=lines[11:13]
        ItStDate=lines[14:21]
        ItEndDate=lines[21:28]
        sdep=lines[36:39]
        sarr = lines[54:57]
        SerialNum=lines[192:200]
        dic  = {'RecType':'3', 'FltNum':FltNum, 'itnV':itnV, 'legN':legN, 'ItStDate':ItStDate, 'ItEndDate':ItEndDate, 'sdep':sdep, 'sarr':sarr, 'SerialNum':SerialNum}
        val = (FltNum, itnV, legN, ItStDate, ItEndDate, sdep, sarr, SerialNum)
        lst.append(val)
        sons = json.dumps(dic, indent=6)
        print(sons)
        with open("mainFile2.json",'a') as k:
            k.write(sons)
        continue

    elif(lines.startswith('4')):
        RecType=4
        BpI=lines[28:29]
        OpI=lines[29:30]
        DataElemIdentif=lines[30:33]
        BoardPt=lines[33:36]
        OffPt=lines[36:39]
        SerialNum=lines[193:200]
        dic  = {'RecType':'4', 'BpI':BpI, 'OpI':OpI, 'DataElemIdentif':DataElemIdentif, 'BoardPt':BoardPt, 'OffPt':OffPt, 'SerialNum':SerialNum}
        val = (BpI, OpI, DataElemIdentif, BoardPt, OffPt, SerialNum)
        lst.append(val)
        sons = json.dumps(dic, indent=6)
        print(sons)
        with open("mainFile2.json",'a') as k:
            k.write(sons)
    elif(lines.startswith('5')):
        RecType=lines[0:1]
        SerialNumRef=lines[187:193]
        EndCode=lines[193:194]
        SerialNum=lines[194:200]
        dic  = {'RecType':RecType, 'SerialNumRef':SerialNumRef, 'EndCode':EndCode, 'SerialNum':SerialNum}
        val = (RecType, SerialNumRef, EndCode, SerialNum)
        lst.append(val)
        sons = json.dumps(dic, indent=6)
        print(sons)
        with open("ffile.json",'a') as k:
            k.write(sons)