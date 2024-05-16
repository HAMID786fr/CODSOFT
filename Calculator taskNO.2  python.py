#!/usr/bin/env python
# coding: utf-8

# In[3]:


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Division by zero is not allowed. Please try again."

def main():
    print("Calculator")
    
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")
        
        # Take input from the user for operation choice
        choice = input("Enter  number of operation  ")

        if choice == '0':
            print("Exiting the calculator...")
            break

        # Check if the choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            try:
                # Take input from the user for the two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                result = None
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                if result is not None:
                    print(f"The result is: {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()


# In[ ]:




