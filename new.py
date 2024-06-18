import stepic
from PIL import Image
from cryptography.fernet import Fernet

def encode():

    print("*====================================*")

    file = input("Photo: ")
    img = Image.open(file)
    print("The key for encoding: ")
    key = Fernet.generate_key()
    print(key)
    enc = Fernet(key)
    text = input("Enter the data to be encoded: ")
    text_enc = enc.encrypt(text.encode())
    img_stegano = stepic.encode(img, text_enc)
    f1 = input("Enter the new file to save: ")
    img_stegano.save(f1)
    print("Data Encoded Successfully")

    print("*====================================*")

# def decode():

#     print("*====================================*")

#     file = input("Enter the file to be Decoded: ")
#     img = Image.open(file)
#     key = input("Enter the Key for Decryption: ")
#     dec = Fernet(key)
#     decoded = stepic.decode(img)
#     text_dec = dec.decrypt(decoded.encode())
#     print("Encoded Data is: ", text_dec.decode())

#     print("*====================================*")
def decode():

    print("*====================================*")

    file = input("Enter the file to be Decoded: ")
    img = Image.open(file)
    key = input("Enter the Key for Decryption: ")
    try:
        dec = Fernet(key)
        decoded = stepic.decode(img)
        text_dec = dec.decrypt(decoded.encode())
        print("Encoded Data is: ", text_dec.decode())
    except:
        print("Invalid key! Please enter the correct key.")

    print("*====================================*")


def main():
    
    while True:
        print("\n1. Encode\n2. Decode\n3. Exit\n")
        choice = input("Enter your choice: ")

        if choice == '1':
            encode()
        elif choice == '2':
            decode()
        elif choice == '3':
            break
        else:
            print("Please Enter the valid choice")


if __name__ == "__main__":
    main()