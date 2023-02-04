# stage 1
# procedure = ['Starting to make a coffee', 'Grinding coffee beans', 'Boiling water',
#              'Mixing boiled water with crushed coffee beans', 'Pouring coffee into the cup',
#              'Pouring some milk into the cup', 'Coffee is ready!']
# for i in procedure:
#     print(i)

# stage 2
# number = int(input("Write how many cups of coffee you will need:"))
# water = number * 200
# milk = number * 50
# coffee_bean = number * 15
# print(f"For {number} cups of coffee you will need:\n"
#       f"{water} ml of water\n"
#       f"{milk} ml of milk\n"
#       f"{coffee_bean} g of coffee beans")

# stage 3
# water_pre = int(input("Write how many ml of water the coffee machine has:"))
# milk_pre = int(input("Write how many ml of milk the coffee machine has:"))
# bean_pre = int(input("Write how many grams of coffee beans the coffee machine has:"))
# number = int(input("Write how many cups of coffee you will need:"))
# water = number * 200
# milk = number * 50
# coffee_bean = number * 15
# if water > water_pre or milk > milk_pre or coffee_bean > bean_pre:
#     N = min(water_pre // 200, milk_pre // 50, bean_pre // 15)
#     print(f"No, I can make only {N} cups of coffee")
# elif (water_pre - water) // 200 >= 1 and (milk_pre - milk) // 50 >= 1 and (bean_pre - coffee_bean) // 15 >= 1:
#     n = min((water_pre - water) // 200, (milk_pre - milk) // 50, (bean_pre - coffee_bean) // 15)
#     print(f"Yes, I can make that amount of coffee (and even {n} more than that)")
# else:
#     print("Yes, I can make that amount of coffee")

# stage 4
# def buy_coffee():
#     global water, milk, coffee_bean, cup, money
#     kind = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
#     water_c = [250, 350, 200]
#     milk_c = [0, 75, 100]
#     coffee_bean_c = [16, 20, 12]
#     money_e = [4, 7, 6]
#     water -= water_c[kind - 1]
#     milk -= milk_c[kind - 1]
#     coffee_bean -= coffee_bean_c[kind - 1]
#     money += money_e[kind - 1]
#     cup -= 1
#
#
# def fill():
#     global water, milk, coffee_bean, cup
#     variable = [water, milk, coffee_bean, cup]
#     fill_list = ["ml of water", "ml of milk", "grams of coffee beans", "disposable cups"]
#     for i in range(4):
#         variable[i] += int(input(f"Write how many {fill_list[i]} you want to add:"))
#     water, milk, coffee_bean, cup = variable
#
# def withdraw():
#     global money
#     print(f"I gave you ${money}")
#     money = 0
#
#
# water = 400
# milk = 540
# coffee_bean = 120
# cup = 9
# money = 550
#
#
# def represent():
#     global water, milk, coffee_bean, cup, money
#     print(f"The coffee machine has:\n"
#           f"{water} ml of water\n"
#           f"{milk} ml of milk\n"
#           f"{coffee_bean} g of coffee beans\n"
#           f"{cup} disposable cups\n"
#           f"{money} of money\n")
#
#
# def operation():
#     op_name = input("Write action (buy, fill, take):")
#     if op_name == "buy":
#         buy_coffee()
#     elif op_name == "fill":
#         fill()
#     elif op_name == "take":
#         withdraw()
#     print()
#     represent()
#
#
# represent()
# operation()

