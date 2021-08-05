print("#### WELCOME TO THE MOST TRUSTED CAR BUYING SERVICE HELP:- Snazzy Autos!!!!")
model = ["1.Hatchback", "2.Saloon", "3.Estate"]
optional_extra = ["1.Luxury seats", "2.Satellite navigation", "3.Parking sensors", "4.Bluetooth", "5.Sound system"]
model_price = [535000, 495000, 625000]
optional_extra_price = [45000, 5500, 10000, 350, 1000]
extras_bought = []
model_bought = ""
model_count = 0
optional_extras_total_price = 0
cost = 0
while_count = 0
print("From the below Mention list choose any one model of car:")
for i in model:
    print(i)
x = input("Which model do you want to buy? ")
model_bought = x
for i in model:
    if x == i:
       break;
    else:
        model_count += 1
cost += model_price[model_count]

z = int(input("How many optional extras do you want to buy?(Answer in number) "))
print("From the below mention optional Extra Choose atleast one: ")
for i in optional_extra:
    print(i)

while while_count < z:
    y = input("Which extra do you want to get: ")
    extras_bought.append(y)
    for j in optional_extra:
        optional_extra_count = 0
        if y == j:
            break;
        else:
            optional_extra_count += 1
    cost += optional_extra_price[optional_extra_count]
    optional_extras_total_price += optional_extra_price[optional_extra_count]
    while_count += 1
    


old_car = input("Do you have an old car to trade in?(yes/no) ")
if old_car == "yes":
    bool = True
    while bool == True:
        discount = int(input("How much Price you expect of your new car?(10000 to 100000) "))
        if discount >= 10000 and discount <= 100000:
            bool = False
            
        else:
            print("Please enter a discount value under the range(10000 to 100000): ")
            bool = True
elif old_car == "no":
    cost = 0.95 * cost
    
new_or_old = input("Are you an old or a new customer?(old/new) ")
if new_or_old == "old":
    cost = 0.9* cost
if old_car == "yes":
    cost -= discount

print("The Types of Offer available in Snazzy auto!!!") 
print("first offer, If You do Full payment in once then 1% cashback or optional extras free(1)")
print("If You do payment in EMI over 4 years no Extra intrest to be added (2)")
print("if you do payment in EMI with over 7 years then 5% intrest to be added to ammount (3)")
offer = int(input("Which offer do you want to take? "))
temp_cost= 0
temp_cost = 0.01 * cost


if offer == 1:
    print("If you take 1% cashback, you will get " + str(temp_cost) + " off and if you want free optional extras, you will get " + str(optional_extras_total_price) + " off")
    choice = input("Do you want a 1% discount(1) or optional extras free(2)? ")
    if choice == 1:
        cost = 0.99*cost
        print("You bought a " + model_bought + " and you also bought the following extras:")
        for i in extras_bought:
           print(i)
        print("The total cost of your purchase is " + str(cost))
    else:
        cost -= optional_extras_total_price
        print("You bought a " + model_bought + " and you also bought the following extras:")
        for i in extras_bought:
           print(i)
        print("The total cost of your purchase is " + str(cost))
        

elif offer == 2:
    monthly_cost = 0
    monthly_cost = cost / 48
    print("You bought a " + model_bought + " and you also bought the following extras:")
    for i in extras_bought:
      print(i)
    print("The total cost of your purchase is",str(cost))
    print("You will have to pay " + str(monthly_cost) + " monthly")
else:
    monthly_cost = 0
    monthly_cost = (1.05 * cost) / 84
    print("You bought a " + model_bought + " and you also bought the following extras:")
    for i in extras_bought:
      print(i)
    print("The total cost of your purchase is",str(cost))
    print("You will have to pay " + str(monthly_cost) + " monthly")
    
