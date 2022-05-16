# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from datetime import datetime 
import seaborn as sns

def printMenu():
    print("""\
Welcome to Data Analytics.

    1. COVID-19 cases (Singapore)
    2. COVID-19 cases (Tourist Country Origin)
    3. International Visitors
    4. Tourism Receipts
    5. Outbound Departures of Singapore Resident
    6. Correlation between Outbound Departures and COVID-19 cases 
    7. Exit
    
""")


def processCommand():
    while True:
        cmdStr = input("Enter command character to retrieve the cleaned data along with the graphs:")
        print("\n")
        if cmdStr == "1":
            ###DATAFRAME (Covid in SG)
            df = pd.read_csv("Covid.csv")
            
            #Select Top 5 Countries
            dff = df[df.location == "Singapore"]
            
            #Select relevant columns
            dfff = dff[["location", "date", "total_cases"]]
            #dfff.head()
            
            #Split the date into date-month-year
            dfff[['Date', 'Month', 'Year']] = dfff.date.str.split("/", expand=True)
            
            #Extract first day of each month 
            data = dfff[(dfff.Date == "1")]
            print("Final Table:", "\n")
            print(data.head())
            
            ###PLOTTING (Graph 1: Covid in SG)  
            plt.title("Covid Situation in Singapore")
            plt.xlabel("Months")
            plt.ylabel("Total Number of Covid Cases")
            plt.xticks(rotation=90)
            plt.plot(data.date, data["total_cases"])
            plt.show()
            
        elif cmdStr == "2":
            ###DATAFRAME (Tourist Country Origin)
            df = pd.read_csv("Covid.csv")
            
            #Select Top 5 Countries
            dff = df[(df.location == "China")|(df.location == "Australia")|(df.location == "India")|(df.location == "Indonesia")|(df.location == "Malaysia")]
            
            #Select relevant columns
            dfff = dff[["location", "date", "total_cases"]]
            dfff.head()
            
            #Split the date into date-month-year
            dfff[['Date', 'Month', 'Year']] = dfff.date.str.split("/", expand=True)
            
            
            #Extract first day of each month 
            data = dfff[(dfff.Date == "1")]
            print("Final Table:", "\n")
            print(data.head())
            
            ###PLOTTING (Graph 2: Covid in tourist origin countries)
            aus = data[data.location == 'Australia']
            chi = data[data.location == 'China']
            ind = data[data.location == 'India']
            mal = data[data.location == 'Malaysia']
            indo = data[data.location == 'Indonesia']
            plt.plot(aus['date'], aus['total_cases'], 'b', label='Australia')
            plt.plot(chi['date'], chi['total_cases'], 'r', label='China')
            plt.plot(mal['date'], mal['total_cases'], 'yellow', label='Malaysia')
            plt.plot(indo['date'], indo['total_cases'], 'purple', label='Indonesia')
            plt.title("Number of Covid Cases in Singapore's Top Tourist Origin Countries")
            plt.xlabel("Dates")
            plt.ylabel("Number of Covid Cases")
            plt.xticks(rotation=90)
            plt.legend()
            plt.show()
            
        elif cmdStr == "3":   
            #DATAFRAME (International Visitors)
            df = pd.read_csv('International Visitors to Singapore.csv')
            inv_df = df.T
            
            ## Rename columns
            headers = inv_df.iloc[0]
            new_df  = pd.DataFrame(inv_df.values[1:], columns=headers)
            #new_df.head()
            
            ## Drop redundant columns
            new_df.columns
            new_df.drop([' Topic : International Visitor Arrivals ', ' Title  : M550001 - International Visitor Arrivals By Inbound Tourism Markets, Monthly '], inplace=True, axis=1)
            
            ## Drop redundant rows
            new_df = new_df.drop([0,1])
            
            # Select columns
            #new_df.columns
            #print(new_df.columns)
            data = new_df.rename(columns={' Variables ':'Dates', ' Total International Visitor Arrivals By Inbound Tourism Markets * ': "Total"})
            #data.head()
            data = data[['Dates', 'Total', '         Indonesia ', '         Malaysia ', '         China ', '         India ','         Australia ']]
            print("Final Table:", "\n")
            print(data)

            ###PLOTTING (Graph 1: Total Number Of International Visitors)     
            data["Total"] = data["Total"].str.replace(",","").astype(float)
                            
            plt.title("Total Number of International Visitors Each Month")
            plt.xlabel("Months")
            plt.ylabel("Number of International Visitors")
            plt.plot(data['Dates'], data['Total'])
            plt.xticks(rotation=90)
            plt.show()
                
            ###PLOTTING (Graph 2: Top Countries)
            data['         Indonesia '] = data['         Indonesia '].str.replace(",","").astype(float)
            data['         Malaysia '] = data['         Malaysia '].str.replace(",","").astype(float)
            data['         China '] = data['         China '].str.replace(",","").astype(float)
            data['         India '] = data['         India '].str.replace(",","").astype(float)
            data['         Australia '] = data['         Australia '].str.replace(",","").astype(float)
                            
            plt.title("Number of International Visitors From Top 5 Countries To Singapore")
            plt.xlabel("Months")
            plt.xticks(rotation=90)
            plt.ylabel("Number of International Visitors")
            plt.plot(data['Dates'], data['         Indonesia '], 'r', label='Indonesia')
            plt.plot(data['Dates'], data['         Malaysia '], 'g', label='Malaysia')
            plt.plot(data['Dates'], data['         China '], 'y', label='China')
            plt.plot(data['Dates'], data['         India '], 'brown', label='India')
            plt.plot(data['Dates'], data['         Australia '], 'purple', label='Australia')
            plt.legend()    
            plt.show()
            
            
        elif cmdStr == "4":
            ###DATAFRAME (Tourism Receipts)
            filename = "Tourism Receipts.csv"
            df = pd.read_csv(filename)
            
            #Drop rows/columns with Nan 
            df = df.dropna()
            
            #Rename column names (with row 3, i.e. Quarter Year)
            df.columns = df.loc[3]
            
            #Remove row 3 (which is now the columns names)
            df = df.drop(3)
            
            #Extract necessary columns
            dff = df.loc[5:8,["Variables", "2019 1Q", "2019 2Q", "2019 3Q", 
                          "2019 4Q", "2020 1Q"]]
            
            #Rename row (with column 0, i.e. ‘Variables’ column)
            dff.index = dff.iloc[:, 0]
            del dff["Variables"]
            print("Final Table:", "\n")
            print(dff)
            
            ###PLOTTING (Line Graph of Singapore Tourism Receipt by Year (Quarterly))
            #Converting values from string to float
            dff["2019 1Q"] = dff["2019 1Q"].str.replace(",","").astype(float)
            dff["2019 2Q"] = dff["2019 2Q"].str.replace(",","").astype(float)
            dff["2019 3Q"] = dff["2019 3Q"].str.replace(",","").astype(float)
            dff["2019 4Q"] = dff["2019 4Q"].str.replace(",","").astype(float)
            dff["2020 1Q"] = dff["2020 1Q"].str.replace(",","").astype(float)
            
            graph = dff.T.plot.line(title = "Singapore Tourism Receipt by Year (Quaterly)")
            graph.set_xlabel("Year (Quarterly)")
            graph.set_ylabel("Tourism Receipts")
            plt.show()
            pass
        
        elif cmdStr == "5":
            ###DATAFRAME (Outbound Departures)
            fname = "Outbound Departures.csv"
            df = pd.read_csv(fname)  
            #Rename columns
            df.columns = ['Time','Total Outbound Departures of Singapore Residents','Total Outbound Departures of Singapore Residents (Air)','Total Outbound Departures of Singapore Residents (Sea)']  
            #Delete redundant rows 
            df_cleaned = df.drop(df.index[0:5])
            df_cleaned1 = df_cleaned.drop(df.index[120:135])
            df_cleaned2 = df_cleaned1.drop(df.index[13:120])
            df_cleaned3 = df_cleaned2.drop(['Total Outbound Departures of Singapore Residents (Air)'], axis=1)
            df_cleaned4 = df_cleaned3.drop(['Total Outbound Departures of Singapore Residents (Sea)'], axis=1)    
            #Change of string to integer format
            df_cleaned4["Total Outbound Departures of Singapore Residents"] = df_cleaned4["Total Outbound Departures of Singapore Residents"].str.replace(",","").astype(int)
            print("Final Table:", "\n")
            print(df_cleaned4)
            
            ###PLOTTING (Bar Graph for Total Outbound Departure)
            labels = ['2019 Dec','2020 Jan','2020 Feb','2020 Mar','2020 Apr','2020 May','2020 Jun','2020 Jul']
            Total = [1271780,759018,420253,207985,5237,6265,8528,10304]
            
            #Reindexing
            df_cleaned33 = df_cleaned4.reindex([23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5])
            
            x = np.arange(len(labels))  
            width = 0.8
            fig, ax = plt.subplots()
            rects1 = ax.bar(x - width/2, Total, width, label='Total Outbound Departures of Singapore Residents')
            
            ax.set_ylabel('Total Outbound Departures of Singapore Residents')
            ax.set_title('Bar Graph for Total Outbound Departures of Singapore Residents')
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            plt.xticks(rotation=90)
            ax.legend()
            #Adding of labels
            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    ax.annotate('{}'.format(height),
                                xy=(rect.get_x() + rect.get_width() / 2, height),
                                xytext=(0, 3),
                                textcoords="offset points",  
                                ha='center', va='bottom')
            
            plt.rcParams["figure.figsize"] = (15,10) 
            autolabel(rects1)
            plt.show()          
            pass
        
        elif cmdStr == "6":
            ###DATAFRAME (Correlation)
            Total_Outbound_Departures_of_Singapore_Residents = [759018,420253,207985,5237,6265,8528,10304]
            Total_Cases = [13,85,746,14797,18725,9295,8148]
            
            ###PLOTTING (Scatterplot to find correlation)
            fig=plt.figure()
            ax=fig.add_axes([0,0,1,1])
            ax.scatter(Total_Cases, Total_Outbound_Departures_of_Singapore_Residents, color='r')
            ax.set_xlabel('Total Cases')
            ax.set_ylabel('Total Outbound Departures of Singapore Residents')
            ax.set_title('Correlation between Total Cases and Total Outbound Departures of Singapore Residents ')
            plt.show()

             
        elif cmdStr == "7":
            print("Goodbye :)")
            break
        else:
            print("Error! Please enter valid number from 1 to 7")
            pass
    return

def main():
    printMenu()
    processCommand()
    

if (__name__ == "__main__"):
    main()
