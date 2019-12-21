import classes
from classes import *

def main():
	processDataObj=ProcssData("data.json")
	if(not(processDataObj.get_length_of_hashTable()==0)):#file exist 
		window = Tk()
		a=SocialAppGUI(window,processDataObj)
		window.mainloop()
		
main()