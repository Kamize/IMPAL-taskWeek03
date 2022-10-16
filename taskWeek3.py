amount = int(input("Input total computer to be repaired : "))
service_time = int(input("Insert time : "))
pick_up = input("Pick Up? (y/n) : ")


#Computer/Peripheral Amount
if amount == 1 or amount == 2:
    add_fee = 0
    base_fee = 50
elif amount >= 3 or amount <= 10:
    add_fee = 10 * amount
    base_fee = 100
elif amount > 10:
    add_fee = 10 * amount
    base_fee = 500
#Price based on service time
if service_time < 8 and service_time > 17:
    base_fee = base_fee * 2

if pick_up == "yes":
    base_fee = base_fee / 2

base_fee = base_fee + add_fee
print("Total fee : ", base_fee)