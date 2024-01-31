
# Example usage
atomic_number = int(input("Enter the atomic number of the element: "))

    # Initialize variables for group and period
group_number = 0
period_number = 1

    # Electronic configuration filling pattern
filling_pattern = [2, 8, 8, 18, 18]

    # Determine period number
while atomic_number > sum(filling_pattern):
    period_number += 1
    filling_pattern.append(18)

    # Determine group number within the period
for electrons_in_shell in filling_pattern:
    group_number += 1
    if atomic_number <= electrons_in_shell:
        break
    atomic_number -= electrons_in_shell

print("Group Number: ", group_number, "Period Number:", period_number)