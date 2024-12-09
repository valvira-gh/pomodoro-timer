import time

class PomodoroTimer:
    def __init__(self):
        self.duration = 0

    def add_duration(self):
        print("How many minutes you want to focus?")
        self.duration = int(input("Minutes: "))
        print()
        print(f"Timer is set to {self.duration}")


    def __str__(self):
        return f"Timer is set to {self.duration} minutes."


if __name__ == "__main__":
    # test cases
    timer = PomodoroTimer()
    timer.add_duration()
    print(timer)
