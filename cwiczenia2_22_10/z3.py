# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def is_even(a):
    if(a%2==0):
        b = True
    else:
        b = False

    if(b==True):
        print('Ta liczba jest parzysta')
    else:
        print('Ta liczba nie jest parzysta')
    
is_even(123456782)