import time
from datetime import datetime
import threading

class Reminder:
    def __init__(self):
        self.events = []  # List of tuples: (event_name, event_time)
        self.lock = threading.Lock()

    def add_event(self, name, time_obj):
        with self.lock:
            self.events.append((name, time_obj))
            self.events.sort(key=lambda x: x[1])  # Keep events sorted by time

    def view_events(self):
        if not self.events:
            print("No upcoming events.")
            return
        print("\nUpcoming Events:")
        with self.lock:
            for i, (name, time_obj) in enumerate(self.events, 1):
                print(f"{i}. {name} at {time_obj.strftime('%Y-%m-%d %H:%M')}")

    def run_reminders(self):
        while True:
            now = datetime.now()
            with self.lock:
                # Copy the list to avoid modification during iteration
                for event in self.events[:]:
                    name, time_obj = event
                    if now >= time_obj:
                        print(f"\n🔔 Reminder: '{name}' is happening now or soon!")
                        self.events.remove(event)
            time.sleep(30)  # Check every 30 seconds
