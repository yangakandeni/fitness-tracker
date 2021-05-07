import requests, urllib

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

if __name__ == "__main__":
    # print(get_file("http://lib.stat.cmu.edu/datasets/boston"))
    lines = get_file_sample('steps.txt')
    for line in lines:
        print(line.strip())


