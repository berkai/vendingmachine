from utils.logging import Logger
from configs import AppConfig
from .calculator import Calculator


class VendingMachine(object):
    calc = Calculator()

    def display_stock(self):
        return [AppConfig.STOCKS[item]["name"] for item in range(len(AppConfig.STOCKS))]

    def get_price(self, amount):
        '''
        you can see which items you can buy
        :param amount: deposited total coins
        :return: product names and codes of the snacks
        '''
        item_names = [AppConfig.STOCKS[item]["name"]
                      for item in range(len(AppConfig.STOCKS)) if AppConfig.STOCKS[item]["price"] <= int(amount)]
        Logger.debug(f"item names: {item_names}")

        item_keys = [key for key, value in AppConfig.STOCKS.items() if value["name"] in item_names]
        Logger.debug(f"item keys: {item_keys}")

        names_and_keys = [list(t) for t in zip(item_names, item_keys)]
        Logger.debug(f"item names and keys: {names_and_keys}")

        return names_and_keys

    def get_snacks_with_codes(self):
        '''
        :return: a list that show codes with names of the snacks
        '''
        return [{"code": item, "name": AppConfig.STOCKS[item]["name"], "price": AppConfig.STOCKS[item]["price"]}
                for item in range(len(AppConfig.STOCKS))]

    def get_selected_snack_with_item_code(self, item_code):
        '''

        :param item_code: snack code
        :return:
        '''
        try:
            return AppConfig.STOCKS[item_code]["name"], AppConfig.STOCKS[item_code]["price"]
        except Exception as ex:
            Logger.info(f"Selected item code is not valid. Item Code: {item_code}")

    def check_coin(self, coin):
        if int(coin) in AppConfig.ALLOWED_COINS:
            return True
        else:
            Logger.info(
                f"Insert a coin from the following coins list: [{'$, '.join(map(str, AppConfig.ALLOWED_COINS))}]")

    def bool_question(self, answer):
        '''
        User's response for a single question
        :param answer: 'y' or 'n'
        :return: boolean
        '''
        if answer.lower() in ["y", "n"]:
            if answer == "y":
                return True
            else:
                return False
        else:
            Logger.info(f"We are not understand your answer. Your answer is: {answer}")

    def insert_coin(self, snack_code, amount):
        '''
        when an user insert a coin machine asks to the user are you willing to add more money or nott
        :param amount:deposited amount to the machine
        :return: total deposited to the machine
        '''
        item_name, item_price = self.get_selected_snack_with_item_code(item_code=int(snack_code))
        customer_answer = input('Would you like to add money?:\n [Y/N]\n')
        if self.bool_question(customer_answer):
            while True:
                Logger.info(
                    f"Insert a coin from the following coins list: [{'$, '.join(map(str, AppConfig.ALLOWED_COINS))}]")
                adding_amount = input('\n ')
                if self.check_coin(int(adding_amount)):
                    amount += int(adding_amount)
                    Logger.info(f"amount added: {adding_amount}")
                    if amount >= item_price:
                        break
                    else:
                        Logger.info(f"You can't buy the {item_name} with {amount} coins.\n")
        else:
            Logger.info(f"You can' buy the {item_name} with {item_price} coins. Here is your coins: {amount}\n")
        Logger.info(f"amount: {amount}")

        return amount

    def buy_ops(self, snack_code, added_amount):

        item_name, item_price = self.get_selected_snack_with_item_code(int(snack_code))
        Logger.info(f"Selected snack with price: {item_name, item_price}\n")
        customer_answer = input(f'Would you like to buy the {item_name}?:\n [Y/N]\n')

        if self.bool_question(customer_answer):
            Logger.info(f"Selected snack price and amount: {item_price, added_amount}\n")
            while self.calc.check_price(item_price, int(added_amount))==True:
                Logger.info(f"Selected {item_name} has been bought\n"
                            f"Bon Appetit\n")
                self.insert_coin(snack_code, added_amount)

            Logger.info(f"Selected {item_name} has been bought\n"
                        f"--------Bon Appetit--------\n")
        else:
            Logger.info(f"See you again! Here is your money: {added_amount} coins\n")