class Cipher:
    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()



class Atbash(Cipher):
    def __init__(self):
        self.alphabet =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.cipher_alphabet = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M',
                                         'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']


    def encrypt(self, text):
        self.encrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                self.encrypted_text.append(self.cipher_alphabet[index])

        self.encrypted_text = ''.join(self.encrypted_text)
        print("Here is your Encrypted message:")
        print(self.encrypted_text)

    def decrypt(self, text):
        self.decrypted_text = []
        text = text.upper()

        for letter in text:
            if letter in self.cipher_alphabet:
                index = self.cipher_alphabet.index(letter)
                self.decrypted_text.append(self.alphabet[index])

        self.decrypted_text = ''.join(self.decrypted_text)
        print("Here is your Decrypted message:")
        print(self.decrypted_text)




class Keyword(Cipher):
    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.keyword_alphabet = ['K', 'R', 'Y', 'P', 'T', 'O', 'S', 'A', 'B', 'C', 'D', 'E', 'F',
                                 'G', 'H', 'I' 'J', 'L', 'M', 'N', 'Q', 'U', 'V', 'W', 'X', 'Z']

    def encrypt(self, text):
        self.encrypted_text = []
        text = text.upper()

        for thing in text:
            if thing in self.alphabet:
                index = self.alphabet.index(thing)
                self.encrypted_text.append(self.keyword_alphabet[index])

        self.encrypted_text = ''.join(self.encrypted_text)
        print("Here is your Enrypted message:")
        print(self.encrypted_text)


    def decrypt(self, text):
        self.decrypted_text = []
        text = text.upper()

        for char in text:
            if char in self.keyword_alphabet:
                index = self.keyword_alphabet.index(char)
                self.decrypted_text.append(self.alphabet[index])

        self.decrypted_text = ''.join(self.decrypted_text)
        print("Here is your Decrypted message:")
        print(self.decrypted_text)
