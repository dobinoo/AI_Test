# word_list ={"futbal" : ["brankar", "gula", "lopta", "futbalista", "hrac", "rozhodca", "trener", "dvaja treneri", "dvojity utok"],
# "spanok": ["postel", "pyzamo", "budik", "spanok"]}

#user_input = input()
#print(word_list["futbal"])
#print(len(word_list))
#search_value = input()

# for key, value in word_list.items():
#     for word in value:
#         if word == search_value:
#             print(key)

test_string = "Toto je testovaci string a idem vyskusat ci dokazem spravne vyhladavat stringy"
hladany_string = input()

if hladany_string in test_string:
    print("found")
else:
    print("not_found")
