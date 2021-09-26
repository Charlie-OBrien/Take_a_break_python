import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(1800) #30 minutes
    #time.sleep(10)  # <- for debug and testing 10 seconds
    webbrowser.open('https://www.youtube.com/watch?v=b-dfCIjYs0s')
    #print("Take a break!") # <- for debug and testing
    break_count = break_count + 1