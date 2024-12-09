import time

class PomodoroTimer:
    def __init__(self):
        self.duration = 0

    def set_duration(self, duration: int):
        self.duration = duration
    
    def start_timer(self):
        if self.duration <= 0:
            print("Timer duration is not set or invalid.")
            return
    
        print(f"Timer started for {self.duration} minutes. Stay focused!")
        time.sleep(self.duration * 3)
        print("Time's up! Take a break.")