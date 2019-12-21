from collections import OrderedDict
import json 
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

class Person():
    def __init__(self,personID=None,firstName=None,surname=None,age=None,gender=None,friends=None):
        self.id=personID
        self.firstName=firstName
        self.surname=surname
        self.age=age
        self.gender=gender
        self.friends=friends
        
    def set_id(self,personID):
        self.id=personID     
    def get_id(self):
        return self.id
    
    def set_firstName(self,firstName):
        self.firstName=firstName     
    def get_firstName(self):
        return self.firstName
    
    def set_surname(self,surname):
        self.surname=surname     
    def get_surname(self):
        return self.surname
    
    def set_age(self,age):
        self.age=age     
    def get_age(self):
        return self.age
    
    def set_gender(self,gender):
        self.gender=gender    
    def get_gender(self):
        return self.gender
    
    def set_friends(self,friends):
        self.friends=friends     
    def get_friends(self):
        return self.friends
		
		

class ProcssData():
    def __init__(self,jsonFilePath=None):
        self.hashTable={} ##self.hashTable is hash table attribute ,which its index is person id and value is person object
        self.lenDataInHashTable=0
        if(not(jsonFilePath==None)):
            self.read_and_process_jsonFile(jsonFilePath)

    ##read data from path of json file and return list of data
    def load_json_data(self,jsonFilePath):
        loadedData=[]
        try:
            jsonData=open(jsonFilePath, 'r')
            loadedData= json.load(jsonData) ## loadedData is list of all json data
        except IOError:
            print("File not accessible")

        return loadedData
    
    ##get list of data from json file as an input and put into hash table 
    def put_data_into_hashTable(self,loadedData):
        for obj in loadedData:
            personObject=Person(personID=obj["id"],firstName=obj["firstName"],surname=obj["surname"],age=obj["age"],\
                   gender=obj["gender"],friends=obj["friends"])
            self.hashTable[obj["id"]]=personObject
            self.lenDataInHashTable+=1

        
    ##get no of data recognized in hash table 
    def get_length_of_hashTable(self):
        return self.lenDataInHashTable
        
    ##read json file and extract data from it then put the data into hash table     
    def read_and_process_jsonFile(self,jsonFilePath):
        loadedData=self.load_json_data(jsonFilePath)
        if(len(loadedData)!=0):
            self.put_data_into_hashTable(loadedData)
    
    ##return person object;given its id 
    def get_person_from_id(self,chosenID):
        return self.hashTable[chosenID]  
    
    ##return direct friends for chosen user; given its id
    def get_direct_friends(self,chosenID):
        return self.hashTable[chosenID].get_friends() ##return list of ids of friends
    
    ##return list of friends of friends for chosen_user; given its id
    def get_friends_of_friends(self,chosenID):
        friendsOfFriends=[]
        directFriendsIDs=self.get_direct_friends(chosenID)
        for directFriendID in directFriendsIDs:
            friendsOfDirectFriendIDs=self.get_direct_friends(directFriendID)
            friendsOfFriends+=friendsOfDirectFriendIDs
        return list(OrderedDict.fromkeys(friendsOfFriends)) ##remove repeated id in friendsOfFriends list if found
    
    ##return suggested friends for chosen user; given its id
    def get_suggested_friends(self,chosenID):
        suggestedFriends=[] ##list of all suggested friend
        countRepeatedId=[0]*21 # create list ,every index in it represent person id, to count all id getten    
        directFriendsIDs=self.get_direct_friends(chosenID)
        for directFriendID in directFriendsIDs:
            friendsOfDirectFriendIDs=self.get_direct_friends(directFriendID)
            for friendOfDirectFriendID in friendsOfDirectFriendIDs:
                countRepeatedId[friendOfDirectFriendID]+=1

        for selectedID in range(len(countRepeatedId)):
            if(not(selectedID==chosenID) and not(selectedID in directFriendsIDs) and countRepeatedId[selectedID]>1):
                suggestedFriends.append(selectedID)

        return list(OrderedDict.fromkeys(suggestedFriends)) ##remove repeated id in suggestedFriends list if found
		
		
