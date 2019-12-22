# social-media-group
## Overview:
This social media APP is python APP for a group of people, in form of a social graph.Each person has one or more connections to groups.
Dataset of persons provided in (data.json) file and represents databse for group of people.
This app provides functionality to choose person by its ID and display the following information:

- Direct friends: those people who are directly connected to the chosen user.
- Friends of friends: those who are two steps away from the chosen user but not directly connected to the chosen user.
- Suggested friends: people in the group who know 2 or more direct friends of the chosen user but are not directly connected to the chosen user.


## System requirement:
- Windows or Ubuntu
- Python3 

## How to run program:
- Download code by this command `git clone https://github.com/AhmedSYD/Social-Network-APP`
- Run program by 3 different methods:
  - Run `main.exe` file.(note: you should run this file on Windows platform)
  - You can run code also by this command `python main.py` or `python3 main.py`
  - I write the same full code on jupyter notebook in `social_network_app_notebook.ipynb` file .you can open it and start running each cell in it

## How to use program:
![gui1](https://user-images.githubusercontent.com/26576895/71326980-34dd2e80-250b-11ea-97a4-dd9978e65651.JPG)

- At first, you should choose any user ID.
- Second, choose type of friends you want to show.
- Then, click on `Get data` button. 
- At the end, you will show person information in output label frame for each type of friends.
(Note: I seperate each friend information from another by line.)

## Demo:
- You can find demo video for this program at this [**Link**](https://www.youtube.com/watch?v=fDFSyp87r7U)

