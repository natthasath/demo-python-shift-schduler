import calendar

def show_calendar(year, month):
    # Display the calendar
    cal = calendar.monthcalendar(year, month)

    # Get the month and year as strings
    month_str = calendar.month_name[month]
    year_str = str(year)

    # Print the header
    print(f"Calendar for {month_str} {year_str}")
    print("-----------------------------")

    # Print the days of the week
    print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")

    # Print each week's row
    for week in cal:
        row = ""
        for day in week:
            if day == 0:
                # Print a blank space for days outside the month
                row += "     "
            else:
                # Print the day right-aligned
                row += f"{day:2d}   "
        print(row)

# Example usage: display calendar for July 2023
show_calendar(2023, 7)
