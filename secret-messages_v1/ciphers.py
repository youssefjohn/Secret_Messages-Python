class Cipher:
    ''' THIS IS THE PARENT CIPHER. IT HAS TWO METHODS THAT
        WILL RAISE AN ERROR IF THEY ARE NOT USED BY
        THE SUBCLASSES.
    '''

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()


class Atbash(Cipher):
    '''THIS IS MY FIRST CIPHER, IT INHERITS FROM THE CIPHER CLASS'''
    def __init__(self):
        '''THIS METHOD INSTANTIATES TWO LISTS OF LETTERS'''

        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                         'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.cipher_alphabet = ['Z', 'Y', 'X', 'W', 'V', 'U',
                                'T', 'S', 'R', 'Q', 'P', 'O',
                                'N', 'M', 'L', 'K', 'J', 'I',
                                'H', 'G', 'F', 'E', 'D', 'C',
                                'B', 'A']

    def encrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND ENCRYPTS
           IT USING THE CIPHER_ALPHABET ATTRIBUTE
        '''

        self.encrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                self.encrypted_text.append(self.cipher_alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.encrypted_text = ''.join(self.encrypted_text)
        print("Here is your Encrypted message:")
        print(self.encrypted_text)

    def decrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND
           DECRYPTS IT USING THE ALPHABET ATTRIBUTE
        '''

        self.decrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.cipher_alphabet:
                index = self.cipher_alphabet.index(letter)
                self.decrypted_text.append(self.alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.decrypted_text = ''.join(self.decrypted_text)
        print("Here is your Decrypted message:")
        print(self.decrypted_text)


class Keyword(Cipher):
    '''THIS IS MY SECOND CIPHER, IT INHERITS FROM THE CIPHER CLASS'''

    def __init__(self):
        '''THIS METHOD INSTANTIATES TWO LISTS OF LETTERS'''

        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                         'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.keyword_alphabet = ['K', 'R', 'Y', 'P', 'T', 'O',
                                 'S', 'A', 'B', 'C', 'D', 'E',
                                 'F', 'G', 'H', 'I', 'J', 'L',
                                 'M', 'N', 'Q', 'U', 'V', 'W',
                                 'X', 'Z']

    def encrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND
           ENCRYPTS IT USING THE KEYWORD_ALPHABET ATTRIBUTE
        '''

        self.encrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                self.encrypted_text.append(self.keyword_alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.encrypted_text = ''.join(self.encrypted_text)
        print("Here is your Enrypted message:")
        print(self.encrypted_text)

    def decrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND DECRYPTS
           IT USING THE ALPHABET ATTRIBUTE
        '''

        self.decrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.keyword_alphabet:
                index = self.keyword_alphabet.index(letter)
                self.decrypted_text.append(self.alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.decrypted_text = ''.join(self.decrypted_text)
        print("Here is your Decrypted message:")
        print(self.decrypted_text)


class Affine:
    '''THIS IS MY THIRD CIPHER, IT INHERITS FROM THE CIPHER CLASS'''
    def __init__(self):
        '''THIS METHOD INSTANTIATES TWO LISTS OF LETTERS'''

        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                         'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R',
                         'S', 'T', 'U', 'V', 'W', 'X',
                         'Y', 'Z']

        self.affine_alphabet = ['I', 'N', 'S', 'X', 'C', 'H',
                                'M', 'R',	'W', 'B', 'G', 'L',
                                'Q', 'V', 'A', 'F', 'K', 'P',
                                'U', 'Z', 'E', 'J', 'O', 'T',
                                'Y', 'D']

    def encrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND ENCRYPTS
           IT USING THE ALPHABET ATTRIBUTE
        '''

        self.encrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                self.encrypted_text.append(self.affine_alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.encrypted_text = ''.join(self.encrypted_text)
        print("Here is your Encrypted message")
        print(self.encrypted_text)

    def decrypt(self, text):
        '''THIS METHOD TAKES IN A USER MESSAGE AND DECRYPTS
           IT USING THE AFFINE_ALPHABET ATTRIBUTE
        '''

        self.decrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.affine_alphabet:
                index = self.affine_alphabet.index(letter)
                self.decrypted_text.append(self.alphabet[index])

            else:
                if letter == ' ':
                    continue
                raise ValueError("Sorry you entered an incorrect value. "
                                 "This communication is now terminated")

        self.decrypted_text = ''.join(self.decrypted_text)
        print("Here is your Decrypted message")
        print(self.decrypted_text)

