from utils.logging import Logger
from configs import AppConfig
from machine import vending_machine as vm

import time
def display_menu(operation):
    '''
    all ops about the vending machine
    :param operation:
    :return:
    '''
    vending_machine = vm.VendingMachine()

    if operation == "1":
        Logger.info(f"list of available snacks:\n{vending_machine.display_stock()}\n")

    elif operation == "2":
        Logger.info(f"All snacks with codes: {vending_machine.get_snacks_with_codes()}\n")
        snack_code = input("Please enter snack code:\n ")
        item_name, item_price = vending_machine.get_selected_snack_with_item_code(int(snack_code))
        Logger.info(f"Selected snack name with price: {item_name, item_price}\n")
        customer_answer = input(f'Would you like to buy the {item_name}?:\n [Y/N]\n')
        if vending_machine.bool_question(customer_answer):
            Logger.info(f"Insert a coin from the following coins list: [{'$, '.join(map(str, AppConfig.ALLOWED_COINS))}]")
            amount = input('\n ')
            Logger.info(f"{item_name} selected. price is {item_price} and deposit amount is {amount}\n")
            # added_amount = vending_machine.insert_coin(int(snack_code), int(amount))
            if int(amount) >= item_price:
                vending_machine.buy_ops(int(snack_code), amount)
                Logger.info(f"Selected snack: {item_name}\n"
                            f"--------Bon Appetit--------\n")
            else:
                Logger.info(f"You can't buy {item_name} with {amount} coins!\n")
                added_amount = vending_machine.insert_coin(snack_code, int(amount))
                # items_and_keys = vending_machine.get_price(added_amount)
                vending_machine.buy_ops(int(snack_code), added_amount)
        else:
            customer_answer = input("Would you like to buy another snack?:\n [Y/N]\n")
            answer = vending_machine.bool_question(customer_answer)
            if answer:
                display_menu(operation)
            else:
                display_menu(input(get_all_ops()))

    elif operation == "3":

        Logger.info(f"Insert a coin from the following coins list: [{'$, '.join(map(str, AppConfig.ALLOWED_COINS))}]")
        amount = input('\n ')
        items_and_keys = vending_machine.get_price(int(amount))
        Logger.info(f"All snacks with codes: {vending_machine.get_snacks_with_codes()}\n")
        Logger.info(f"All snacks with can you buy without adding coins: {items_and_keys}\n")
        if vending_machine.check_coin(int(amount)):
            if len(items_and_keys) > 0:
                snack_code = input("Please enter snack code:\n ")
                vending_machine.buy_ops(int(snack_code), int(amount))
            else:
                Logger.info(f"You can't buy anything with {amount} coins!\n")
                snack_code = input("Please enter snack code or quit with  'q':\n ")
                if snack_code != "q":
                    added_amount = vending_machine.insert_coin(int(snack_code), int(amount))
                    items_and_keys = vending_machine.get_price(added_amount)
                    Logger.info(f"You can buy these items: {items_and_keys}\n")
                    snack_code = input(f"Please enter snack codes above:\n ")
                    vending_machine.buy_ops(int(snack_code), added_amount)
                else:
                    Logger.info("Come here with more money (0.0)"
                                f"Here is your money:{amount}")


    else:
        Logger.info('You have not chosen a valid option, please try again.')

    display_menu(input(get_all_ops()))

def get_all_ops():
    operation_names = '''Select operation:
    [1] List All Snacks
    [2] Select Snack
    [3] Insert Coin
    '''
    return operation_names

if __name__ == '__main__':
    while AppConfig.MAINTENANCE_MODE:
        operation = input(get_all_ops())
        display_menu(operation)
        time.sleep(5)