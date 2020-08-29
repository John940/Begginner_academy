class Machine:
    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9

    def action(self):
        actions = "0"
        while actions != "exit":
            actions = input("Write action (buy, fill, take, remaining, exit):")
            if actions == "remaining":
                self.screen()
            elif actions == "buy":
                self.buy()
            elif actions == "fill":
                self.fill()
            elif actions == "take":
                self.take()

    def screen(self):
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")

    def espresso(self):
        if self.coffee_beans < 16:
            print("Sorry, not enough coffee beans!")
        elif self.water < 250:
            print("Sorry, not enough water!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            self.money += 4
            self.disposable_cups -= 1
            self.coffee_beans -= 16
            self.water -= 250
            print("I have enough resources, making you a coffee!")

    def latte(self):
        if self.coffee_beans < 20:
            print("Sorry, not enough coffee beans!")
        elif self.water < 350:
            print("Sorry, not enough water!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        else:
            self.money += 7
            self.disposable_cups -= 1
            self.coffee_beans -= 20
            self.milk -= 75
            self.water -= 350
            print("I have enough resources, making you a coffee!")

    def cappuccino(self):
        if self.coffee_beans < 12:
            print("Sorry, not enough coffee beans!")
        elif self.water < 200:
            print("Sorry, not enough water!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        else:
            self.disposable_cups -= 1
            self.coffee_beans -= 12
            self.money += 6
            self.milk -= 100
            self.water -= 200
            print("I have enough resources, making you a coffee!")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        cafe = input()
        if cafe == "1":
            self.espresso()
        elif cafe == "2":
            self.latte()
        elif cafe == "3":
            self.cappuccino()

    def fill(self):
        print("Write how many ml of water do you want to add:")
        added_water = int(input())
        self.water += added_water
        print("Write how many ml of milk do you want to add:")
        added_milk = int(input())
        self.milk += added_milk
        print("Write how many grams of coffee beans do you want to add:")
        added_beans = int(input())
        self.coffee_beans += added_beans
        print("Write how many disposable cups of coffee do you want to add:")
        added_cups = int(input())
        self.disposable_cups += added_cups

    def take(self):
        print("I gave you $", self.money)
        self.money = 0


mikel_coffee = Machine()
mikel_coffee.action()
