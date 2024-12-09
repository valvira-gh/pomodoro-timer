from timer import PomodoroTimer
from ui import PomodoroUI

def main():
    ui = PomodoroUI()
    timer = PomodoroTimer()

    while True:
        ui.display_menu()
        choice = ui.get_user_choice()

        if choice == 1:
            duration = ui.prompt_for_duration()
            if duration is not None:
                timer.set_duration(duration)
                timer.start_timer()
        elif choice == 2:
            ui.display_message("Under construction...")
        elif choice == 0:
            ui.display_message("Exiting the application. Goodbye!")
            break
        else:
            ui.display_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()