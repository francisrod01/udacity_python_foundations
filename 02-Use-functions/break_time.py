#!/usr/bin/python3.4

import time
import webbrowser

count = 0
while count < 3:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count += 1

print("Good bye!")
