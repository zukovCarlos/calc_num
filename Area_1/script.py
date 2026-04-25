import baseConverter

def main():
    print("Welcome to the base converter!")
    print("Please enter the number you want to convert:")
    number = input()
    print("Please enter the base of the number you want to convert from (2-36):")
    from_base = int(input())
    print("Please enter the base you want to convert to (2-36):")
    to_base = int(input())
    
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        print("Invalid base. Please enter a base between 2 and 36.")
        return
    
    try:
        converted_number = baseConverter.convertBase(number, from_base, to_base)
        print(f"The number {number} in base {from_base} is {converted_number} in base {to_base}.")
    except ValueError as e:
        print(f"Error: {e}")
        
main()