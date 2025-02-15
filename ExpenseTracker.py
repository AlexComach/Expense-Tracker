from tabulate import tabulate

user_list = []
user_list_duplicate = []
tracker = {}

def log_expense(user_name, amount, category, description):
    try:
        current_expense = {}
        current_expense["user_name"] = user_name
        current_expense["category"] = category
        current_expense["description"] = description
        current_expense["amount"] = amount
    
        return current_expense
    
    except Exception as e:
        print(f"Unexpected Error: {e}")


def view_list(username, list_to_view):
    try:
        if len(list_to_view) == 0:
            print("You dont have anything in yet.\n")
            return

        if isinstance(list_to_view, dict):
            list_to_view = [list_to_view]

        for entry in list_to_view:
            if entry["user_name"] == username:
                list_table = tabulate(list_to_view, headers='keys', tablefmt='simple_outline')
        print(list_table)
        
    
    except Exception as e:
        print(f"Unexpected error: {e}")


def store_data(user_name, expense_data):
    try:
        tracker[user_name] = expense_data
        user_list.append(expense_data)  
        user_list_duplicate.append(expense_data)

    except Exception as e:
        print(f"Unexpected error: {e}")


def breakdown(username, wage):
    try:
        if len(user_list) == 0:
            print("You don't have anything in yet.\n")
            return
        
        amount = []
        category_sums = {}  
        current_category = user_list_duplicate[0]['category']

        for entry in user_list_duplicate:
            if entry['category'] == current_category:
                amount.append(entry['amount'])
            else:
                category_sums[current_category] = sum(amount)
                amount = []
                current_category = entry['category']
                amount.append(entry['amount'])  

        
        category_sums[current_category] = sum(amount)

        category_sums["total"] = sum(category_sums.values())

        print(f"\n{username}, your breakdown is as follows:\n")
        
        table = [[key, value] for key, value in category_sums.items()]
        print(tabulate(table, headers=["Expenses", "Cost"], tablefmt="presto"))
        print("\n")
        
        for key, value in category_sums.items():
            if key != "total":
                print(f"{key} has accounted for {(round(value/wage)*100), 1}% of your wage and {(round(value/category_sums['total']*100), 1)}% of you total spendings this month.")
            
        
        print(f"\nYou have {(wage - category_sums['total'])} left.")



        
        

    except Exception as e:
        print(f"Unexpected error: {e}")
    

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

                view_list(user, log_expense(user, log_expense_amount, log_expense_category, log_expense_description))
                
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
                print("Thank you, come again.")
                break

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
            break

        except Exception as e:
            print(f"Unexpected error: {e}")
            break     

main()


