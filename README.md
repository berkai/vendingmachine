## UML Diagrom of the algorithm

![vendingmachine](https://user-images.githubusercontent.com/20394555/140628102-c805f1f8-9927-4d51-8674-183bff1db9d3.jpeg)

### Specs

- No operation is performed while "maintenance mode" is on.
- Operator easiliy change the allowed coins from config.
- User can see available stocks.
- User can choose an item also insert cash into the vending machine.
- Vending Machine can track of the inserted deposit amount with the price of the selected item.
- Vending machine must display an option to cancel the operation.
- User gets the selected item and the back change with the allowed coins.

### What should I add?

- User cannot see the stock changes instantly.
- Stock quantity changes must applied immediately
- Price could be also able to change from config.
- Adding some constant strings for the logging.

### Usage

- **python3.9**

```bash
python3 main.py
```
