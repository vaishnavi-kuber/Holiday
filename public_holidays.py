from datetime import datetime, timedelta

# Major US holidays in the second half of 2026 (July through December)

def get_holidays_2026():
    holidays = [
        {"name": "Independence Day", "date": "July 04, 2026", "day": "Saturday"},
        {"name": "Labor Day", "date": "September 07, 2026", "day": "Monday"},
        {"name": "Columbus Day", "date": "October 12, 2026", "day": "Monday"},
        {"name": "Veterans Day", "date": "November 11, 2026", "day": "Wednesday"},
        {"name": "Thanksgiving", "date": "November 26, 2026", "day": "Thursday"},
        {"name": "Christmas Day", "date": "December 25, 2026", "day": "Friday"}
    ]
    return holidays

if __name__ == "__main__":
    print("Holidays in the Second Half of 2026:\n")
    for holiday in get_holidays_2026():
        print(f"- **{holiday['name']}** - {holiday['date']} ({holiday['day']})")