from playsound import playsound
import time

# write formatting & clearing code
CLEAR = '\033[2J'
CLEAR_AND_RETURN = '\033[H'

# defining focus function
def focus(minutes):
    alarm_time_elapsed = 0
    seconds = minutes*60

    print(CLEAR)
    while alarm_time_elapsed < seconds:
        time.sleep(1)
        alarm_time_elapsed += 1

        alarm_time_left = seconds - alarm_time_elapsed
        alarm_minutes_left = alarm_time_left//60
        alarm_seconds_left = alarm_time_left%60
        print(f'{CLEAR_AND_RETURN}{'focus|'}{alarm_minutes_left:02d}:{alarm_seconds_left:02d}')
    playsound('rest.mp3') # rest.mp3 because we want to become chill for the break ;)

# defining rest function
def rest(minutes):
    wait_time_elapsed = 0
    seconds = minutes*60

    print(CLEAR)
    while wait_time_elapsed < seconds:
        time.sleep(1)
        wait_time_elapsed += 1

        wait_time_left = seconds - wait_time_elapsed
        wait_minutes_left = wait_time_left//60
        wait_seconds_left = wait_time_left%60
        print(f'{CLEAR_AND_RETURN}{'rest|'}{wait_minutes_left:02d}:{wait_seconds_left:02d}')
    playsound('focus.mp3') # focus.mp3 because we want to become hyped for the next focus session;)

# assembling pomodoro function
def pomodoro(focus_time, rest_time, cycles):
    n = 0

    while n < cycles:
        focus(focus_time)
        rest(rest_time)
        n += 1
    return

# insert your preferred focus time (minutes), rest time (minutes) and cycles
pomodoro(25,5,3)