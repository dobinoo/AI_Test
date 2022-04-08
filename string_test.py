test_string = "Toto je testovaci string a idem vyskusat ci dokazem spravne vyhladavat stringy"
hladany_string = input()

if hladany_string in test_string:
    print("found")
else:
    print("not_found")
