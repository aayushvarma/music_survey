# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 23:19:39 2020

@author: Praveen Varma
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import webbrowser as web
import sys as sys
df1=pd.read_csv(r"C:\Users\Praveen Varma\Downloads\music.csv")
df2=pd.read_csv(r"C:\Users\Praveen Varma\Downloads\music2.csv")
df4=pd.read_csv(r"C:\Users\Praveen Varma\Downloads\music4.csv")
df6=pd.read_csv(r"C:\Users\Praveen Varma\Downloads\music6.csv")
print()
print("********************************************************************")
print("MUSIC ARTISTS SURVEY") 
print("********************************************************************")
print()
print("ENTER 0 TO VIEW ALL STATS")
print("ENTER 1 TO READ ABOUT THE WEEKND")
print("ENTER 2 TO READ ABOUT DRAKE")    
print("ENTER 3 TO READ ABOUT RIHANNA")
print("ENTER 4 TO READ ABOUT TRAVIS SCOTT")
print("ENTER 5 TO READ ABOUT EMINEM")
print("ENTER 6 TO READ ABOUT KANYE WEST")
print("ENTER 7 TO READ ABOUT CHRIS BROWN")
print("ENTER 8 TO READ ABOUT BLACKBEAR")
print("ENTER 9 TO READ ABOUT KENDRICK LAMAR")
print("ENTER 10 TO READ ABOUT J. COLE")
print("ENTER 11 TO READ ABOUT JAY-Z")
print("ENTER 12 TO READ ABOUT TWENTY ONE PILOTS")
print("ENTER 13 TO READ ABOUT ARCTIC MONKEYS")
print("ENTER 14 TO READ ABOUT THE NBHD")
print("ENTER 15 TO READ ABOUT LOGIC")
print("ENTER 16 TO VIEW ANOTHER ARTIST OR MOVE TO NEXT CATEGORY")
x=1
while x<17:   
            
    x=int(input("Enter any number between 0-15 to view the respective Artist: "))
 
    if x==0:
        print(df1)
        print("------------------------------------------------------------------")
        print("Some Additional Information:")
        print("------------------------------------------------------------------")
        print(df2)
    elif x==1:
        print(df1.iloc[0])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/The_Weeknd")
        
    elif x==2:
        print(df1.iloc[1])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Drake_(musician)")
        
    elif x==3:
        print(df1.iloc[2])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Rihanna")
        
    elif x==4:
        print(df1.iloc[3])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
          web.open("https://en.wikipedia.org/wiki/Travis_Scott")
        
    elif x==5:
        print(df1.iloc[4])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Eminem")
        
    elif x==6:
        print(df1.iloc[5])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Kanye_West")
        
    elif x==7:
        print(df1.iloc[6])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Chris_Brown")
        
    elif x==8:
        print(df1.iloc[7])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Blackbear")
        
    elif x==9:
        print(df1.iloc[8])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Kendrick_Lamar")
        
    elif x==10:
        print(df1.iloc[9])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/J_Cole")
        
    elif x==11:
        print(df1.iloc[10])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Jay_Z")
        
    elif x==12:
        print(df1.iloc[11])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Twenty_One_Pilots")
        
    elif x==13:
        print(df1.iloc[12])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/Arctic_Monkeys")
        
    elif x==14:
        print(df1.iloc[13])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e=="y":
         web.open("https://en.wikipedia.org/wiki/The_Neighbourhood")
        
    elif x==15:
        print(df1.iloc[14])
        e=str(input("To View the Artist's Wikipedia Page Enter Y"))
        if e== "y":
         web.open("https://en.wikipedia.org/wiki/Logic_(rapper)")
        
    elif x==16:
        print("To move to next set enter y for YES and n for NO ")
        a=str(input("Type y or n :"))
        
        if a == "n" :
           x=1
        else :
            print("You are now going to view the next Category.")
    else:
        print("Invalid Option")
        x=1
        while x>17:
            
            x=1
            x+=1
    x+=1    
        
print()
print()
print("*************************************************************************") 
print()
print()

