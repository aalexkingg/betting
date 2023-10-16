import urllib.request as ul
from bs4 import BeautifulSoup as soup


def get_bets(tournament, verbose=False):
    if verbose:
        print("\n ------------- ( " + tournament + " ) -----------------")

    football_url = "https://easyodds.com/football/" + tournament
    print(football_url)

    req = ul.Request(football_url)

    client = ul.urlopen(req)
    htmldata = client.read()
    client.close()

    pagesoup = soup(htmldata, "html.parser")
    row = pagesoup.findAll('a', {"class": "eo-match"})

    if verbose:
        print(row , " : this is the bets fetched from website")
        
    bets = []

    for item in row:
        # Get home team object
        home = item.find_next('span', {'class': 'match-side itm-side1'})
        # Get draw object
        draw = item.find_next('span', {'class': 'draw-odds'})
        # Get away team object
        away = item.find_next('span', {'class': 'match-side itm-side2'})

        # Get data from home object
        home_name = home.find_next('span', {'class': 'side-name'}).text.strip()
        home_bet = home.find_next('span', {'class': 'side-odds'}).text.strip()

        draw_bet = draw.text.strip()

        # Get data from away object
        away_name = away.find_next('span', {'class': 'side-name'}).text.strip()
        away_bet = away.find_next('span', {'class': 'side-odds'}).text.strip()

        if verbose:
            print(home_name + " vs " + away_name)
            print(home_bet + " " + draw_bet + " " + away_bet)

        # Calculate bet odds as decimal
        bet1 = float(home_bet.split("/")[0]) / float(home_bet.split("/")[1])
        bet2 = float(draw_bet.split("/")[0]) / float(draw_bet.split("/")[1])
        bet3 = float(away_bet.split("/")[0]) / float(away_bet.split("/")[1])

        bets.append([home_name, away_name, bet1, bet2, bet3])

    return bets


class PayPal:
    """
    PayPal API:
        - Uses HTTP posting to communicate with paypal via web
        - Posting requires credentials
        - Researching how to post to paypal in order to transfer money

    Functions:
        - Send Money (Via address)
        - Check Balance
        - Get recent transactions

    """

    def __int__(self):
        pass

    def call(self):
        ...


class Bookies:
    """
    Bookies API:

    """

    balance = 0
    active_bets = []

    def __init__(self):
        self.tick()

    def tick(self):
        """
        THIS FUNCTION NEEDS TO BE CALLED AT THE START OF EVERY OTHER FUNCTION
        :return:
        """
        self.update_balance()

    def update_balance(self) -> None:
        pass

    def get_balance(self) -> float:
        self.tick()
        return self.balance

    def make_bet(self, amount: float):
        self.tick()

        # If bet amount is below balance (should probably be a lot less than current balance)

        # Then place bet

    def get_bets(self) -> list:
        """Returns list of all active bets"""
        self.tick()
        return self.active_bets

