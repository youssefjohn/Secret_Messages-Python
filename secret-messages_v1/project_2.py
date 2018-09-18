

def main_menu():
    print("Hi welcome to the Secret Message sender!")
    print("You're going to be asked a few questions, please answer them to proceed")
    print("If you would like to quit, please just press Q or type 'quit' followed by enter to exit.")


    while True:


        message = input("What is your message? ").lower()

        user_choice = input("So would you like to Encrypt your message, or Decrypt? "
                                   "Please type in the exact purpose:  ").lower()


        if user_choice == "q" or user_choice == "quit":
            sys.exit("Goodbye")

        elif user_choice != "encrypt" and user_choice != "decrypt":
            print("That isnt valid, please try again")

        else:
            double_check = input(f" Ok got it, you would like to {user_choice}, is that right? y/n").lower()
            if double_check == 'y':
                sub_menu(message, user_choice)

            else:
                continue



def sub_menu(message, user_choice):
    list_of_ciphers = ["Keyword", "Atbash", "ADFGVX"]
    display_ciphers = [thing for thing in list_of_ciphers]
    while True:

        print(f"Ok thats great, now lets move on to our next step. Please choose which Cipher you would like to use out of: {' / '.join(display_ciphers)} ")

        cipher_choice = input("> ").lower()

        if cipher_choice == 'keyword' and user_choice == 'encrypt':
            new_user = ciphers.Keyword()
            new_user.encrypt(message)
            sys.exit("Good luck comrade!")


        elif cipher_choice == 'atbash' and user_choice == 'encrypt':
            new_user = ciphers.Atbash()
            new_user.encrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'adfgvx' and user_choice == 'encrypt':
            break

        elif cipher_choice == 'keyword' and user_choice == 'decrypt':
            new_user = ciphers.Keyword()
            new_user.decrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'atbash' and user_choice == 'decrypt':
            new_user = ciphers.Atbash()
            new_user.decrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'adfgvx' and user_choice == 'decrypt':
            break

        else:
            print("sorry I don't recognise that value, please try again")
            continue






main_menu()




