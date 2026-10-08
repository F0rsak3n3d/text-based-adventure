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


    print("Welcome to Harvest Valley.")
    print("------------------------------")

    while True:
        print(f"\n Day {day} | Gold: {gold} | Inventory: {inventory}")
        print("\nWhat would you like to do?")
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
            print("\n-----Your Farm Fields-----")
            for i, plant in enumerate(plots):
                if plant is None:
                    print(f"Plot {i+1}: [ Empty Dirt ]")
                elif plant.is_withered:
                    print(f"Plot {i+1}: [ Withered {plant.name} ]")
                elif plant.is_grown:
                    print(f"Plot {i+1}: [ Mature {plant.name} | Ready to harvest ]")
                else:
                    status = "Watered" if plant.water_level == 1 else "Dry"
                    print(f"Plot {i+1}: [ {plant.name} | Growth: {plant.current_growth}/{plant.days_to_grow} | Status: {status}]")

            print("\nWhat would you like to do?")
            print("1. Water a crop")
            print("2. Plant a seed")
            farm_choice = input("Enter choice: ").strip()
            while farm_choice not in ["1", "2"]:
                print("Invalid choice. Please enter 1 or 2.")
                farm_choice = input("Enter choice: ").strip()
            if farm_choice == "1":
                while True:
                    try:
                        plot_num = int(input("Enter plot number to water (1-3): ")) - 1
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 3.")
                        continue
                    else:
                        if 0 <= plot_num < len(plots):
                            if plots[plot_num] is not None:
                                plots[plot_num].water()
                            else:
                                print("This plot is empty. You can't water it.")
                            break
                        else:
                            print("Invalid plot number. Please enter a number between 1 and 3.")

            elif farm_choice == "2":
                if inventory["Seeds"] > 0:
                    while True:
                        try:
                            plot_num = int(input("Enter plot number to plant a seed (1-3): ")) - 1
                        except ValueError:
                            print("Invalid input. Please enter a number between 1 and 3.")
                            continue
                        else:
                            if 0 <= plot_num < len(plots):
                                if inventory["Seeds"] > 0:
                                    if plots[plot_num] is None:
                                        plots[plot_num] = Crops("Turnip", 3)
                                        inventory["Seeds"] -= 1
                                        print(f"You planted a seed in plot {plot_num + 1}.")
                                        break
                                    else:
                                        print("This plot is already occupied. You can't plant here.")
                                        break
                                else:
                                    print("You don't have any seeds left to plant.")
                                    break
                            else:
                                print("Invalid plot number. Please enter a number between 1 and 3.")

        elif choice == "2":
            print("\n[Action] Walking to the market...")
            time.sleep(1)
        elif choice == "3":
            day += 1
            print(f"\n[Action] You sleep peacefully. Welcome to Day {day}.")
            for plant in plots:
                if plant is not None:
                    plant.advance_day()
            time.sleep(1)
        elif choice == "4":
            print("\nThanks for playing Terra Valley. Saving your farm...")
            break
game_loop()