class SocialAppGUI():
    def __init__(self,window,procesDataObj):
        self.processDataObj=procesDataObj
        
        ##specify window 
        self.window = window
        self.window.title("Social network app")
        self.window.geometry('550x475')
        self.window.resizable(False,False)
        
        ##specify input label frame 
        self.inputLabelFrame=LabelFrame(self.window, text="Choose user and type of friends",padx=59)
        #self.inputLabelFrame.config(relief=FLAT)
        self.inputLabelFrame.grid(column=0, row=0)
        ##specify choose user label
        self.chooseUserLbl = Label(self.inputLabelFrame, text="Choose user id:",padx=-50)
        self.chooseUserLbl.grid(column=0, row=0)
        ##specify combobox ids
        ComboboxValues=[]
        for i in range(1,self.processDataObj.get_length_of_hashTable()+1):
            ComboboxValues.append(i)
        self.comboIDs = Combobox(self.inputLabelFrame,state="readonly",values=ComboboxValues,width=10)
        self.comboIDs.grid(column=1, row=0)
        self.comboIDs.current(0)
        ##specify choose type of friends label
        lbl = Label(self.inputLabelFrame, text="Choose type of friend to show:")
        lbl.grid(column=0, row=1)
        ##spcify direct friend check button
        self.directFriendVar=IntVar()
        self.directFriendCheckbutton=Checkbutton(self.inputLabelFrame,text="Direct friends",variable=self.directFriendVar)
        self.directFriendCheckbutton.grid(column=0,row=2)
        ##spcify friends of friends check button
        self.friendsOfFriendVar=IntVar()
        self.friendsOfFriendCheckbutton=Checkbutton(self.inputLabelFrame,text="Friends of friends",variable=self.friendsOfFriendVar)
        self.friendsOfFriendCheckbutton.grid(column=1,row=2)
        self.padLbl1 = Label(self.inputLabelFrame, text=" ")  ##pad label
        self.padLbl1.grid(column=2, row=2)
        ##spcify suggested friend check button
        self.suggestedFriendVar=IntVar()
        self.suggestedFriendCheckbutton=Checkbutton(self.inputLabelFrame,text="Suggested friends",variable=self.suggestedFriendVar)
        self.suggestedFriendCheckbutton.grid(column=3,row=2)
        self.padLbl2 = Label(self.inputLabelFrame, text="")
        self.padLbl2.grid(column=4,row=2)
        
        ##sepeicify output label frame
        self.outputLabelframe=LabelFrame(self.window, text="Output")
        self.outputLabelframe.grid(column=0, row=2)
        ##specify direct friend label and scrolled text
        self.directFriendLbl = Label(self.outputLabelframe, text="Direct friends")
        self.directFriendLbl.grid(column=0, row=0)
        self.directFriendsScroll = scrolledtext.ScrolledText(self.outputLabelframe,width=20,height=15)
        self.directFriendsScroll.grid(column=0,row=1)
        self.directFriendsScroll.configure(state='disabled')
        ##specify friends of friend label and scrolled text
        self.friendsOfFriendLbl = Label(self.outputLabelframe, text="Friends of friends")
        self.friendsOfFriendLbl.grid(column=1, row=0)
        self.friendsOfFriendsScroll = scrolledtext.ScrolledText(self.outputLabelframe,width=20,height=15)
        self.friendsOfFriendsScroll.grid(column=1,row=1)
        self.friendsOfFriendsScroll.configure(state='disabled')
        ##specify sugggested friend label and scrolled text
        self.suggestedFriendLbl = Label(self.outputLabelframe, text="Suggested friends")
        self.suggestedFriendLbl.grid(column=2, row=0)
        self.suggestedFriendsScroll = scrolledtext.ScrolledText(self.outputLabelframe,width=20,height=15)
        self.suggestedFriendsScroll.grid(column=2,row=1)
        self.suggestedFriendsScroll.configure(state='disabled')
        
        ##sepecify get data button 
        self.padlbl3 = Label(self.inputLabelFrame, text="")
        self.padlbl3.grid(column=1, row=3)
        self.getDataBtn = Button(self.inputLabelFrame, text="Get data", bg="#64dd17", fg="white", command=self.clicked,width=15)
        self.getDataBtn.grid(column=1, row=4)

        ##specify quit button 
        self.padlbl4 = Label(self.window, text=" ")
        self.padlbl4.grid(column=0, row=3)
        self.quitBtn = Button(self.window, text="Reset", bg="#ff6d00", fg="white", command=self.reset,width=10)
        self.quitBtn.grid(column=0, row=4)
        
    def clicked(self):
        chosenID=int(self.comboIDs.get())
        if(self.directFriendVar.get()==1):
            self.directFriendsScroll.configure(state='normal')
            self.directFriendsScroll.delete('1.0', END)
            directFriends=self.processDataObj.get_direct_friends(chosenID)
            if(len(directFriends)>0):
                text=""
                for i,ID in enumerate(directFriends):
                    personObj=self.processDataObj.get_person_from_id(ID)
                    text+="id:"+str(ID)+"\n"+"FirstName:"+personObj.get_firstName()+"\n"+ \
                    "surname:"+personObj.get_surname()+"\n"
                    if(i<(len(directFriends)-1)): ## to prevent printing line after last person
                        text+="--------------"+"\n"
                self.directFriendsScroll.insert(INSERT,text)
            else:
                self.directFriendsScroll.insert(INSERT,"None")
            self.directFriendsScroll.configure(state='disabled')
        else:
            self.directFriendsScroll.configure(state='normal')
            self.directFriendsScroll.delete('1.0', END)
            self.directFriendsScroll.configure(state='disabled')


        if(self.friendsOfFriendVar.get()==1):
            self.friendsOfFriendsScroll.configure(state='normal')
            self.friendsOfFriendsScroll.delete('1.0', END)
            friendsOfFriends=self.processDataObj.get_friends_of_friends(chosenID)
            if(len(friendsOfFriends)>0):
                text=""
                for i,ID in enumerate(friendsOfFriends):
                    personObj=self.processDataObj.get_person_from_id(ID)
                    text+="id:"+str(ID)+"\n"+"FirstName:"+personObj.get_firstName()+"\n"+ \
                    "surname:"+personObj.get_surname()+"\n"
                    if(i<(len(friendsOfFriends)-1)): ## to prevent printing line after last person
                        text+="--------------"+"\n"
                self.friendsOfFriendsScroll.insert(INSERT,text)
            else:
                self.friendsOfFriendsScroll.insert(INSERT,"None")
            self.friendsOfFriendsScroll.configure(state='disabled')
        else:
            self.friendsOfFriendsScroll.configure(state='normal')
            self.friendsOfFriendsScroll.delete('1.0', END)
            self.friendsOfFriendsScroll.configure(state='disabled')

        if(self.suggestedFriendVar.get()==1):
            self.suggestedFriendsScroll.configure(state='normal')
            self.suggestedFriendsScroll.delete('1.0', END)
            suggestedFriends=self.processDataObj.get_suggested_friends(chosenID)
            if(len(suggestedFriends)>0):
                text=""
                for i,ID in enumerate(suggestedFriends):
                    personObj=self.processDataObj.get_person_from_id(ID)
                    text+="id:"+str(ID)+"\n"+"FirstName:"+personObj.get_firstName()+"\n"+ \
                    "surname:"+personObj.get_surname()+"\n"
                    if(i<(len(suggestedFriends)-1)): ## to prevent printing line after last person
                        text+="--------------"+"\n"
                self.suggestedFriendsScroll.insert(INSERT,text)
            else:
                self.suggestedFriendsScroll.insert(INSERT,"None")
            self.suggestedFriendsScroll.configure(state='disabled')
        else:
            self.suggestedFriendsScroll.configure(state='normal')
            self.suggestedFriendsScroll.delete('1.0', END)
            self.suggestedFriendsScroll.configure(state='disabled')
    
    def reset(self):
        self.comboIDs.current(0)
        self.directFriendVar.set(0)
        self.friendsOfFriendVar.set(0)
        self.suggestedFriendVar.set(0)
        self.directFriendsScroll.configure(state='normal')
        self.directFriendsScroll.delete('1.0', END)
        self.directFriendsScroll.configure(state='disabled')
        self.friendsOfFriendsScroll.configure(state='normal')
        self.friendsOfFriendsScroll.delete('1.0', END)
        self.friendsOfFriendsScroll.configure(state='disabled')
        self.suggestedFriendsScroll.configure(state='normal')
        self.suggestedFriendsScroll.delete('1.0', END)
        self.suggestedFriendsScroll.configure(state='disabled')

