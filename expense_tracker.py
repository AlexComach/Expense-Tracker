from tabulate import tabulate
from connect_to_db import get_db_connection
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
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
        current_expense["date"] = formatted_date
    
        return current_expense
    
    except Exception as e:
        return f"Unexpected Error: {e}"

def view_list(username, list_to_view):
    try:
        if not list_to_view:
            return "You don't have anything in yet.\n"

        if isinstance(list_to_view, dict):
            list_to_view = [list_to_view]

        filtered_list = []
        
        for entry in list_to_view:
            if entry["user_name"] == username:
                filtered_list.append(entry)

        if not filtered_list:
            return f"No records found for user: {username}"

        list_table = tabulate(filtered_list, headers="keys", tablefmt="simple_outline")
        print(list_table)
        return list_table

    except Exception as e:
        return f"Unexpected error: {e}"


def store_data(user_name, expense_data):
    try:
        mydb, mycursor = get_db_connection()
        
        tracker[user_name] = expense_data 
        user_list.append(expense_data)  
        user_list_duplicate.append(expense_data)
        
        sql = "INSERT INTO expenses (user_name, category, description, amount, date) VALUES (%s, %s, %s, %s, %s)"
        
        values = []
        
        values.append((expense_data["user_name"], expense_data["category"], expense_data["description"], expense_data["amount"], expense_data["date"]))

        # print(values)
        
        mycursor.executemany(sql, values)
        mydb.commit()
        mydb.close()
        
    except Exception as e:
        return f"Unexpected error: {e}"


def breakdown(username, wage):
    try:
        if len(user_list) == 0:
            return "You dont have anything in yet.\n"
            
        amount = []
        category_sums = {}  
        current_category = user_list_duplicate[0]["category"]
        user_expenses = []

        for entry in user_list_duplicate:
            if entry["user_name"] == username:
                user_expenses.append(entry)

        if len(user_expenses) == 0:
            return f"{username} has no recorded expenses.\n"

        for current_user_values in user_expenses:
            if current_user_values["category"] == current_category:
                amount.append(current_user_values["amount"])
            else:
                category_sums[current_category] = sum(amount)
                current_category = current_user_values["category"]
                amount.append(current_user_values["amount"])  
        
        category_sums[current_category] = sum(amount)

        category_sums["total"] = sum(category_sums.values())

        print(f"\n{username}, your breakdown is as follows:\n")
        
        table = []
        for key, value in category_sums.items():
            table.append([key, value])

        print(tabulate(table, headers=["Expenses", "Cost"], tablefmt="presto"))
        print("\n")
        
        for key, value in category_sums.items():
            if key != "total":
                print(f"{key} has accounted for {round(value/wage*100, 1)}% of your wage and {round(value/category_sums['total']*100, 1)}% of your total spendings this month.")
            
        print(f"\nYou have {wage - category_sums['total']} left.")

    except Exception as e:
        print(f"Unexpected error: {e}")




# store_data("Alex", log_expense("Alex", 150, "transport", "car"))
# store_data("Alex", log_expense("Alex", 150, "food", "groceries"))
# store_data("Bill", log_expense("Bill", 150, "transport", "bike"))
# print(user_list)
# breakdown("Bill", 2000)