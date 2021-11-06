from utils.logging import Logger
from configs import AppConfig

from random import randint

class Calculator(object):

    def cashback_calc(self, snack_price, amount):
        '''

        :param snack_price: price of the willing to buy item
        :param amount: amount of inserted coin
        :return: coins list of the change
        example: changes_coins = [1,5,1,1] that means we are return 8 coins that contains one 5 coin
                                three 1 coins
        '''
        change = amount - snack_price
        Logger.info(f"Your change is :{change}\n")
        changes_coins = [coin for coin in AppConfig.ALLOWED_COINS if coin < change]
        while True:
            changes_coins.append(changes_coins[randint(0, len(changes_coins) - 1)])
            if sum(changes_coins) >= change:
                if sum(changes_coins) > change:
                    changes_coins.pop()
                if sum(changes_coins) == change:
                    break

        return changes_coins

    def check_price(self, snack_price, amount):
        '''
        :param snack_price: the price of snack
        :param amount: the amount of user given the machine
        if deposited amount bigger or not equal to the snack we kindly ask to the user insert more coin
        '''

        if amount - snack_price > 0:
            Logger.info(f"Thank you so much. Take your snack below also do not forget to get change")
            Logger.info(f"Here is the cashback :\n[{'$, '.join(map(str, self.cashback_calc(snack_price, amount)))}]")
            return True
        else:
            return False



