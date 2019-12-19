#
# File:      26852_encryptor.py
# Author:    Ke Zhang
# SAIBT Id:  26852
# Version:   1.0  11 April 2017
# Description: Assignment part II
#   This is my own work as defined by the University's
#   Academic Misconduct policy.
#

# set basic message
index = 0
newString = ""
count = 1
number = 0
rateCheck = False

#menu 
print("Welcome to CMS (Code Management System)\n")
print("\n*** Menu ***\n")
print("1. Encrypt string")
print("2. Decrypt string")
print("3. All allowed decryptions")
print("4. Quit")

#ask use to enter command
choice = input("\nPlease enter choice (1-4): ")

#the while loop for user to end the program
while choice != "4":
    number = 0
    # error check for command
    while choice != '1' and choice != '2' and choice != '3' and choice != '4':
        choice = input("Invalid choice. Please enter choice (1-4): ")
             
    # the step of encryption 
    if choice == "1":

        newString = ""
        index = 0
        number = 0
        # enter the string and choose the rate
        toEncrypt = input("\nPlease enter string to encypt: ")
    
        #error check for invalid rate
        rate = input("Please enter offset value (1 - 94): ")
        while not(rate.isdigit() and 1 <= int(rate) <= 94):
            rate = input("Invalid offset. Please enter offset value (1 - 94): ")
               
        #program to encrypt the string
        for letter in toEncrypt:
            rateNum = ord(toEncrypt[index]) + int(rate)

            # to set the value in the range 32 - 126
            if rateNum > 126:
                rateNum = 32 + ((ord(toEncrypt[index]) + int(rate)) - 126) -1
            elif 32 <= rateNum <= 126:
                rateNum = ord(toEncrypt[index]) + int(rate)        
            newString += chr(rateNum)
            index +=1
        print("\nEncrypted string: ",newString)
        
    # the step of decryption
    elif choice == "2":

        newString = ""
        index = 0
        number = 0
        
        toDecrypt = input("\nPlease enter string to decypt: ")
        
        rate = input("Please enter offset value (1 - 94): ")

        #error check for invalid rate
        while not rate.isdigit() and not (1 <= int(rate) <= 94)  :
            rate = input("Invalid offset. Please enter offset value (1 - 94): ")
        
        #the program to decrypt the string
        for letter in toDecrypt:
            rateNum = ord(toDecrypt[index]) - int(rate)

            if rateNum < 32:
                rateNum = 126 - ( 32 - (ord(toDecrypt[index]) - int(rate))) + 1
            elif 32 < rateNum < 126:
                rateNum = ord(toDecrypt[index]) - int(rate)        
            newString += chr(rateNum)
            index +=1
        print("\nEncrypted string: ",newString)
        
    # the step to get all the decryption
    elif choice == "3":

        # the while loop to show all decryption 
        while count <= 94:
            index = 0
            #the first decryption
            if count == 1: 
                newString = ""
                index = 0
                toDecrypt = input("\nPlease enter string to decypt: ")
                for  letter in toDecrypt:
                    
                    rateNum = ord(toDecrypt[index]) - 1
                    if rateNum < 32:
                        rateNum = 126 - ( 32 - ord(toDecrypt[index])) 
                    elif 32 <= rateNum <= 126:
                        rateNum = ord(toDecrypt[index]) - 1
                    elif rateNum >= 126:
                        rateNum = 32 + (ord(toDecrypt[index])-126) -1
                    
                    newString += chr(rateNum)
                    index +=1
                
                print("\nOffset:",count,"Decrypted string: ",newString)
                count += 1
            # the another 93 decryption
            else:
                stepString = ""
                       
                for  letter in newString:
                    
                    rateNum = ord(newString[index]) - 1
                    if rateNum < 32:
                        rateNum =(126 - ( 32 - ord(newString[index]))) 
                    elif 32 <= rateNum <= 126:
                        rateNum = ord(newString[index]) - 1
                    elif rateNum > 126:
                        rateNum = 32 + (ord(newString[index])-126) -1
                    stepString += chr(rateNum)
                    index +=1
                
                print("Offset:",count,"Decrypted string: ",stepString)
                count += 1
                newString = stepString

    if choice != '4':
        print("\n*** Menu ***\n")
        print("1. Encrypt string")
        print("2. Decrypt string")
        print("3. All allowed decryptions")
        print("4. Quit")

        choice = input("\nPlease enter choice (1-4): ")
        
#end of the program
print("\nThank you for using CMS.")
    

