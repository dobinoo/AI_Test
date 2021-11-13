import time

while True:
        user_input = input()
        time.sleep(3)

        if user_input == "exit":
            exit()

        print(user_input + "\n")
