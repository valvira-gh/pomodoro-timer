class PomodoroUI:
    def display_menu(self):
        print("*** POMODORO TIMER ***")
        print("1. Set and start Pomodoro timer")
        print("2. View saved data (not implemented yet)")
        print("0. Exit")
        print()
    
    def get_user_choice(self):
        try:
            return int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            return None
    
    def display_message(self, message: str):
        print(message, end="\n" * 2)
    
    def prompt_for_duration(self):
        try:
            return int(input("Enter focus duration in minutes: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            return None