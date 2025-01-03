def create_timetable():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    timetable = {}

    print("Create your weekly timetable!")
    for day in days:
        print(f"\nEnter the schedule for {day}:")
        subjects = []
        for i in range(1, 7):  # Assuming six periods a day
            subject = input(f"  Period {i}: ")
            subjects.append(subject)
        timetable[day] = subjects

    return timetable

def display_timetable(timetable):
    print("\nYour Weekly Timetable:")
    print("-" * 50)
    for day, subjects in timetable.items():
        print(f"{day}: {', '.join(subjects)}")

# Main Program
if __name__ == "__main__":
    weekly_timetable = create_timetable()
    display_timetable(weekly_timetable)
