#Unique password
#This code is has list of 10 thousand most common used password, Enter your code in cmd and this program will check if that already exists.
import random 
import string

def generate_salt(lenght=32):
    characters = string.ascii_letters + string.digits
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt
    
def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = [line.strip() for line in file]
    return passwords

def is_password_matched(user_input, password_list):
    return user_input in password_list

def main():
    file_path = "Please input your own file path"
    
    passwords = read_passwords(file_path)
    
    while True:
        user_input = input("Enter your password to check: ").strip()
        
     
        
        if is_password_matched(user_input, passwords):
            print("The password matches one in the list. Common password denied. DONOT USE")
        else:
            print("The password does not match any in the list. ITS A UNIQUE PASSWORD")
            print(f"Generated salt: {salt}")

if __name__ == "__main__":
    main()

