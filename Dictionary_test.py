word_list ={"futbal" : ["brankar", "gula", "lopta", "futbalista", "hrac", "rozhodca", "trener"],
            "spanok": ["postel", "pyzamo", "budik", "spanok"]}

#user_input = input()
#print(word_list["futbal"])
#print(len(word_list))
search_value = "futbalista"

for key, value in word_list.items():
    for word in value:
        if word == search_value:
            print(key)
