def is_prime(n):
    '''
    verifica daca numarul este prim
    :param n: numar natural
    :return: adevarat sau fals
    '''
    if n<2:
        return False
    else:
        ok=True
        for i in range(2, n//2 + 1):
            if n%i == 0:
                ok=False
    if ok:
        return True
    else:
        return False

def get_goldbach(n):
    '''
    verificam conjectura lui Goldbach
    :param n: numar intreg
    :return: p1 si p2 daca ambele sunt prime si suma lor este egala cu nin cazul lui n par, iar daca numarul este impar p1=2, iar daca si p2=n-p1 este prim se returneaza numererle
    '''
    if n%2 == 1:
        p1=2
        p2=n-2
        if is_prime(p2) == True:
            return p1, p2
    else:
        for p1 in range(2, n//2+1):
            if is_prime(p1) == True:
                p2=n-p1
                if is_prime(p2) == True:
                    return p1,p2

def test_get_goldbach():
    '''
    testam daca functia este corecta
    :return:p1 si p2
    '''
    assert get_goldbach(100) == (3, 97)
    assert get_goldbach(5) == (2, 3)
    assert get_goldbach(7) == (2,5)
    assert get_goldbach(12344) == (43, 12301)
    assert get_goldbach(17) == None

def get_newton_sqrt(n, steps):
    '''

    :param n: numar intreg
    :param steps: numar intreg
    :return: aproximarea radicalului numarului intr-un numar de pasi
    '''
    x0=2
    for i in range (0, steps):
        x0=x0/2+n/(2*x0)
    return x0


def test_get_newton_sqrt():
    '''
    testam daca functia este corecta
    :return: aproximarea radicalului numarului intr-un numar de pasi
    '''
    assert get_newton_sqrt(16, 9) == 4
    assert get_newton_sqrt(12, 3) == 3.4642857142857144
    assert get_newton_sqrt(7, 1) == 2.75
    assert get_newton_sqrt(3, 2) == 1.7321428571428572
    assert get_newton_sqrt(21, 4) == 4.582578583339913


def is_superprime(n):
    '''
    functia verifica daca prefixele numarului sunt prime
    :param n: numar intreg
    :return: adevarat daca toate prefixele numarului sunt prime si fals in caz contrar
    '''
    while n>0:
        if is_prime(n) == False:
            return False
        n=n//10
    return True

def test_is_superprime():
    '''
    testam daca functia este corecta
    :return:adevarat daca  numarul este superprim si fals in caz contrar
    '''
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(13) == True
    assert is_superprime(1237) == False
    assert is_superprime(53) == True


def menu():
    print("Alegeti optiunea:")
    print("1.Conjectura lui Goldbach")
    print("2.Calculul radicalului folosind metoda lui Newton")
    print("3.Numar superprim")
    print("0.Iesire")


def main():
    menu()
    option=int(input("Option"))
    while option != 0:
        if option == 1:
            n=int(input("n="))
            print(get_goldbach(n))
        if option == 2:
            n=int(input("n="))
            steps=int(input("step="))
            print(get_newton_sqrt(n, steps))
        if option == 3:
            n=int(input("n="))
            print(is_superprime(n))

    menu()
    option = int(input("Option="))


if __name__ == '__main__':
    main()

'''
la problema 3 exista solutie pentru orice n numar par mai mare decat 3. 
'''