# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def two_list_cube(list1,list2):
    combo_list = list1+list2
    no_duplicate=list(set(combo_list))
    final_list = [elem ** 3 for elem in no_duplicate]
    return final_list

print(two_list_cube([1,2,3],[3,4,5]))
