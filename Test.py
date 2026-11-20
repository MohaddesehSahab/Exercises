base_cost = 200000
age = int(input("Enter your age : "))
membership = input("Do you have a club membership ? (yes or no): ").strip().upper()
if age < 0 or age > 100 :
    print("Invalid age!")
elif age <= 15 :
    print("You can us the service for free!")
elif 16 <= age <= 50 :
    if membership == "YES" :
        discounted_cost = int(base_cost * 0.5)
        print(f"Final Cost : {discounted_cost}")
    elif membership == "NO" :
        discounted_cost = base_cost
        print(f"Final Cost : {discounted_cost}")
    else :
        print("Invalid Input, Please enter Yes or No")
else :
    if membership == "YES" :
        discounted_cost = int(base_cost * 0.2)
        print(f"Final Cost : {discounted_cost}")
    elif membership == "NO" :
        discounted_cost = int(base_cost * 0.35)
        print(f"Final Cost : {discounted_cost}")
    else :
        print("Invalid Input, Please enter Yes or No")