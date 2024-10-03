def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add = input("Enter the item to add: ")
            shopping_list.append(add)
            print(f"{add} Has Been Added! ")
            pass
        elif choice == '2':
            remove = input("Please Choose The Item You Want To Remove: ")
            shopping_list.remove(remove)
            print(f"{remove} Has Been Removed! ")
            pass
        elif choice == '3':
            print(f"These Are All Items You Have: {shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
