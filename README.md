# net_connection_tester
src for a basic internet connection testing app

Steps for using the widget/app:
#1  The src is given which needs to be processed to exe
       -> Here's how: https://www.geeksforgeeks.org/convert-python-script-to-exe-file/
  
#2  create a folder named "files" in the same directory as the main application.exe directory (connection_tester.exe)
#3  paste an mp3 file inside the "files" folder
       -> this will play if there is an active net connection
       
#4  rename it to "SYT.mp3"
#5  Run connection_tester.exe
      -> a console will open and keep printing "trying to PING" if there is no connection
      -> if there's an active connection or if the connection comes back, the program will print "Net Ashche!"
         and start playing SYT.mp3
