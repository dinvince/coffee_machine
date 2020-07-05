class CoffeeMachine:
    def __init__(self):
        self.water: int = 400
        self.milk: int = 540
        self.beans: int = 120
        self.cups: int = 9
        self.money: int = 550
        self.state: str = "choosing an action"
        self.fill_state = "fill_water"

    def __str__(self):
        return (f"The coffee machine has:\n"
                f"{self.water} of water\n"
                f"{self.milk} of milk\n"
                f"{self.beans} of coffee beans\n"
                f"{self.cups} of disposable cups\n"
                f"${self.money} of money\n")

    def display(self):
        if self.state == "choosing an action":
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state == "buy":
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif self.state == "fill":
            if self.fill_state == "fill_water":
                print("\nWrite how many ml of water do you want to add:")
            elif self.fill_state == "fill_milk":
                print("Write how many ml of milk do you want to add:")
            elif self.fill_state == "fill_beans":
                print("Write how many grams of coffee beans do you want to add:")
            elif self.fill_state == "fill_cups":
                print("Write how many disposable cups of coffee do you want to add:")
        else:
            pass

    def is_enough_resources(self, how_much_water: int = 0, how_much_milk: int = 0,
                            how_many_beans: int = 0, how_many_cups: int = 0) -> bool:
        if self.water - how_much_water < 0:
            print("Sorry, not enough water!")
            return False
        if self.milk - how_much_milk < 0:
            print("Sorry, not enough milk!")
            return False
        if self.beans - how_many_beans < 0:
            print("Sorry, not enough beans!")
            return False
        if self.cups - how_many_cups < 0:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self, user_input):
        if user_input == "1":
            if self.is_enough_resources(250, 0, 16, 1):
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif user_input == "2":
            if self.is_enough_resources(350, 75, 20, 1):
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif user_input == "3":
            if self.is_enough_resources(200, 100, 12, 1):
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
        elif user_input == "back":
            pass
        else:
            print("You made a wrong choice.")

    def remaining(self):
        print(self)

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def fill(self, user_input):
        if self.fill_state == "fill_water":
            self.water += int(user_input)
            self.fill_state = "fill_milk"
        elif self.fill_state == "fill_milk":
            self.milk += int(user_input)
            self.fill_state = "fill_beans"
        elif self.fill_state == "fill_beans":
            self.beans += int(user_input)
            self.fill_state = "fill_cups"
        elif self.fill_state == "fill_cups":
            self.cups += int(user_input)
            self.state = "choosing an action"
            self.fill_state = "fill_water"
            print()

    def work(self, user_input=""):
        if not user_input:
            if self.state == "remaining":
                print()
                self.remaining()
                self.state = "choosing an action"
            elif self.state == "take":
                print()
                self.take()
                self.state = "choosing an action"
            self.display()
        elif user_input and self.state == "choosing an action":
            if user_input in ("buy", "fill", "take", "remaining", "exit"):
                self.state = user_input
            else:
                print("Give me a right action.\n")
        elif self.state == "buy":
            self.buy(user_input)
            print()
            self.state = "choosing an action"
        elif self.state == "fill":
            self.fill(user_input)
        else:
            print("Work: something is wrong.")


coffee_machine = CoffeeMachine()
action = "start"
while action != "exit":
    coffee_machine.work()
    action = input("> ")
    coffee_machine.work(action)
