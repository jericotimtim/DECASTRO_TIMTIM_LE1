game_library = {
    "Donkey Kong": {"Quantity": 3, "Cost": 2},
    "Super Mario Bros": {"Quantity": 5, "Cost": 3},
    "Tetris": {"Quantity": 2, "Cost": 1},
}

user_inventory = {
    "user_inventory": {
        "Donkey Kong": 0,
        "Super Mario Bros": 0,
        "Tetris": 0
    }
}

users = {}
admin_user = "admin"
admin_pass = "adminpass"
username = ""
password = ""
user_coins = 0
user_points = 0

def sign_up(username, user_coins, user_points):
    print("_" * 100)    
    print("\n> Create a new account")
    
    while True:
        try:
            username = str(input("\n\t> Enter your username: "))
            if username in users:
                print("\n\t\t>> Username already exists. Please enter a different username.")
                continue
            else:
                password = str(input("\t> Enter your password (must have at least 8 characters): "))
                while True:
                    try:
                        if len(password) >= 8:            
                            users[username] = {"password": password, "user_coins": user_coins, "user_points": user_points}
                            print(users)
                            print("\n\t\t>> You have successfully signed up to AA Game Rentals.")
                            main_menu(username, user_coins, user_points)
                            break
                        else:
                            print("\n\t\t>> Your password must have at least 8 characters.")
                            sign_up(username, user_coins, user_points)
                            break
                    except ValueError:
                        print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                        sign_up(username, user_coins, user_points)
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_up(username, user_coins, user_points)

