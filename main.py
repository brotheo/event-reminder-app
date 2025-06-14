import threading
from reminder import Reminder
from datetime import datetime

def show_menu():
    print("\n--- Event Reminder ---")
    print("1. Add event reminder")
    print("2. View events")
    print("3. Exit")

def main():
    reminder = Reminder()
    reminder.load_events()  # Load any saved events (optional if implemented)

    # Start reminder thread to check and alert asynchronously
    reminder_thread = threading.Thread(target=reminder.run_reminders, daemon=True)
    reminder_thread.start()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            event_name = input("Enter event name: ").strip()
            date_str = input("Enter event date and time (YYYY-MM-DD HH:MM): ").strip()

            try:
                event_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                if event_time <= datetime.now():
                    print("Event time must be in the future.")
                    continue
                reminder.add_event(event_name, event_time)
                print(f"Event '{event_name}' scheduled for {event_time}")
            except ValueError:
                print("Invalid date/time format. Please use YYYY-MM-DD HH:MM")

        elif choice == "2":
            reminder.view_events()

        elif choice == "3":
            print("Exiting Event Reminder.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
