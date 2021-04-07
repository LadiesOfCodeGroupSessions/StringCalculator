

def add(string):
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(int(char))
    return sum(numbers)


