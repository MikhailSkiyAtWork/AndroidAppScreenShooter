# AndroidAppScreenShooter
In order to use this script it is necessary to install Android SDK and AndroidViewClient library

Links:
Android SDK http://developer.android.com/sdk/index.html

AndroidViewClient https://github.com/dtmilano/AndroidViewClient (necessary to download it as zip)

Installation AndroidViewClient https://github.com/dtmilano/AndroidViewClient/wiki

Install Python Image Library http://stackoverflow.com/a/29438193/1462969

After this, the PATH should be created 
Add variable into PATH http://hathaway.cc/post/69201163472/how-to-edit-your-path-environment-variables-on-mac
What should be added
/Users/Mikhail/Library/Android/sdk/build-tools/22.0.1
/Users/Mikhail/Library/Android/sdk/tools
/Users/Mikhail/Library/Android/sdk/platform-tools
In your case it may be another PATH, but the idea is to add PATH where you SDK tools are located

If everything is ok, after this you need to connect your device or emulator with installed application. And now you can
run script in the terminal 
python /Users/Mikhail/PycharmProjects/androidUITest/mymonkey.py

IMPORTNANT. In order to save screenshots in your own location, you need to change location in script mymonkey.py in method makeScreen(name) 

