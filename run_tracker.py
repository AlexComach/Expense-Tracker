from expense_tracker import log_expense, view_list, store_data, breakdown, user_list, user_list_duplicate, tracker
from tabulate import tabulate


def main():
    user = str(input("Input your name: "))
    while True:
        try:
            print(f"\nWelcome {user} to my monthly expense tracker.")

            option = input("\nPress l to log an expense.\nPress v to view\nPress c to change to a different user.\nPress b for a breakdown of inputted expenses.\nPress e to end.\n\nEnter letter here: ")

            if option.lower() == "l":
                log_expense_amount = float(input("\nInput expense amount: "))
                log_expense_category = str(input("Input expense category, e.g. Food, Transport: ")).lower()
                log_expense_description = str(input("Input expense description: "))
                print("\n")

                current_expense = log_expense(user, log_expense_amount, log_expense_category, log_expense_description)

                view_list(user, current_expense)
                
                store_data_confirmation = input("Would you like to store this data?\ny for yes\nn for no\n")

                if store_data_confirmation.lower() == "y":
                    store_data(user, log_expense(user, log_expense_amount, log_expense_category, log_expense_description))
                    print("\nStored.\n")
                    
                    view = input("Would you like to view everything in your name?\nPress y for yes and n for no\n\nInput here: ")

                    if view.lower() == "y":
                        view_list(user, user_list)
                        continue
                        
                    elif view.lower() == "n":
                        continue

                    else:
                        print("Invalid input. Going back to the top.")
                        continue
            
            elif option.lower() == "v":
                view_list(user, user_list)
                continue
            
            elif option.lower() == "e":
                return "Thank you, come again." 

            elif option.lower() == "b":
                wage = int(input("Enter your current monthly wage: "))
                breakdown(user, wage)

            elif option.lower() == "c":
                user = str(input("Choose a name to change to: "))
                continue

            else:
                print("Invalid Input.\n")      

        except(TypeError, ValueError) as e:
            print(f"\nError: {e}\n")
            continue

        except KeyboardInterrupt as e:
            print(f"\nError {e}")
            continue

        except Exception as e:
            print(f"Unexpected error: {e}")
            continue     

main()