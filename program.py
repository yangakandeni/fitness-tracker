import pprint

from functions import display_average_steps, get_file, get_file_sample, display_menu

def program():
    # read file
    lines = get_file_sample('steps.txt')

    # calculate average steps
    average_steps = display_average_steps(lines)
    print(f'\nWELCOME TO YOUR FITNESS TRACKER APP')
    print(f'\nHere is your progress...')
    print(f"\n{''.ljust(10, '*')} MONTH vs STEPS {''.ljust(10, '*')}")
    for month, steps in average_steps.items():
        print(f"\n{''.ljust(10, ' ')} {month} - {steps}", end="")

    print(f"\n\n{''.ljust(38, '*')}\n")

if __name__ == "__main__":
    program()
