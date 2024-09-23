from playsound import playsound
import time

# write some formatting & clearing code
CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

# write main body for the alarm clock
def alarm(hours, minutes, seconds):
    seconds_converted = hours*3600 + minutes*60 + seconds
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds_converted:
        time.sleep(1)
        time_elapsed = time_elapsed + 1

        time_left = seconds_converted - time_elapsed
        hours_left = time_left // 3600
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f'{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}')
        
    playsound('alarmclock.mp3')

# ask user how long before alarm
hours = int(input('hours: '))
minutes = int(input('minutes: '))
seconds = int(input('seconds: '))

# sound tha alarm
alarm(hours,minutes,seconds)
