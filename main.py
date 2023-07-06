import random

def assign_shifts(employees, shifts):
    schedule = {}

    for shift in shifts:
        # Shuffle the employees list to randomize the order
        random.shuffle(employees)

        for employee in employees:
            if employee['availability'][shifts.index(shift)]:
                schedule[shift] = employee['name']
                employee['availability'][shifts.index(shift)] = False
                break

    return schedule


# Example data
employees = [
    {'name': 'Alice', 'availability': [True, True, False, True, False, True, False]},  # Example availability: [Mon, Tue, Wed, Thu, Fri, Sat, Sun]
    {'name': 'Bob', 'availability': [True, False, True, False, True, False, True]},
    {'name': 'Carol', 'availability': [False, True, True, True, False, True, False]},
    {'name': 'Dave', 'availability': [True, False, True, False, True, False, True]},
]

shifts = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Assign shifts to employees
schedule = assign_shifts(employees, shifts)

# Print the schedule
for shift, employee in schedule.items():
    print(f"{shift}: {employee}")
