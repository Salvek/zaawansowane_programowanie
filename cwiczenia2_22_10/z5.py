# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def is_in_list(list, num):
    return num in list 

list = [1, 2, 3, 4, 5]
num = 3

print(is_in_list(list, num))