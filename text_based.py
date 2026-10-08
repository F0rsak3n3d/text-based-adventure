import time

def game_loop():
    gold = 10
    day = 1
    inventory = {"Seeds": 3, "Turnips": 0}
    plots = [None, None, None]

#----------------------------------------------------------------------
#------------------------------CROP LOGIC------------------------------
#----------------------------------------------------------------------

    class Crops:
        def __init__(self, name, days_to_grow):
            self.name = name
            self.days_to_grow = days_to_grow
            self.current_growth = 0
            self.water_level = 0
            self.is_withered = False
            self.is_grown = False

        def water(self):
            if not self.is_withered and not self.is_grown:
                self.water_level = 1
                print(f"You watered the {self.name}.")
            elif self.is_grown:
                print(f"The {self.name} is already fully grown and ready to harvest.")

        def advance_day(self):
            if self.is_withered or self.is_grown:
                return

            if self.water_level == 1:
                self.current_growth += 1
                self.water_level = 0

                if self.current_growth >= self.days_to_grow:
                    self.is_grown = True

            else:
                self.is_withered = True

#----------------------------------------------------------------------
#------------------------------CROP LOGIC------------------------------
#----------------------------------------------------------------------


    print("Welcome to Terra Valley")
    print("------------------------------")

    while True:
        print(f"\n Day {day} | Gold: {gold} | Inventory: {inventory}")
        print("What would you like to do?")
        print("1. Tend to your farm")
        print("2. Visit the market")
        print("3. Sleep (End the day)")
        print("4. Save and Quit the game")

        while True:
            try:
                choice = input("\nEnter your choice (1-4): ").strip()

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                
            else:
                if choice in ["1", "2", "3", "4"]:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")

        if choice == "1":
            print("\n[Action] Checking fields... Your crops look healthy")
            time.sleep(1)
        elif choice == "2":
            print("\n[Action] Walking to the market...")
            time.sleep(1)
        elif choice == "3":
            day += 1
            print(f"\n[Action] You sleep peacefully. Welcome to Day {day}.")
            time.sleep(1)
        elif choice == "4":
            print("\nThanks for playing Terra Valley. Saving your farm...")
            break
game_loop()