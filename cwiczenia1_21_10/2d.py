# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

def every_other_list(list):
    for i in list:
        if(i%2!=0):
            print(i)

list = (1,2,3,4,5,6,7,8,9,10)
every_other_list(list)
