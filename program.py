from functions import display_average_steps, get_file, get_file_sample
import pprint

def program():
    # read file
    lines = get_file_sample('steps.txt')

    # calculate average steps
    average_steps = display_average_steps(lines)
    print(f'\nThese are your average steps for this year\n')
    print(list(average_steps.items()))



if __name__ == "__main__":
    program()