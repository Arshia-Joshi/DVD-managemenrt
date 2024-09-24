import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

print ("*************** WELCOME TO UNIVERSAL DVD SYSTEM ****************")
print ( "  ")

def addNewDVD():
    #print ("in Add New DVD")
    dvdid = int(input("Enter a DVD id : "))
    title = input("Enter a DVD title : ")
    actor = input("Enter Actor : ")
    director = input("Enter Director : ")
    genre = input("Enter Genre of Movie : ")
    language = input("Enter language of movie : ")
    year = input("Enter year of movie Release : ")
    bdf = pd.read_csv(r"D:\\Project\\DVD.csv")
    n = bdf["DVD_Id"].count()
    bdf.at[n] = [dvdid,title,actor,director,genre,language,year]
    bdf.to_csv(r"D:\\Project\\DVD.csv",index = False)
    print (" DVD added succesfully ")
    print(bdf)                
    print ("--------------------------------------")

def searchDVD():
    #print ( "in search DVd")
    title = input("Enter a DVD name : ")
    bdf = pd.read_csv(r"D:\\Project\\DVD.csv")
    df = bdf.loc[bdf["DVD_Title"] == title]
    if df.empty:
        print("No DVD found with this title")
    else:
        print ("DVD details are : " )
        print (df)
    print ("--------------------------------------")

def deleteDVD():
     #print ("in deelete DVD")
     dvdid = float(input("ENter a DVD id : "))
     bdf = pd.read_csv(r"D:\\Project\\DVD.csv")
     bdf=bdf.drop(bdf[bdf["DVD_Id"]== dvdid].index)
     bdf.to_csv(r"D:\\Project\\DVD.csv",index = False)
     print (" DVD deleted succesfully ")
     print(bdf)    
     print ("--------------------------------------")

def showDVD():
    #print ("in show dvd")
    bdf = pd.read_csv(r"D:\\Project\\DVD.csv")
    print (bdf)
    print ("--------------------------------------")

def showMembers():
    #print ("in show members")
    bdf = pd.read_csv(r"D:\\Project\\Members.csv")
    print (bdf)
    print ("--------------------------------------")

def issueDVD():
    #print ("in issue DVD")
    dvd_name = input("Enter DVD name : ")
    bdf = pd.read_csv(r"D:\\Project\\DVD.csv")
    bdf = bdf.loc[bdf["DVD_Title"] == dvd_name]
    if bdf.empty:
        print("No DVD found with this title")
        return

    m_name = input ("Enter member name : ")
    mdf = pd.read_csv(r"D:\\Project\\Members.csv")
    mdf = mdf.loc[mdf["Member_Name"] == m_name]
    if mdf.empty:
        print("No such member found")
        return

    #dateofissue = int(input("Enter date of issue DDMMYYY " ))
    dateofissue = date.today()
    numberofDVDissued= int(input("Enter number of DVD issued : "))
    bdf = pd.read_csv(r"D:\\Project\\issuedvd.csv")
    n = bdf["Dvd_Name"].count()
    bdf.at[n] = [dvd_name,m_name,dateofissue,numberofDVDissued,""]
    bdf.to_csv(r"D:\\Project\\issuedvd.csv",index = False)
    print (" DVD issued succesfully ")
    print(bdf) 
    
    print ("--------------------------------------")

def returnDVD():
    #print ("in return DVD")
    m_name = input ("Enter member name : ")
    dvd_name = input("Enter DVD name : ")
    idf = pd.read_csv(r"D:\\Project\\issuedvd.csv")
    idf = idf.loc[idf["Dvd_Name"] == dvd_name]
    if idf.empty:
        print("This DVD is not issued in records ")
    else:
        idf = idf.loc[idf["Member_Name"] == m_name]
        if idf.empty:
            print("This DVD is not issued to this member")
        else:
            print ("DVD can be returned")
            ans = input("Are you sure you want to return this DVD ? ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"D:\\Project\\issuedvd.csv")
                #idf=idf.drop(idf[idf["Dvd_Name"]== dvd_name].index)
                #n=idf[idf["Dvd_Name"]== dvd_name].index
                #n=idf.query(idf["Dvd_Name"] == dvd_name & idf["Member_Name"] == m_name).index
                n=idf.query('Dvd_Name == @dvd_name & Member_Name == @m_name').index
                print(n)
                return_date = date.today()
                idf.loc[n,"Date_of_Return"] = return_date
                #idf.at[n] = [dvd_name,m_name,dateofissue,numberofDVDissued,return_date]
                idf.to_csv(r"D:\\Project\\issuedvd.csv",index = False)
                print (" DVD returned succesfully ")
                
            else:
                print("retuirn operation cancelled")
       
        
    
    print ("--------------------------------------")

def showIssuedDVD():
    #print ("in show issued dvds")
    idf = pd.read_csv(r"D:\\Project\\issuedvd.csv")
    print (idf)
    print ("--------------------------------------")
           
def login():
    uname = input ("Enter username : ")
    pwd = input ("Enter password : ")
    df = pd.read_csv(r"D:\\Project\\users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print ("Invalid username")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print ("Invalid password")
            return False
        else:
            print ("welcome " + uname)
            print (" ")
            return True

def Showmenu():
    print ("-------------------------------------------------")
    print ("              UNIVERSAL DVD MENU                 ")
    print ("-------------------------------------------------")
    print (" Press 1 - Add a New DVD")
    print (" Press 2 - Search for a DVD")
    print (" Press 3 - Delete a DVD")
    print (" Press 4 - Show all DVDs")
    print (" Press 5 - Show all Members")
    print (" Press 6 - Issue a  DVD")
    print (" Press 7 - Return a DVD")
    print (" Press 8 - Show all issued DVDs")
    print (" Press 9 - To exit")
    print (" ")
    choice = int(input("Enter an Option : "))
    return choice


if login():
    while True:
        ch = Showmenu()
        print (" choice selected is " + str(ch))
        if ch == 1:
            addNewDVD()
        elif ch == 2:
            searchDVD()
        elif ch == 3:
            deleteDVD()
        elif ch == 4:
            showDVD()
        elif ch == 5:
            showMembers()
        elif ch == 6:
             issueDVD()
        elif ch == 7:
             returnDVD()
        elif ch == 8:
             showIssuedDVD()
        elif ch == 9:
            break
        else:
            print ("Invalid Option selected - Please select correct option ")
            print(" ")
              
print (" ")            
print ("Thank you for visiting Universal DVD")
