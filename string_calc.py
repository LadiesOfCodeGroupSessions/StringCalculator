

def add(string):
    if string == "":
        return 0
    if string[0:2] == "//":
        delimiter = find_delimiter(string)
        string = string[4:]
        numbers = string.replace(delimiter,' ').split()
    else:
        numbers = string.replace("\n", " ").replace(",", " ").split()
    num = []
    for char in numbers:
        num.append(int(char))
    return sum(num)


def find_delimiter(string):
    double_slash = string[0:2]
    delimiter = string[2]
    end_delimeter = string[3]
    return delimiter

def find_negative_number(string):
    negative_number = " "
    for char in string:
        if char == :
            char.join(negative_number)
            print(f"Negatives not allowed{negative_number}")
            return negative_number







