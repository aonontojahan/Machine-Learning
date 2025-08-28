names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']

name = input("Welcome, whom are you looking for? ")

if name == "Alice" or name == "Bob" or name == "Charlie" or name == "David" :
    print(f"{name} is available.")

elif name == "Eva":
    print(f"We dont fuck with MAGI {name}")
    
else:
    print(f"{name} is not available.")