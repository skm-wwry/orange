@echo off
:1
echo "start"
tasklist|find /i "AutoDoor"||start C:\Users\cjfre\Desktop\AutoDoor.exe
ping/n 3 127.1>nul
goto 1
