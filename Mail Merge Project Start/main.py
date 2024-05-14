#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/py thon/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# ./Input/Letters/starting_letter.txt

with open("./Input/Names/invited_names.txt") as file:
    names=file.readlines()
    print(names)
with open("./Input/Letters/starting_letter.txt") as mail_file:
    mail=mail_file.read()
    
    print(mail)

for name in names:
    new_msg=mail.replace('[name]', name.strip('\n'))
    with open(f"./Output/ReadyToSend/{name.strip('\n')}_invited_names.txt",mode='w') as write_file:
        
        write_file.write(new_msg)
    
#     mail.replace('name', name)
#     print(mail)