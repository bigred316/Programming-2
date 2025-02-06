
thing1 = int(input("what is the value of your first card"))
thing2 = int(input("what is the value of your first card"))


def blackjack(card1, card2):
    cardtotal = card1 + card2
    if card1 == card2:
        print("Split")
    if (cardtotal < 17):
        print("Hit")
    else:
        return("Stand")
    while cardtotal < 22:
        cardtotal += int(input("WHat is the value of the card you drew"))
        if (cardtotal < 17):
            print("Hit")
        else:
            return("Stand")
    return("You busted")
blackjack(thing1, thing2)
