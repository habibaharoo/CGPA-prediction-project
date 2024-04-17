from tabulate import tabulate
from colorama import Fore, Back, Style, init

init(autoreset=True)

# Collect course and GPA data
course_data = []
for i in range(1, 6):
    course_name = input(f"Enter Name of Course {i}: ")
    credit = float(input(f"Enter Credit of Course {i}: "))
    desired_gpa = float(input(f"Enter desired GPA of Course {i}: "))

    # Validate inputs
    if credit <= 0 or desired_gpa < 0 or desired_gpa > 4.0:
        print("Invalid input. Credits should be positive, and GPA should be between 0.0 and 4.0.")
        exit()

    course_data.append([course_name, credit, desired_gpa])

# Calculate total credits and GPA
credits = sum(course[1] for course in course_data)
total_GP = sum(course[1] * course[2] for course in course_data)
GPA = total_GP / credits

# Create a tabulated string
table_data = [list(map(str, row)) for row in course_data]
table_data.append(["Total", credits, ""])
table_data.append(["GPA", "", round(GPA, 2)])

# Define headers and column alignments
headers = ["Course Name", "Credit", "Desired GPA"]
col_alignments = ["left", "center", "center"]

# Display the table with colorization for all rows
for i, row in enumerate(table_data):
    if i == len(table_data) - 2:  # Highlight Total row
        print( Back.YELLOW + Style.BRIGHT + tabulate([row], headers, tablefmt="fancy_grid", colalign=col_alignments, numalign="center",stralign="center", disable_numparse=True))

    elif i == len(table_data) - 1:  # Highlight GPA row
        print(Back.YELLOW + Style.BRIGHT + tabulate([row], headers, tablefmt="fancy_grid", colalign=col_alignments, numalign="center", stralign="center", disable_numparse=True))

    else:
        # Alternate row colors for the upper table
        color = Back.GREEN if i % 2 == 0 else Back.CYAN
        print(Fore.BLACK + tabulate([row], headers, tablefmt="fancy_grid", colalign=col_alignments, numalign="center", stralign="center", disable_numparse=True).replace('\n', f'{Style.RESET_ALL}\n{color}'))
