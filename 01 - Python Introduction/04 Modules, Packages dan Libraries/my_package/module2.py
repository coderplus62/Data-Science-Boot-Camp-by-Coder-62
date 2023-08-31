def kali(a, b):
    """Mengembalikan hasil perkalian dua bilangan."""
    return a * b

def bagi(a, b):
    """Mengembalikan hasil dari pembagian dua bilangan."""
    if b != 0:
        return a / b
    else:
        return "Tidak dapat dibagi dengan nol"
