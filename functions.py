import requests
import re


def get_file(url):
    """ reads file from url"""
    response = requests.get(url)
    data = response.text

    return data


def get_file_sample(filepath):
    """ sample function for testing the code with local file"""
    with open(filepath, 'r+') as f:
        lines = f.readlines()
        
        return lines


def display_average_steps(file_lines):
    # read file, and clean lines with regex
    lines = [re.search(r'\d+', line.strip()).group() for line in file_lines]

    months = list(('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))

    days = list((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    steps = {}

    for day, month in zip(days, months):
        monthly_steps = []
        for count in range(day):
            # create list of steps taken each month
            monthly_steps.append(int(lines[count]))

        # average steps per month
        average_steps = int(sum(monthly_steps) / day )
        steps.setdefault(month, average_steps)
    
    return steps



# if __name__ == "__main__":
#     print(display_average_steps())
