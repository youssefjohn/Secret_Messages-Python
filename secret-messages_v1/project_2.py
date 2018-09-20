import ciphers
import sys

def main_menu():
    ''' THIS IS THE MAIN BODY.
        IT RUNS THE INITIAL MESSAGES/INPUTS TO THE USER.'''

    print("Hi welcome to the Secret Message sender! "
          "You're going to be asked a few questions. "
          "Please answer them to proceed.\n"
          "If you would like to quit, "
          "please just press Q or type 'quit' "
          "followed by enter to exit. ")

    while True:
        '''THIS WHILE LOOP IS IN PLACE TO GAIN ANSWERS FROM THE USER,
           IT PROMPTS THE USER TO GIVE A MESSAGE,
           ENCRYPT OR DECRYPT IT, THEN DOUBLE CHECKS IF THEY
           ARE HAPPY WITH THEIR CHOICE.

           ONCE IT HAS ALL 3 ANSWERS, IT RUNS THE SUB_MENU FUNCTION.
        '''

        message = input("What is your message? ").lower()

        user_choice = input("So would you like to "
                            "Encrypt your message, or Decrypt? "
                            "Please type in the exact purpose:  ").lower()

        if user_choice == "q" or user_choice == "quit":
            sys.exit("Goodbye")

        elif user_choice != "encrypt" and user_choice != "decrypt":
            print("That isnt valid, please try again")

        else:
            double_check = input(f" Ok got it, you would like to"
                                 "{user_choice}, is that right? y/n").lower()
            if double_check == 'y':
                # clear()
                sub_menu(message, user_choice)

            else:
                continue


def sub_menu(message, user_choice):
    ''' THIS IS THE SUB_MENU. IT PRESENTS THE USER WITH"
        A LIST OF CIPHERS TO ENCRYPT OR DECRYPT THEIR CODE WITH.
        IT RUNS A FEW CHECKS TO MAKE SURE EVERYTHING IS CORRECT,
        THEN RUNS THE CHOSEN CIPHER. '''

    list_of_ciphers = ["Keyword", "Atbash", "Affine"]
    display_ciphers = [thing for thing in list_of_ciphers]
    while True:

        print("Ok thats great, now lets move on to our next step. "
              "Please choose which Cipher you would "
              f"like to use out of: {' / '.join(display_ciphers)} ")

        cipher_choice = input("> ").lower()

        if cipher_choice == 'keyword' and user_choice == 'encrypt':
            new_user = ciphers.Keyword()
            new_user.encrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'atbash' and user_choice == 'encrypt':
            new_user = ciphers.Atbash()
            new_user.encrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'affine' and user_choice == 'encrypt':
            new_user = ciphers.Affine()
            new_user.encrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'keyword' and user_choice == 'decrypt':
            new_user = ciphers.Keyword()
            new_user.decrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'atbash' and user_choice == 'decrypt':
            new_user = ciphers.Atbash()
            new_user.decrypt(message)
            sys.exit("Good luck comrade!")

        elif cipher_choice == 'affine' and user_choice == 'decrypt':
            new_user = ciphers.Affine()
            new_user.decrypt(message)
            sys.exit("Good luck comrade!")

        else:
            print("sorry I don't recognise that value, please try again")
            continue

main_menu()
