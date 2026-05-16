import time 

def countdown(t, msg = "Done!"):
    while t:
        mins, secs, = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    print(msg)

def cli_countdown(): 
    t = input("Enter time in seconds: ")
    countdown(int(t))

cli_countdown()
