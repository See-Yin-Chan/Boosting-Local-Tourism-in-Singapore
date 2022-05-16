# -*- coding: utf-8 -*-
import pandas as pd
import time
from itertools import combinations
import random

df = pd.read_csv("price.csv")
df1 = pd.read_csv("deals.csv", encoding= 'unicode_escape')
df3 = pd.read_csv("activities6.csv")
df4 = pd.read_csv("activities7.csv")
df6 = pd.read_csv("dining.csv")
ussdf = pd.read_csv("ussrecom.csv") 
ussdic = ussdf.to_dict('list')
zoodf = pd.read_csv("zoorecom.csv") 
zoodic = zoodf.to_dict('list')
riverdf = pd.read_csv("riverrecom.csv") 
riverdic = riverdf.to_dict('list')
nightdf = pd.read_csv("nightrecom.csv") 
nightdic = nightdf.to_dict('list')
flyerdf = pd.read_csv("flyerrecom.csv") 
flyerdic = flyerdf.to_dict('list')
birddf = pd.read_csv("birdrecom.csv") 
birddic = birddf.to_dict('list')

####@ =============================================

def listToremove(list):
    return str(list).replace('[','').replace(']',"").replace("'","")

def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')
    
####@ =============================================

def printMenu():
    print("""\
Welcome to E-agency!

What would you like to do today?

1. Cheap Cheap Deals
2. Make My Day
3. What's For Free
4. Hungry Eat What
""")

