import random 

length = 15 
i = 1 
char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*" 
password = "" 

while i <= length: 
    password = password + random.choice(char_set) 
    i = i + 1 

# Open the output file in write mode
with open('output.txt', 'w') as outfile:
    # Write the password to the output file
    outfile.write("Password: " + password + "\n")
