# -*- coding: utf-8 -*-
"""
Created on Sat May  8 23:51:39 2021

@author: Raza_Jutt
"""

import random 

cards = [x for x in range(1,53)]

labels = {1: "Ace",
          2: "2",
          3: "3",
          4: "4",
          5: "5",
          6: "6",
          7: "7",
          8: "8",
          9: "9",
          10: "10",
          11: "Jack",
          12: "Queen",
          13: "King"}

card_type = { 1 : "hearts  ", 
              2 : "clubs   ", 
              3 : "diamonds", 
              4 : "spades  "}

def display_Cards(cards):
    for i in cards:
        if i<=13 :
            print(card_type[1]+" -----   "+labels[i])
        elif i>13 and i<=26:
            print(card_type[2]+" -----   "+labels[i-13])
        elif i>26 and i<=39:
            print(card_type[3]+" -----   "+labels[i-26])
        else:
            print(card_type[4]+" -----   "+labels[i-39])
            
            
def shaffle_deck(display=0): # display 0=don't show  and 1=show cards  
    random.shuffle(cards)
    if display:
        print("_____Shuffled Deck_____")
        display_Cards(cards)
    return cards
       
def King_Queen(cards):
    for i in range(0,51):
        if cards[i]==12 or cards[i] ==25 or cards[i] ==38 or cards[i] ==51:   ## Queen Finded
            if cards[i+1] == 13 or cards[i+1] == 26 or cards[i+1] == 39 or cards[i+1] == 52: ## Searching for King in next index
                return 1,i
            elif i<51:
                if cards[i+2] == 13 or cards[i+2] == 26 or cards[i+2] == 39 or cards[i+2] == 52: ## Searching for King in next to next index
                    return 1,i
        
        
        if cards[i] == 13 or cards[i] == 26 or cards[i] == 39 or cards[i] == 52: ## King Finded
            if cards[i+1]==12 or cards[i+1] ==25 or cards[i+1] ==38 or cards[i+1] ==51: ## Searching for Queen in next index
                return 1,i
            elif i<51:
                if cards[i+2] == 12 or cards[i+2] == 25 or cards[i+2] == 38 or cards[i+2] == 51: ## Searching for Queen in next to next index
                    return 1,i
                
    return 0,0

#### Question 2 Part B : King and Queen consecutively or 1 card away

def main(numberOFexperiments=1):
    print("#############################################")
    count = 0
    for i in range(numberOFexperiments):
        shaffle_deck()   ## Shaffle deck
        situation , atNumber = King_Queen(cards)
        if situation:
            count += 1
            print("  ")
            print(" Experiment : "+ str(i+1))
            print(" At location: "+ str(atNumber))
            print("  ")
            display_Cards(cards)
            
    print("  ")
    print(" Number of Occurrence : "+ str(count))
    print(" Totall Experiment    : "+ str(numberOFexperiments))
    print(" Probability of two Consecutive King and Queen    : ",end=(""))
    print(count/numberOFexperiments)
    print("  ")


### for Q2 Part: B call n number of experiment
numberOFexperiments = int(input("Enter number of Experiments on Consecutive Queen : "))
main(numberOFexperiments)