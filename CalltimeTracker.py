import datetime
import sys

# ToDo: timer starts and stops, import results to list,
#  import list to csv, print daily stats on bottom of spreadsheet

first_names = []
last_names = []
give_amts = []
raise_amts = []
call_results = []
better_numbers = []
dates = []
call_notes = []

go_again = True
def call_program():
    in_list = False
    now = datetime.datetime.now()
    print("Welcome to the calltime tracker")
    first_name = str.upper(input("Prospect first name? "))
    last_name = str.upper(input("Prospect last name? "))
    call_note = str.upper(input("Any notes? (Enter to skip) "))
    call_result = str.upper(input("Enter call results: "))
    yes_list = ["YES", "Y", "YESS", "YE"]
    results_list = {
        "WG": "will give",
        "WR": "will raise",
        "TG": "try to give",
        "TR": "try to raise",
        "LM": "left message",
        "BN": "bad number",
        "DNC": "do not call"
    }
    give_amt = 0
    raise_amt = 0
    better_number = 0
    if call_result in results_list:
        in_list = True
        if call_result == "WG":
            give_amt = input("What amount? $")
        if call_result == "TG":
            give_amt = input("What amount? $")
        if call_result == "WR":
            raise_amt = input("What amount? $")
        if call_result == "TR":
            raise_amt = input("What amount? $")
        if call_result == "BN":
            better_number = str(input("What's a better number? Enter a question mark if you do not have one. "))
        print("Stored", now)
        first_names.append(first_name)
        last_names.append(last_name)
        call_results.append(call_result)
        give_amts.append(give_amt)
        raise_amts.append(raise_amt)
        better_numbers.append(better_number)
        dates.append(now)
        call_notes.append(call_note)
        again = str.upper(input('Do you want to enter another name? '))
        if again not in yes_list:
            print("Good work today")
            sys.exit()
    while in_list is False:
        print("Not Valid")
        call_result = str.upper(input("Enter call results: "))
        if call_result in results_list:
            in_list = True
            if call_result == "WG":
                give_amt = input("What amount? $")
            if call_result == "TG":
                give_amt = input("What amount? $")
            if call_result == "WR":
                raise_amt = input("What amount? $")
            if call_result == "TR":
                raise_amt = input("What amount? $")
            if call_result == "BN":
                better_number = str(input("What's a better number? Enter a question mark if you do not have one. "))
            print("Stored", now)
            first_names.append(first_name)
            last_names.append(last_name)
            call_results.append(call_result)
            give_amts.append(give_amt)
            raise_amts.append(raise_amt)
            better_numbers.append(better_number)
            dates.append(now)
            call_notes.append(call_note)
            again = str.upper(input('Do you want to enter another name? '))
            if again not in yes_list:
                print("Good work today")
                sys.exit()
while go_again == True:
    call_program()
print("Thank you")
