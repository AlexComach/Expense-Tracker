from tabulate import tabulate
from expense_tracker import log_expense, view_list, store_data, breakdown
import pytest


@pytest.fixture
def expense_data():
    log_expense_data = {"user_name":"Alex", "category":"transport", "description":"car", "amount": 150}

    return log_expense_data

@pytest.fixture
def empty_list():
    list = []
    return list


@pytest.fixture
def test_list():
    test_list_no_error = [{"user_name":"Alex", "category":"bills", "description":"water", "amount": 20},{"user_name":"Alex", "category":"transport", "description":"car", "amount": 150},{"user_name":"Alex", "category":"food", "description":"lunch", "amount": 10},{"user_name":"Alex", "category":"food", "description":"groceries", "amount": 200}]
    return test_list_no_error

def test_log_expense(expense_data):
    assert log_expense("Alex", 150, "transport", "car") == expense_data


def test_view_list(test_list, empty_list):
    test_list_error = [{"user_name":"Alex", "amount": 1.50},{"user_name":"Bill", "amount": 2}]
    test_list_dict = {"user_name":"Alex", "amount": 1.50}

    assert view_list("Alex", empty_list) == "You dont have anything in yet.\n"
    assert view_list("Alex", test_list) == tabulate(test_list, headers='keys', tablefmt='simple_outline')
    assert view_list("Alex", test_list_error) == "user error"
    assert view_list("Alex", test_list_dict) == tabulate([test_list_dict], headers='keys', tablefmt='simple_outline')



def test_store_data(expense_data, test_list):
    user_name = "Alex"
    tracker = {user_name:expense_data}

    assert tracker[user_name] == expense_data
    assert expense_data in test_list 


def test_breakdown(test_list, empty_list):    
    
    category_sums = {}
    amount = []
    current_category = test_list[0]["category"]

    for entry in test_list:
        if entry["category"] == current_category:
            amount.append(entry["amount"])
        else:
            category_sums[current_category] = sum(amount)
            amount = []
            current_category = entry["category"]
            amount.append(entry["amount"])
    
    category_sums[current_category] = sum(amount)


    assert breakdown("Alex", empty_list) == "You dont have anything in yet.\n"
    assert category_sums["food"] == 210 
    assert category_sums["transport"] == 150  
    assert category_sums["bills"] == 20  
    assert sum(category_sums.values()) == 380
    
    

    



    

