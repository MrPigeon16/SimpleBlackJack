import BlackJackClass
import BlackJackfunction
import time
BLACK_JACK = 21
HIT = 1
STAND = 0
DEALER_STAND = 17

def main():
    
    BlackJackfunction.welcome_msg()
    time.sleep(0.1)

    player = BlackJackClass.player()
    dealer = BlackJackClass.player()

    player.hit()
    print(f"Your total is {player.sum()}")
    dealer.hit()
    print(f"the dealer total is {dealer.sum()}")
    
    time.sleep(1)
    while(player.sum() <= BLACK_JACK):
        todo = int(input("press 1 to HIT, and 0 to STAND: "))
        if todo == HIT:
            player.hit()
            print(f"Your total is {player.sum()}")
            if(player.sum() == BLACK_JACK):
                print("BLACKJACK, you have won the game! ")
                break
            time.sleep(0.5)
        else:
            break
    

    if player.sum() != BLACK_JACK:

        if(player.sum() > BLACK_JACK):
            print("SORRY, You have lost you are busted, DEALER WINS!")
        else:

            print("alright, let's see what the dealer have to offer!")
            time.sleep(1)
            while(dealer.sum() < DEALER_STAND):
                dealer.hit()
                print(f"the dealer total is {dealer.sum()}")
                time.sleep(0.5)
        
            time.sleep(1)
            if(dealer.sum() == BLACK_JACK):
                print("The Dealer win!")
            elif(dealer.sum() == player.sum()):
                print("THIS IS A PUSH, nobody win -_-")
            elif(dealer.sum() > BLACK_JACK):
                print("The dealer busted, PLAYER WIN!")
            elif(dealer.sum() > player.sum()):
                print("DEALER WIN!")
            else:
                print("PLAYER WIN!")
        
        
if __name__ == "__main__":
    main()