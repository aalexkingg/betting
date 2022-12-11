#
# Got to think about bes tway to automate getting bets for sports, and the leagues in those sports
#  E.g Premier league in football
# i reckon at the moment we just focus on getting a program where it takes the bets from the website and reports back the profitable matches and the possible bets
## and worry about the automation later

from bets import get_bets
from core import points
from paypal_bridge import PayPal
from bookies_bridge import Bookies

##############################################
#
# Main program should loop infinitely in order
# to check and make the bets, see nas bets can
# be updated.
#
# Bets may be updated from non-profitable to
# profitable.
#
# Program also needs to take winnings, move it
# back to PayPal, and distribute where
# necessary in case of low balance on other
# bookies site.
#
##############################################


def main():

    competition = ['premier-league',
                   'uefa-champions-league',
                   'world-cup',
                   'championship',
                   'la-liga',
                   'uefa-europa-league']

    for i in range(len(competition)):

        print(" ---------- { " + competition[i] + " } ----------")

        tournament = get_bets(tournament=competition[i])

        for match in tournament:
            ##print(match)

            home_name = match[0]
            away_name = match[1]

            bet1 = match[2]
            bet2 = match[3]
            bet3 = match[4]

            profitable_bets = points(bet1, bet2, bet3, precision=3)
            bet1Win = 0
            bet2Win = 0
            bet3Win = 0
            # If list is not empty, profitable bets exist
            if profitable_bets:
                print(match)
                # Find bet in bookies and make bet
                highestTotal = 0
                bestCombo = []
                for bets in profitable_bets:
                    if(highestTotal<bets[0]*bet1 + bets[1]*bet2 + bets[2]*bet3 - (2*sum(bets))):
                        highestTotal = bets[0]*bet1 + bets[1]*bet2 + bets[2]*bet3 - (2*sum(bets))
                        bet1Win = bets[0] * bet1 - sum(bets) + bets[0]
                        print(bets[0] * bet1," ",sum(bets)," ",bet1)
                        bet2Win = bets[1] * bet2 - sum(bets) + bets[1]
                        bet3Win = bets[2] * bet3 - sum(bets)+ bets[2]
                        bestCombo = bets
                print("Profit : " , highestTotal)
                print("Best bet : ", bestCombo)
                print("Bet1 Profit " , bet1Win, " Bet2 Profit " , bet2Win, " Bet3 Profit " , bet3Win )
                print(" ")

if __name__ == "__main__":
    main()