df1=pd.read_csv(r'C:\Users\Praveen Varma\Downloads\music.csv')
df2=pd.read_csv(r"C:\Users\Praveen Varma\Downloads\music2.csv")
print("To View the First 5 Artists Enter 1.")
print("To View the Last 5 Artists Enter 2.")  
print("To View the Real Names of all Artists Enter 3. ")    
print("To View the Net Worth of all Artists Enter 4.")
print("To View Artist Info of those who have more than 25 Million Monthly Listeners Enter 5.")
print("To View Artist Info of those who are in the top 10 enter 6.")
print("To View the Artist Info of those who are still producing music Enter 7.")
print("To View the Artists that started their career before 2000 Enter 8")
print("To View the Artists who have more than 10 Albums Enter 9")
print("To View the Monthly Listeners of all Artists Enter 10")
print("To Enter Information about a new Artist Enter 11")
print("To Look at a Graphs of all Numerical Values Enter 12")
print("To Exit the Program Enter 13.")

df8=pd.read_csv(r'C:\Users\Praveen Varma\Documents\music8.csv')
k=df8['Names']
j=df8["Single Songs"]
df7=pd.read_csv(r'C:\Users\Praveen Varma\Documents\music9.csv')
p=df7['Names']
t=df7["NetWorth(Mn)"]
df10=pd.read_csv(r"C:\Users\Praveen Varma\Documents\music10.csv")
v=df10['Artist Name']
w=df10["No. of Albums"]
z=1
while z<14:    

    z=int(input("Enter Number: ")) 
    if z==1:
        print(df1.head(5))
    elif z==2:
        print(df2.tail(5))
    elif z==3: 
        print(df2[["Names","Real Names"]])
    elif z==4:
        print(df2[["Names","Net Worth"]])
    elif z==5:
        print(df2.head(8))
    elif z==6:
        print(df2.head(10))
    elif z==7:
        print(df2.head(14))
    elif z==8:
        print(df4)
    elif z==9:
        print(df6)
    elif z==10:
        print(df2[["Names","Monthly Listeners"]])
    elif z==11:
        print("Enter details of New Artist")
        p=(input("Enter Name of New Artist: "))
        q=(input("Enter Worldwide Rank of New Artist: "))
        r=(input("Enter Active Years of New Artist: "))
        s=(input("Enter Genre of New Artist: "))
        t=(input("Enter No. of Albums of New Artist: "))
        u=(input("Enter No. of Singles of New Artist: "))
        v=(input("Enter Most Sold ALbum of New Artist: "))
        df1.at[16,:]=p,q,r,s,t,u,v
        print(df1)
    
    elif z==12:
        print("To view Graph on Net Worths Enter 1")
        print("To view Graph on No. of Singles Enter 2")
        print("To view Graph on No. of Albums Enter 3")
        print("To exit Enter 4")
        
        
    

      
        h=1
        while h<4:
            h=int(input("Select any No. from 1-3 to view the respective Graphs."))
            if h==1:
                plt.title("Net Worths")
                plt.xticks(rotation='vertical')
                plt.xlabel("Net Worth")
                plt.ylabel(" Artist Name")
                plt.bar(p,t)
                plt.show()
        
            elif  h==2:
                plt.title("No. of Singles")
                plt.xticks(rotation='vertical')
                plt.xlabel("No. of Singles")
                plt.ylabel("The Artist")
                plt.barh(k,j)
                plt.show()
    
            elif h==3:
                plt.title("No. of Albums")
                plt.xticks(rotation='vertical')
                plt.xlabel("No. of Albums")
                plt.ylabel("The Artist")
                plt.barh(v,w)
                plt.show()
     
            elif h==4:
                print("You will now go back to Original Set.")

        
            else:
                print("Invalid Option.Please try again.")
                
               
    elif z==13:
        print("You are now exiting the Program.Thank you.")
        sys.exit()
else:
    print("Invalid Option")
    z=1
    while z>14:
            
        z=1
        z+=1
z+=1    


    

        
    
        

   
   
   

   
   
  