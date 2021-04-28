

def add(string):
    if string == "":
        return 0
    if string[0:2] == "//":
        delimiter = find_delimiter(string)
        string = string[4:]
        numbers = string.replace(delimiter,' ').split()
    else:
        numbers = string.replace("\n", " ").replace(",", " ").split()
    # numbers = ["-1", "2", "3"]    
    numbers_list = []
    for char in numbers:
        numbers_list.append(int(char))
    # numbers_list = [-1, 2, 3]
    negative_numbers_list = find_negative_numbers(numbers_list)
    if len(negative_numbers_list) > 0:
        negative_numbers_string = ""
        for number in negative_numbers_list:
            negative_numbers_string += str(number)
        message = "Negatives not allowed: " + negative_numbers_string
        return message
    return sum(numbers_list)


def find_delimiter(string):
    double_slash = string[0:2]
    delimiter = string[2]
    end_delimeter = string[3]
    return delimiter

def find_negative_numbers(numbers_list):
    negative_numbers = []
    for num in numbers_list:
        if num <0:
            negative_numbers.append(num)
    return negative_numbers