def sign_in(username, user_coins, user_points):
    print("_" * 100)   
    print("\n> Sign in to your account")
    
    while True:
        try:
            username = str(input("\n\t> Enter your username: "))
            password = str(input("\t> Enter your password: "))
        
            if users[username]['password'] == password:
                users[username].update(user_inventory)
                print("\n\t\t>> You have signed in successfully to AA Game Rentals.\n")
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Your log-in details are incorrect. Please try again.")
                sign_in(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_in(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Your log-in details are incorrect. Please try again.")
            sign_in(username, user_coins, user_points)

def sign_admin(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Sign in as Administrator")

    while True:
        try:
            adm_user = str(input("\n\t> Enter your username: "))
            adm_pass = str(input("\t> Enter your password: "))
        
            if admin_user == adm_user and admin_pass == adm_pass:
                print("\n\t\t>> You have signed in successfully.")
                admin_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Your log-in details are incorrect. Please try again.")
                sign_admin(username, user_coins, user_points)
                break
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            sign_admin(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Your log-in details are incorrect. Please try again.")
            sign_admin(username, user_coins, user_points)

def display_games(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Display Games")

    while True:
        i = 1
        for games in game_library:
            print(f"\n{i}. {games}")
            i += 1
            for details in game_library[games]:
                print(f"{details}: {game_library[games][details]}")

        try:
                choice = str(input("\n\t> Would you like to go back to the user menu? (Y/N) "))
                if choice == 'N' or choice == 'n':
                    continue
                elif choice == 'Y' or choice == 'y':
                    user_menu(username, user_coins, user_points)
                    break
                else:
                    print("\n\t\t>> Invalid input. Please try again.")
                    continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            display_games(username, user_coins, user_points)

def rent_game(username, user_coins, user_points):
    mod_points = 0

    print("_" * 100)
    print("\n> Rent Game")

    while True:
        i = 1
        for games in game_library:
            print(f"\n{i}. {games}")
            i += 1
            for details in game_library[games]:
                print(f"{details}: {game_library[games][details]}")
        try:
            game_choice = str(input("\n\t> Kindly refer to the game library and type the name of your selected game: ")).lower().title()

            if game_choice in game_library:
                if game_library[game_choice]['Quantity'] > 0:
                    if users[username]['user_coins'] >= game_library[game_choice]['Cost']:
                        game_library[game_choice]['Quantity'] -= 1
                        users[username]['user_coins'] -= game_library[game_choice]['Cost']
                        users[username]['user_inventory'][f'{game_choice}'] += 1
                        print(f"\n\t\t>> You have rented {game_choice} for {game_library[game_choice]['Cost']} coins! You now have a total of {users[username]['user_coins']} coin/s.")
                        if game_library[game_choice]['Cost'] >= 2:
                            mod_points = int(game_library[game_choice]['Cost'] / 2)
                            users[username]['user_points'] += mod_points
                            print(f"\t\t>> You have earned {mod_points} point/s from your purchase! You now have a total of {users[username]['user_points']} point/s.")
                    else:
                        print("\n\t\t>> You do not have enough coins! Please top-up your account on the user menu.")
                        user_menu(username, user_coins, user_points)
                        break
                elif game_library[game_choice]['Quantity'] <= 0:
                    try:
                        stock_choice = str(input(f"\n\t\t>> {game_choice} is currently out of stock. Would you like to choose another game? (Y/N) "))
                        if stock_choice == 'Y' or stock_choice == 'y':
                            continue
                        elif stock_choice == 'N' or stock_choice == 'n':
                            user_menu(username, user_coins, user_points)
                            break
                        else:
                            print("\n\t\t>> Invalid input. Please try again.")
                            continue
                    except ValueError:
                        print("\n\t\t>> [ValueError] Invalid input. Please try again.")
                        rent_game(username, user_coins, user_points)
            else:
                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) rent another game or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                rent_game(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            rent_game(username, user_coins, user_points)

def return_game(username, user_coins, user_points):
    print("_" * 100)
    print("\n> Return Game\n")
    
    while True:
        print("\n> Here is the list of your currently rented games:")

        i = 1
        for rented_games in users[username]['user_inventory']:
            print(f"\n{i}. {rented_games}")
            print(f"Inventory: {users[username]['user_inventory'][rented_games]}")
            i += 1

        try:
            return_item = str(input("\n\t> Kindly refer to the game library and type the name of the game that you want to return: ")).lower().title()
            if return_item in game_library:
                return_qty = int(input("\t> How many copies would you like to return? "))
                if return_qty <= users[username]['user_inventory'][f'{return_item}']:
                    users[username]['user_inventory'][f'{return_item}'] -= return_qty
                    game_library[return_item]['Quantity'] += return_qty
                    print(f"\n\t\t>> You have returned {return_qty} copy/ies of {return_item}. You now have {users[username]['user_inventory'][f'{return_item}']} stock/s of {return_item} in your inventory. Thank you for renting from AA Game Rentals!")
                else:
                    print(f"\n\t\t>> You do not have enough copies of {return_item} to return. Please try again.")
                    return_game(username, user_coins, user_points)
                    break
            else:
                print("\n\t\t>> Game is not available. Please enter a game within our selection.")
                continue       
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)
        except KeyError:
            print("\n\t\t>> [KeyError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)
        
        try:
            choice = str(input("\n\t> Would you like to (A) return another game or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                return_game(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                user_menu(username, user_coins, user_points)
                break
            else:
                print("\n\t\t>> Invalid input. Please try again.")
                continue
        except ValueError:
            print("\n\t\t>> [ValueError] Invalid input. Please try again.")
            return_game(username, user_coins, user_points)

def topup_account(username, user_coins, user_points):
    topup_user_coins = 0

    print("_" * 100)
    print("\n> Top-up Account")

    while True:
        try:
            topup_user_coins = int(input("\n\t> Enter the amount of coins to add to your account: "))
            users[username]['user_coins'] += topup_user_coins
            print(f"\n\t\t>> You have topped up {topup_user_coins} coin/s. You now have a total of {users[username]['user_coins']} coin/s.")
        except ValueError:
            print("\n\t\t>> Invalid input. Please try again.")
            topup_account(username, user_coins, user_points)

        try:
            choice = str(input("\n\t> Would you like to (A) top-up again or (B) go back to the user menu? (A/B) "))
            if choice == 'A' or choice == 'a':
                topup_account(username, user_coins, user_points)
                break
            elif choice == 'B' or choice == 'b':
                 