def processCommand():
    def getdeals(a):
        if option == a:
            print("-"*81)
            for each in df1[str(a)]:
                print(each)
                print("-"*81)
                time.sleep(3)
            
    def getactivities(b):
        if loc == b:
            total = float(df["Child"][b]+df["Adult"][b]+df["Senior Citizen"][b])
            att = df["Attractions"][b]
            remainbud = budget - total
            print(f"Your remaining budget is ${remainbud:.2f}.")
            if remainbud < 0:
                print("Please enter another attraction.")
            a = df3.columns.get_loc(str(att))
            df4 = df3.iloc[:,a:a+2]
            col_name = list(df4.columns)[1]
            df5 = df4[df4[str(col_name)] > 0]
            act = list(df5.iloc[:, 0])       
            pri = list(df5.iloc[:, 1])        
            dic = dict(zip(act, pri))
            lis = []
            for key, value in dic.items():
                lis.append(value)
            x = 0
            for each in lis:  
                if remainbud > each:
                    x += 1 
            if x > 0:
                for i in range(1,3):    
                    all_comb = list(combinations(lis, i))
                    for each_comb in all_comb:
                        s = []
                        if sum(each_comb) <= remainbud:
                            for each_item in each_comb:
                                for val in dic.values():
                                    if val == each_item:
                                        b = list(dic.keys())[list(dic.values()).index(each_item)]
                                        s.append(b)
                            a = listToremove(s)
                            print(f"The recommended activities are {a}.")
                            print("-"*81)
                            time.sleep(1.5)
            elif x == 0:
                print("\n")
                print("Please check out the free and fun activities!")
                print("\n")
                
    def printrecom(indexno, nameofdic):
        if loc == indexno:
            recom = list(nameofdic.keys())
            random_recom = random.choice(recom)
            print(random_recom)
            a = nameofdic.get(random_recom)
            b = listToStringWithoutBrackets(a)
            c = float(b)
            if c == 0:
                print("The activities at this location are free. Go for it!")
                print("-"*81)
            else:
                print(f"It costs ${c:.2f} but it's definitely worth it!")
    
    def combineactandrecom(a, dictname):
        getactivities(a)
        time.sleep(2)
        printrecom(a, dictname)
        
    def getfreeactivities():
        act =  list(df5[str(att)])
        if len(act) == 0:
            print("There are no free activities. However, there are other fun things to do!")
        else:
            print("Here are some free activities in this attraction:")
            time.sleep(1)
            for each in act:
                print(each)
                time.sleep(3)
        print("-"*81)
    
    def getdining(a):
        if option == a:
            print("-"*81)
            for each in df6[str(a)]:
                print(each)
                print("-"*81)
                time.sleep(3)
    
    ####@ =============================================
    while True:
        while True:
            try:
                cmdStr = int(input("Enter command character to proceed: "))
                if cmdStr < 1 or cmdStr > 4:
                    print("Invalid. Please enter a valid number from 1 to 4.")
                    continue
                else: break
            except ValueError: 
                print("Please enter a valid number from 1 to 4.")
        if cmdStr == 1:
            print(df["Attractions"])
            while True:
                try:
                    loc = int(input("Enter the index number of attraction: "))
                    if loc < 0 or loc > 5:
                        print("Invalid. Please enter a valid number from 0 to 5.")
                        continue
                    else:
                        break
                except:
                    print("Please enter a valid number from 0 to 5.")                    
            option = int(loc)
            getdeals(0) 
            getdeals(1) 
            getdeals(2) 
            getdeals(3) 
            getdeals(4)
            getdeals(5)
            pass
            printMenu()
        elif cmdStr == 2:
            print("Here are the prices of the various attractions (in SGD):")
            print(df)
            while True: 
                try:
                    nchild = int(input("Enter the number of children (0 - 12 years): "))
                    if nchild < 0:
                        print("Error. Pls enter a valid number.")
                        continue
                    else: break 
                except:
                    print("Pls enter a valid number.")
            while True: 
                try:
                    nadult = int(input("Enter the number of adult(s) (13 - 59 years): "))
                    if nadult < 0:
                        print("Error. Pls enter a valid number.")
                        continue
                    else: break 
                except:
                    print("Pls enter a valid number.")
            while True: 
                try:
                    nseci = int(input("Enter the number of senior citizen(s) (> 59 years): "))
                    if nseci < 0:
                        print("Error. Pls enter a valid number.")
                        continue
                    else: break 
                except:
                    print("Pls enter a valid number.")
            while True: 
                l = 0
                while True:                     
                    try:
                        budget = float(input("What is your budget: "))
                        if budget < 0:
                            print("Error. Pls enter a valid number.")
                            continue
                        else: break 
                    except:
                        print("Pls enter a valid number.")      
                print("-"*81)
                for i, j, k, s in zip(list(df["Child"]), list(df["Adult"]), list(df["Senior Citizen"]), range(7)):
                    total = i*nchild + j*nadult + k*nseci
                    att = df["Attractions"][s]
                    if total <= budget:
                        print(f"You can visit {att} for ${total:.2f}.")
                        time.sleep(0.5)
                        l += 1
                if l == 0:
                    print("Insufficient budget. Please enter a new budget.")
                    continue
                else: 
                    break 
            print("-"*81)
            print(df["Attractions"])
            while True:
                try:
                    loc = int(input("Enter the index number of attraction: "))
                    if loc > 5:
                        print("Invalid. Please enter a correct number.")
                        continue
                    else: break
                except:
                    print("Error. Please enter a valid number. ")
            combineactandrecom(0, ussdic)
            combineactandrecom(1, zoodic)
            combineactandrecom(2, riverdic)
            combineactandrecom(3, nightdic)
            combineactandrecom(4, flyerdic)
            combineactandrecom(5, birddic)
            print("-"*81)
            pass
            printMenu()
        elif cmdStr == 3:
            print(df["Attractions"])
            while True:
                try:
                    loc = int(input("Enter the index number of attraction: "))
                    if loc > 5:
                        print("Invalid. Please enter a correct number.")
                        continue
                    else: break
                except:
                    print("Error. Please enter a valid number. ")
            if loc == 0:
                att = df["Attractions"][0]
                df5 = df4[df4.Price0 == 0].loc[:,[str(att), "Price0"]]
                getfreeactivities()
            if loc == 1:
                att = df["Attractions"][1]
                df5 = df4[df4.Price1 == 0].loc[:,[str(att), "Price1"]]
                getfreeactivities()
            if loc == 2:
                att = df["Attractions"][2]
                df5 = df4[df4.Price2 == 0].loc[:,[str(att), "Price2"]]
                getfreeactivities()
            if loc == 3:
                att = df["Attractions"][3]
                df5 = df4[df4.Price3 == 0].loc[:,[str(att), "Price3"]]
                getfreeactivities()
            if loc == 4:
                att = df["Attractions"][4]
                df5 = df4[df4.Price4 == 0].loc[:,[str(att), "Price4"]]
                getfreeactivities()
            if loc == 5:
                att = df["Attractions"][5]
                df5 = df4[df4.Price5 == 0].loc[:,[str(att), "Price5"]]
                getfreeactivities()
            pass
            printMenu()
        elif cmdStr == 4:
            print(df["Attractions"])
            while True:
                try:
                    loc = int(input("Enter the index number of attraction: "))
                    if loc > 5:
                        print("Invalid. Please enter a valid number from 0 to 5.")
                        continue
                    else:
                        break
                except:
                    print("Please enter a valid number from 0 to 5.")                    
            option = int(loc)
            getdining(0) 
            getdining(1) 
            getdining(2) 
            getdining(3) 
            getdining(4)
            getdining(5)
            pass
            printMenu()
    return

def main():
    printMenu()
    processCommand()
    
if (__name__ == "__main__"):
    main()
