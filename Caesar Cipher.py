#!/usr/bin/python3

from argparse import ArgumentParser


class Cipher:
    def __init__(self):
        if __name__ == "__main__":
            parser = ArgumentParser(
                description="Caeser Cipher is a method of Encrypt or Decrypt a message")
            parser.add_argument(
                "crypt",
                type=str,
                help="Give 'encrypt' if you want to encrypt a message or Give 'decrypt' if you want to decrypt a message")

            args = parser.parse_args()

            final_message = None

            try:
                if args.crypt == "encrypt":
                    message, shift = self.secretMessage()
                    final_message = self.encrypt(message, shift)

                    print("\nEncrypted Message: ", final_message)
                elif args.crypt == "decrypt":
                    message, shift = self.secretMessage()
                    final_message = self.decrypt(message, shift)

                    print("\nDecrypted Message: ", final_message)
                else:
                    print("Invalid argument!")
            except ValueError:
                print("\nThe shift value should be a number!")
            except KeyboardInterrupt:
                print("\nCtrl + c detected!")

    def secretMessage(self):
        message = input("Enter the message: ")
        shift = int(input("Enter the shift key: "))

        return message, shift

    def encrypt(self, message, shift):
        encrypted_message = ""

        for char in message:
            if char == " ":
                encrypted_message += char
            elif char.isupper():
                encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)

        return encrypted_message

    def decrypt(self, message, shift):
        decrypted_message = ""

        for char in message:
            if char == " ":
                decrypted_message += char
            elif char.isupper():
                decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)

        return decrypted_message


Cipher()
