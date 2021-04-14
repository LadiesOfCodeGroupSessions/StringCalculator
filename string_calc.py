

def add(string):
    if string == "":
        return 0
    numbers = string.split(",")
    #map_numbers = map(int, numbers)
    #return sum(map_numbers)
    num = []
    for char in numbers:
        num.append(int(char))
    #     if char.isdigit():
    #         numbers.append(int(char))
    # return sum(numbers)
    return sum(num)








