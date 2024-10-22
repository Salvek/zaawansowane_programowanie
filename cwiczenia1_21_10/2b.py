def number_list(numbers):
    for n in numbers:
        n=n*2  
    return numbers

def number_list2(numbers):
    return [n * 2 for n in numbers]

list = (1,2,3,4,5)

number_list(list)