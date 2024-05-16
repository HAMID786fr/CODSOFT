#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import string

def generate_password(length):
    # Define the characters to be used for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty string to store the generated password
    password = ""

    # Generate the password by randomly selecting characters from the defined set
    for _ in range(length):
        password += random.choice(characters)

    # Return the generated password
    return password

def main():
    # Prompt the user to enter the desired length of the password
    length = int(input("Enter thelength of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




