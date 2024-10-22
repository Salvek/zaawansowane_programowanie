# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def is_ab_bigger(a: int, b: int, c: int) -> int:
    if(a+b>=c):
        return True
    else:
        return False
    
