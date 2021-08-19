# Spotify-Music-Recommendations-Private
Welcome to The Spotify Algorithm Playlist maker!
First things first known bugs:
1. When running the Spotify_login file 2 of the same webpage will open
2. If you try to add 40 songs to a playlist sometimes a little less (like 38) will be added. I believe this is actually a bug with Spotify's api
and not my fault from the testing I have done at least thats the story I am going with
3. There is currently no way to remove songs artists or genres. If you need to do so restart the program its way easier than programming that in
also I wanted to give this to Joey before he left for college and I am on a limited time schedule. I say this having 4.5 hours knowing well I am just
too lazy
4. The interface has not been tested on other computers. For all I know it may not work at all. This means there will probably be numerous
weird looking things in the interface but it looks trash anyways so who cares.

Now that the bug info is out of the way I will leave you with the instructions of how to get this baby working.
Good Luck you are going to need it

***Note if Anthony has not whitelisted your spotify account nothing will work make sure he does this and doesn't forget

1. Install the required packages using the command pip install -r requirements.txt (on mac it may be pip3 install -r requirements.txt). To do this you either need to navigate to the directory in command prompt or type in the path of the requirements file like this pip install -r C:\Users\Owner\Desktop\Spotify_Reccommendations\requirements.txt.
An easy way to do this on windows is to open the folder with all of the code click on the folder bar which shows the folders you are in and type cmd and press enter. This will bring up a command prompt window that has opened this folder on your computer and you can simply copy and paste pip install -r requirements.txt. If you are on mac look up a tutorial if you need it or manually install the like 3 packages. 
2. Open the Credentials JSON file and enter your spotify username like this: 
"User_id": "Username"
3. Run the Spotify_Login file. This will take you to a webpage where you need to log in with your spotify account info
4. After this is done it should show a webpage that says success. You can exit this and never need to run it again.
5. Run the app file and hope everything works.

Please report all bugs you find to the creator there is still a lot of work to do and its way easier to give out a half working bug ridden program
and have users debug it for me rather than spending the time myself.
Also if you try and break it you probably will. Do with that what you want.
