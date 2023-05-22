#   first version of it (text conversion) without using dataframes,
def round1():
    f1=open("combrou.txt","r")
    print("=============WELCOME==============")
    print(" hi there, this is a combined program involving all the 4 rounds and hereby specify the given cutoff range for given rounds: ")
    A=f1.readlines()
    d=[]
    c=[]
    couns=[]
    dic={'1': 'CEG', '2': 'ACT', '4': 'MIT', '1112': 'RMD', '1113': 'RMK', '1114': 'SA', '1116': 'SRI VENKATESHWARA', '1120': 'VELAMMAL', '1140': 'JPR', '1211': 'REC', '1216': 'SAVEET', '1219': 'VENKATESH', '1225': 'LOYOLLA', '1304': 'SRM', '1306': 'jpr', '1309': 'meenak_sundar', '1315': 'SSN', 'SAI RAM': 'SAI RAM', '1324': 'SAI RAM', '1413': 'VENKATESH.TECH', '1414': 'PRINCE', '1419': 'sai ram', '1422': 'SRM.VALLI', '1432': 'RIT', '1210': 'PANIMALAR'}
    print(dic)
    for i in A:
        j=i.split()
        d.append(j)
    for mn in d:
        if len(mn)>10:
            c.append(mn)
    def disp(x):
        print(x[0],x[1],x[-6],x[-5],x[-4],dic.get(x[-3]),x[-2],x[-1])
        pass
    lena=[]
    print("----------welcome-----------")
    i1=input("input enter commounity: ")
    cou=[]
    print(" select course! you can choose any number of courses that you'd like to enter, type end if it is completed :) ")
    while True:
        inp=input("enter course : ")
        if inp=="end":
            break
        else:
            cou.append(inp)
    if inp=="end":
        print("  1: any college is fine ")
        print("  2: only selected college and will enter using counselling code ")
        i2=int(input("enter your choice : "))
        if i2==1:
            print(" option 1 confirmed!! ")
            print(" 1: only a particular cutoff ")
            print(" 2: range wise selection e.g (185-197) ")
            ch=int(input("enter your choice : "))
            if ch==1:
                i21=float(input("enter cutoff: "))
                for x in c:
                    if float(x[-6])==i21 and x[-4]==i1:
                        if x[-2] in cou:
                            disp(x)
                            lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
            if ch==2:
                l1=float(input("enter starting limit of your cutoff range : "))
                l2=float(input("enter ending limit of your cutoff range : "))
                for x in c:
                    te=float(x[-6])
                    if l1<=te and te<=l2:
                        if (x[-4]==i1) and (x[-2] in cou):
                            disp(x)
                            lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
        if i2==2:
            print(" option 2 confirmed!! ")
            while True:
                inp=input("enter counselling code : ")
                if inp=="end":
                    break
                else:
                    couns.append(inp)
            print(" 1: only a particular cutoff ")
            print(" 2: range wise selection e.g (185-197) ")
            ch=int(input("enter your choice : "))
            if ch==1:
                i21=float(input("enter cutoff: "))
                for x in c:
                    if float(x[-6])==i21 and x[-4]==i1:
                        if x[-3] in couns:
                            if x[-2] in cou:
                                disp(x)
                                lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
            if ch==2:
                l1=float(input("enter starting limit of your cutoff range : "))
                l2=float(input("enter ending limit of your cutoff range : "))
                for x in c:
                    te=float(x[-6])
                    if l1<=te and te<=l2:
                        if x[-4]==i1 and x[-2] in cou:
                            if x[-3] in couns:
                                disp(x)
                                lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
def round2():
    f1=open("round_2.txt","r")
    print("=============WELCOME==============")
    print(" hi there, this is a combined program involving all the 4 rounds and hereby specify the given cutoff range for given rounds: ")
    A=f1.readlines()
    d=[]
    c=[]
    couns=[]
    dic={'1': 'CEG', '2': 'ACT', '4': 'MIT', '1112': 'RMD', '1113': 'RMK', '1114': 'SA', '1116': 'SRI VENKATESHWARA', '1120': 'VELAMMAL', '1140': 'JPR', '1211': 'REC', '1216': 'SAVEET', '1219': 'VENKATESH', '1225': 'LOYOLLA', '1304': 'SRM', '1306': 'jpr', '1309': 'meenak_sundar', '1315': 'SSN', 'SAI RAM': 'SAI RAM', '1324': 'SAI RAM', '1413': 'VENKATESH.TECH', '1414': 'PRINCE', '1419': 'sai ram', '1422': 'SRM.VALLI', '1432': 'RIT', '1210': 'PANIMALAR'}
    print(dic)
    for i in A:
        j=i.split()
        d.append(j)
    for mn in d:
        if len(mn)>10:
            c.append(mn)
    def disp(x):
        print(x[0],x[1],x[-6],x[-4],x[-5],dic.get(x[-3]),x[-2],x[-1])
    lena=[]
    print("----------welcome-----------")
    i1=input("input enter commounity: ")
    cou=[]
    print(" select course! you can choose any number of courses that you'd like to enter, type end if it is completed :) ")
    while True:
        inp=input("enter course : ")
        if inp=="end":
            break
        else:
            cou.append(inp)
    if inp=="end":
        print("  1: any college is fine ")
        print("  2: only selected college and will enter using counselling code ")
        i2=int(input("enter your choice : "))
        if i2==1:
            print(" option 1 confirmed!! ")
            print(" 1: only a particular cutoff ")
            print(" 2: range wise selection e.g (185-197) ")
            ch=int(input("enter your choice : "))
            if ch==1:
                i21=float(input("enter cutoff: "))
                for x in c:
                    if float(x[-6])==i21 and x[-5]==i1:
                        if x[-2] in cou:
                            disp(x)
                            lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
            if ch==2:
                l1=float(input("enter starting limit of your cutoff range : "))
                l2=float(input("enter ending limit of your cutoff range : "))
                for x in c:
                    te=float(x[-6])
                    if l1<=te and te<=l2:
                        if (x[-5]==i1) and (x[-2] in cou):
                            disp(x)
                            lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
        if i2==2:
            print(" option 2 confirmed!! ")
            while True:
                inp=input("enter counselling code : ")
                if inp=="end":
                    break
                else:
                    couns.append(inp)
            print(" 1: only a particular cutoff ")
            print(" 2: range wise selection e.g (185-197) ")
            ch=int(input("enter your choice : "))
            if ch==1:
                i21=float(input("enter cutoff: "))
                for x in c:
                    if float(x[-6])==i21 and x[-5]==i1:
                        if x[-3] in couns:
                            if x[-2] in cou:
                                disp(x)
                                lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
            if ch==2:
                l1=float(input("enter starting limit of your cutoff range : "))
                l2=float(input("enter ending limit of your cutoff range : "))
                for x in c:
                    te=float(x[-6])
                    if l1<=te and te<=l2:
                        if x[-5]==i1 and x[-2] in cou:
                            if x[-3] in couns:
                                disp(x)
                                lena.append(x)
                print(len(lena)," these are the number of students allocoated with respective seats in respective colleges ")
    return lena
print("round1 ends with 184 cutoff: ")
print("round2 ends with 163 cutoff: ")
print("based on your required cutoff, choose the suitable round by choosing: ")
print("1: round 1")
print("2: round 2")
QUERY=int(input("enter your choice: "))
if QUERY==1:
    round1()
if QUERY==2:
    round2()
    




        
        
            
                    
                
                


        




        
        
            
                    
                
                
