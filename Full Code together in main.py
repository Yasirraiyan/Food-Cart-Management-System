menu = ["pizza", "pazta", "coffee", "biriyani", "burger"]
totalbill = 0
turn = 4

while turn > 0:
    choose = input("Enter your choice: ")
    
    if choose in menu:
        print("Valid choice.")
        
        if choose == "pizza":
            totalbill += 40
        elif choose == "pazta":
            totalbill += 50
        elif choose == "coffee":
            totalbill += 60
        elif choose == "biriyani":
            totalbill += 70
        elif choose == "burger":
            totalbill += 80

    else:
        print("Invalid choice!")

    turn -= 1
    if turn > 0:
        print("Total bill so far:", totalbill)

print("Final Total Bill:", totalbill)
