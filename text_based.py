import time

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

def game_loop():
    gold = 10
    day = 1
    inventory = {"Seeds": 3, "Turnips": 0}
    plots = [None, None, None]

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

#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------CHOICE 1-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

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
            print("3. Harvest a mature crop")
            farm_choice = input("Enter choice: ").strip()
            while farm_choice not in ["1", "2", "3"]:
                print("\nInvalid choice. Please enter 1, 2 or 3.")
                farm_choice = input("Enter choice: ").strip()
            if farm_choice == "1":
                while True:
                    try:
                        plot_num = int(input("\nEnter plot number to water (1-3): ")) - 1
                    except ValueError:
                        print("\nInvalid input. Please enter a number between 1 and 3.")
                        continue
                    else:
                        if 0 <= plot_num < len(plots):
                            if plots[plot_num] is not None:
                                plots[plot_num].water()
                            else:
                                print("\nThis plot is empty. You can't water it.")
                            break
                        else:
                            print("\nInvalid plot number. Please enter a number between 1 and 3.")

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
                                        print(f"znYou planted a seed in plot {plot_num + 1}.")
                                        break
                                    else:
                                        print("znThis plot is already occupied. You can't plant here.")
                                        break
                                else:
                                    print("\nYou don't have any seeds left to plant.")
                                    break
                            else:
                                print("\nInvalid plot number. Please enter a number between 1 and 3.")

            elif farm_choice == "3":
                while True:
                    try:
                        plot_num = int(input("Enter a plot number to harvest (1-3) ")) - 1
                    except ValueError:
                        print("Invalid input. Please enter a number between 1 and 3")
                    else:
                        if 0 <= plot_num < len(plots):
                            target_plant = plots[plot_num]
                            if target_plant is None:
                                print("\nThere is nothing growing here to harvest")
                                break
                            elif target_plant.is_withered:
                                print(f"\nThe {target_plant.name} is dead. You clear out the withered weeds.")
                                plots[plot_num] = None
                                break
                            elif target_plant.is_grown:
                                inventory["Turnips"] += 1
                                print(f"\nThe {target_plant.name} has been successfully harvested.")
                                plots[plot_num] = None
                                break
                            else:
                                print(f"\nThe {target_plant.name} isn't fully grown yet. Give it more time")
                                break
                        else:
                            print("\nInvalid plot number. Please enter a number between 1 and 3.")
                            
#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------CHOICE 1-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------CHOICE 2-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

        elif choice == "2":
            market_prices = {
                "Buy_Seed": 2,
                "Sell_Turnip": 8
            }

            while True:
                print("\n----------Welcome to the Harvest Valley Market----------")
                print(f"Your Gold: {gold}")
                print(f"Your Inventory: {inventory}")
                print(f"1. Buy Turnip Seed (-{market_prices["Buy_Seed"]} Gold)")
                print(f"2. Sell Mature Turnip (+{market_prices["Sell_Turnip"]} Gold)")
                print(f"3. Leave Market")
                try:
                    market_choice = int(input("\n Enter your choice (1-3): "))
                except ValueError:
                    print("Invalid input, enter a number from 1 to 3")
                else:
                    if 0 <= market_choice < 3:
                        if market_choice == 1:
                            if gold >= market_prices["Buy_Seed"]:
                                gold -= market_prices["Buy_Seed"]
                                inventory["Seeds"] += 1
                                print("\nYou successfully bought 1 Turnip Seed.")
                                time.sleep(1)
                            else:
                                print("\nYou do not have enough gold to buy a seed.")
                                time.sleep(1)

                        if market_choice == 2:
                            if inventory["Turnips"] > 0:
                                inventory["Turnips"] -= 1
                                gold += market_prices["Sell_Turnip"]
                                print(f"You successfully sold 1 Turnip for {market_prices["Sell_Turnip"]} Gold, brining the total amount of Gold you have to {gold} Gold")
                                time.sleep(1)
                            else:
                                print("You do not have any mature Turnips to sell.")
                                time.sleep(1)

                        else:
                            print("\nYou walk back to your farm... ")
                            time.sleep(1)
                            break
#----------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------CHOICE 2-------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------
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