# stage 5
# water = 400
# milk = 540
# coffee_bean = 120
# cup = 9
# money = 550
#
#
# def buy_coffee():
#     global water, milk, coffee_bean, cup, money
#     kind = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
#     if kind == "back":
#         return
#     else:
#         kind = int(kind)
#     water_c = [250, 350, 200]
#     milk_c = [0, 75, 100]
#     coffee_bean_c = [16, 20, 12]
#     money_e = [4, 7, 6]
#     if water < water_c[kind - 1]:
#         print("Sorry, not enough water!")
#     elif milk < milk_c[kind - 1]:
#         print("Sorry, not enough milk!")
#     elif coffee_bean < coffee_bean_c[kind - 1]:
#         print("Sorry, not enough coffee beans!")
#     elif cup == 0:
#         print("Sorry, not enough disposable cups!")
#     else:
#         print("I have enough resources, making you a coffee!")
#         water -= water_c[kind - 1]
#         milk -= milk_c[kind - 1]
#         coffee_bean -= coffee_bean_c[kind - 1]
#         money += money_e[kind - 1]
#         cup -= 1
#
#
# def fill():
#     global water, milk, coffee_bean, cup
#     variable = [water, milk, coffee_bean, cup]
#     fill_list = ["ml of water", "ml of milk", "grams of coffee beans", "disposable cups"]
#     for i in range(4):
#         variable[i] += int(input(f"Write how many {fill_list[i]} you want to add:"))
#     water, milk, coffee_bean, cup = variable
#
#
# def withdraw():
#     global money
#     print(f"I gave you ${money}")
#     money = 0
#
#
# def represent():
#     global water, milk, coffee_bean, cup, money
#     print(f"The coffee machine has:\n"
#           f"{water} ml of water\n"
#           f"{milk} ml of milk\n"
#           f"{coffee_bean} g of coffee beans\n"
#           f"{cup} disposable cups\n"
#           f"{money} of money\n")
#
#
# def operation():
#     while True:
#         op_name = input("Write action (buy, fill, take, remaining, exit):")
#         if op_name == "buy":
#             buy_coffee()
#         elif op_name == "fill":
#             fill()
#         elif op_name == "take":
#             withdraw()
#         elif op_name == "remaining":
#             represent()
#         elif op_name == "exit":
#             break
#
#
# operation()


# stage 6
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_bean = 120
        self.cup = 9
        self.money = 550
        self.kind = None
        self.water_c = [250, 350, 200]
        self.milk_c = [0, 75, 100]
        self.coffee_bean_c = [16, 20, 12]
        self.money_e = [4, 7, 6]
        self.variable = None
        self.fill_list = ["ml of water", "ml of milk", "grams of coffee beans", "disposable cups"]
        self.op_name = None

    def buy_coffee(self):
        self.kind = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.kind == "back":
            print()
            return
        else:
            self.kind = int(self.kind)
        if self.water < self.water_c[self.kind - 1]:
            print("Sorry, not enough water!\n")
        elif self.milk < self.milk_c[self.kind - 1]:
            print("Sorry, not enough milk!")
        elif self.coffee_bean < self.coffee_bean_c[self.kind - 1]:
            print("Sorry, not enough coffee beans!\n")
        elif self.cup == 0:
            print("Sorry, not enough disposable cups!\n")
        else:
            print("I have enough resources, making you a coffee!\n")
            self.water -= self.water_c[self.kind - 1]
            self.milk -= self.milk_c[self.kind - 1]
            self.coffee_bean -= self.coffee_bean_c[self.kind - 1]
            self.money += self.money_e[self.kind - 1]
            self.cup -= 1

    def fill(self):
        self.variable = [self.water, self.milk, self.coffee_bean, self.cup]
        for i in range(4):
            self.variable[i] += int(input(f"Write how many {self.fill_list[i]} you want to add:"))
        self.water, self.milk, self.coffee_bean, self.cup = self.variable
        print()

    def withdraw(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def represent(self):
        print(f"The coffee machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.coffee_bean} g of coffee beans\n"
              f"{self.cup} disposable cups\n"
              f"${self.money} of money\n")

    def operation(self):
        while True:
            self.op_name = input("Write action (buy, fill, take, remaining, exit):")
            if self.op_name == "buy":
                print()
                self.buy_coffee()
            elif self.op_name == "fill":
                print()
                self.fill()
            elif self.op_name == "take":
                print()
                self.withdraw()
            elif self.op_name == "remaining":
                print()
                self.represent()
            elif self.op_name == "exit":
                break


coffee_machine_1 = CoffeeMachine()
coffee_machine_1.operation()
