#!/bin/bash

# adb tcpip 5555
 
adb connect 25.79.227.245

 adb shell input keyevent 82 && adb shell input swipe 200 900 200 300 && adb shell input text 78569 && adb shell input keyevent 66

