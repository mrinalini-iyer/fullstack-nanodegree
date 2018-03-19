# Take a break program.
# Step1: Wait for 2 hours
# Step 2: Open browser
# Repeat - 3 times
import webbrowser
import time

#time.sleep(2 * 60 * 60)
break_count = 3
count = 0

print('Take a break program started %f seconds'.format(time.time))
while break_count > 0:
    # stops program execution
    # functions abstract exact execution
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=3iDxU9eNQ_0")
    break_count-=1

print('Take a break program complete %f seconds'.format(time.time))
