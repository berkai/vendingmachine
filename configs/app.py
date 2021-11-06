from os import environ as env


class AppConfig:
    LOG_LEVEL = env.get("LOG_LEVEL", "info").upper()
    LOG_COLORIZE = env.get("LOG_COLORIZE", "false").lower() == "true"
    STOCKS = {
    0: {'name': 'Magnum', 'price': 6},
    1: {'name': 'Oreo', 'price': 6},
    2: {'name': 'Duracell', 'price': 7},
    3: {'name': 'Avocado', 'price': 12},
    4: {'name': 'Fanta', 'price': 16},
    5: {'name': 'Capri-Sun', 'price': 14}
    }
    ALLOWED_COINS = env.get("ALLOWED_COINS", [1, 5, 10, 20, 50])