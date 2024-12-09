from timer import PomodoroTimer
def main():
    print("*** POMODORO TIMER ***")

    try:
        timer = PomodoroTimer()
        timer.add_duration()
    except ValueError:
        print("Enter an integer number.")
        pass


if __name__ == "__main__":
    main()