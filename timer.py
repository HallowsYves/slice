import time

from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

def run_timer(minutes):
    total_seconds = minutes * 60

    with Progress(TextColumn("[progress.description]{task.description}"),BarColumn(),TimeRemainingColumn(),) as progress:
        pomo_bar = progress.add_task(f"Pomo", total=total_seconds)
        for x in range(total_seconds, 0, - 1):
            seconds = x % 60
            minutes = int(x / 60)
            progress.update(pomo_bar, advance=1)
            time.sleep(1)
    print("\nBreak Time!")

pomo_length = int(input("Pomodoro Length: "))
run_timer(pomo_length)