name = input("Please enter your name : ")

meet = float(input("Please enter your meet ammount into kg : "))
vagitables = float(input("Please enter your vagitable ammount into kg : "))
fruits = float(input("Please enter your fruit ammount into kg : "))
medicines = float(input("Please enter your medicine ammount into Tab : "))
drinks = float(input("Please enter your drink ammount into Bottle : "))

meet_ammount = meet * 200
vagitables_ammount = vagitables * 100
fruits_ammount = fruits * 80
medicines_ammount = medicines * 50
drinks_ammount = drinks * 40
total_ammount = meet_ammount + vagitables_ammount + fruits_ammount + medicines_ammount + drinks_ammount
print(f"Dear {name} sir, You have  to pay {total_ammount} $")
print("You can pay with card as well as cash")

membership =input(f"Hello {name} sir. Do you have any membership? (yes/no)".lower())

if membership == "yes":
    print(f"Dear {name} sir, As you have our membership card, You will get 20% discount.")
    print("Please give your membership card.")
    print("Verifying your membership card...")
    print(f"Your total ammount is : {total_ammount - (total_ammount * 0.2)} $")
    
elif membership == "no":
    print(f"Dear {name} sir, As you dont have our membership card, You will not get any discount.")
    print("But if you buy our membership card, You will get 20% for normal disscount.")
    print("And extra 10% discount for being new memeber.")
    print("If you want to apply for membership You can create it here")
    
    new_membership = input("Do you want to create membership? (yes/no) ")
    new_membership = new_membership.lower()
    if new_membership == "yes":
        print("Please wait, We are creating your membership...")
        print("Your membership has been created successfully.")
        print("As you are new member, You will get extra 10% discount.")
        print("Normal discount 20% + New member discount 10% = Total 30% discount")
        print(f"After all Your total ammount is : {total_ammount - (total_ammount * 0.3)}")
    else:
        print(f"Your total ammount is : {total_ammount} $")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
