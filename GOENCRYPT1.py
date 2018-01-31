result = ''
message = ''
choice = ''
 
while choice != '-1':
    choice = input("\nWelcome to GOENCRYPT! The fast,small and effecient encryptor!\nPress 1 to encrypt, Press 2 to Decrypt, Or -1 to Exit Program: ")
 
    if choice == '1':
        message = input("\nPlease Enter the Text To Encrypt: ")
 
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)
 
        print (result + '\n\n')
        result = ''
 
    elif choice == '2':
        message = input("\nPlease Enter The Text to Decrypt : ")
 
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)
 
        print (result + '\n\n')
        result = ''
 
    elif choice != '-1':
        print ("You have entered an invalid choice. Please try again.\n\n")
