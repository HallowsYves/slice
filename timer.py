import time

def run_timer(minutes):
    total_seconds = minutes * 60
    for x in range(total_seconds, 0, - 1):
        seconds = x % 60
        minutes = int(x / 60)
        print(f"{minutes:02}:{seconds:02}", end='\r')
        time.sleep(1)
    print("\nBreak Time!")

pomo_length = int(input("Pomodoro Length: "))
run_timer(pomo_length)