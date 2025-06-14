# Event Reminder App

A simple command-line Python application to schedule event reminders and notify you when they occur.

---

## Features

- Add event reminders with a name and a specific date/time  
- View upcoming scheduled events  
- Asynchronous reminder alerts when events occur  
- Simple, user-friendly command-line interface  

---

## Requirements

- Python 3.x  
- Uses only built-in modules (`datetime`, `time`, `threading`) — no external dependencies

---

## Project Structure
![Screenshot 2025-06-14 075318](https://github.com/user-attachments/assets/a1e3d9d2-b3d5-4e7c-9db2-393f3b0f1537)


---

## How to Run

1. Download or clone the project files.  
2. Open a terminal or command prompt in the project directory.  
3. Run the app using:

```bash
python main.py
--- Event Reminder ---
1. Add event reminder
2. View events
3. Exit
Choose an option: 1
Enter event name: Doctor Appointment
Enter event date and time (YYYY-MM-DD HH:MM): 2025-06-15 14:30
Event 'Doctor Appointment' scheduled for 2025-06-15 14:30

Choose an option: 2

Upcoming Events:
1. Doctor Appointment at 2025-06-15 14:30

...

🔔 Reminder: 'Doctor Appointment' is happening now or soon!


