

def add(string):
    if string == "":
        return 0
    numbers = string.replace('\n',' ').replace(',',' ').split()
    num = []
    for char in numbers:
        num.append(int(char))
    return sum(num)









