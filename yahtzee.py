from random import randint
import time
import json
import collections

def roll_a_dice():

    return randint(1,6)

class Turn(object):
   
    def __init__(self):

        self.dice_values = []
        self.throw_number = 0


    def throw_multiple_dice(self, number_of_dice):

        for i in range(0,number_of_dice):

            self.dice_values.append(roll_a_dice())
            #order the list?

        return    
       

    def take_turn(self):
        
        #A turn is up to and including 3 individual throws of 5 or less dice
        self.throw_multiple_dice(5)
        self.throw_number += 1

        #Print result and throw number
        def show_throw_and_dices():
            print "This is throw number %s" % (self.throw_number)
            time.sleep(1.0)
            print "Your dice values are %s" % (self.dice_values)
            time.sleep(1.0)
        
        show_throw_and_dices()

        #Ask whether to throw again
        choice = raw_input("Would you like to roll again (you can re-roll a maximum of 5 dice?) [Y/N] ")

        time.sleep(1.0)

        if choice == "n":
            print ("End of your turn. Your dice values are %s" % self.dice_values)
            return
        
        #Ask which numbers to re-roll
        def additional_throw():
            dices_to_re_roll = raw_input("Which dice do you want to re-roll? ")
            
            time.sleep(1.0)

            numbers_to_re_roll = map(int, dices_to_re_roll.split()) 

            print "You want to re-roll %s ? " % numbers_to_re_roll + ""

            time.sleep(1.0)

            for value in numbers_to_re_roll:
                if value in (self.dice_values):
                    self.dice_values.remove(value)
                else:
                    pass
            print "Your remaining dice are %s " % self.dice_values +""
            time.sleep(1.0)

                          
                #Throw replacement dices
            self.throw_multiple_dice(len(numbers_to_re_roll))

            self.throw_number += 1

        additional_throw()
        
        #Print result and throw number
        show_throw_and_dices()

        #Ask whether to throw again
        choice = raw_input("Would you like to roll again (you can re-roll a maximum of 5 dice?) [Y/N] ")

        time.sleep(1.0)

        if choice == "n":
            print ("End of your turn. Your dice values are %s" % self.dice_values)
            return     

        additional_throw()
        #Print result and throw number

        show_throw_and_dices()

        print "This is the end of your turn. Your dices values are %s" % self.dice_values

class Scorecard(object):

    def __init__(self):

        self.values = {"1's":"empty" , "2's":"empty" , "3's":"empty" , "4's":"empty" , "5's": "empty" , "6's": "empty" , "3 of a kind" : "empty" , "4 of a kind" : "empty" , "low run" : "empty" , "high run" : "empty" , "full house" : "empty", "sum" : "empty" , "yahtzee" : "empty"}
        
    def show_scorecard(self):    
        
        print(json.dumps(self.values, indent=4, sort_keys=True))
    
    def take_1s(self, dices):
        
        sum_of_1s = 0
        
        for dice in dices:
            if dice == 1:
                sum_of_1s +=1
        
        self.values["1's"] = sum_of_1s
    
    def take_2s(self, dices):

        sum_of_2s = 0

        for dice in dices:
            if dice == 2:
                sum_of_2s +=2
        
        self.values["2's"] = sum_of_2s
    
    def take_3s(self, dices):
        
        sum_of_3s = 0
        
        for dice in dices:
            if dice == 3:
                sum_of_3s +=3
        
        self.values["3's"] = sum_of_3s
    
    def take_4s(self, dices):
        
        sum_of_4s = 0
        
        for dice in dices:
            if dice == 4:
                sum_of_4s +=4
        
        self.values["4's"] = sum_of_4s

    def take_5s(self, dices):
        
        sum_of_5s = 0
        
        for dice in dices:
            if dice == 5:
                sum_of_5s +=5
        
        self.values["5's"] = sum_of_5s

    def take_6s(self, dices):
        
        sum_of_6s = 0
        
        for dice in dices:
            if dice == 6:
                sum_of_6s +=6
        
        self.values["6's"] = sum_of_6s    

    def three_of_kind(self, dices, chosen_value):

        count = 0
        three_of_a_kind = 0        
            
        for dice in dices:
            if  dice == chosen_value and count < 3:
                three_of_a_kind += chosen_value
                count += 1
        
        self.values["3 of a kind"] = three_of_a_kind

    def no_three_of_a_kind(self):

        self.values["3 of a kind"] = "x"        

    def four_of_kind(self, dices, chosen_value):
        count = 0
        four_of_a_kind = 0        
            
        for dice in dices:
            if  dice == chosen_value and count < 4:
                four_of_a_kind += chosen_value
                count += 1
        
        self.values["4 of a kind"] = four_of_a_kind  
    
    def no_four_of_a_kind(self):

        self.values["4 of a kind"] = "x"

    def low_run(self, dices):

        self.values["low run"] = 40

    def no_low_run(self, dices):

        self.values["low run"] = "x"
    
    def high_run(self, dices):
        
        self.values["high run"] = 40

    def no_high_run(self, dices):
        
        self.values["high run"] = "x"

    def no_full_house(self):

        self.values["full house"] = "x"
    
    def full_house(self, dices):

        self.values["full house"] = 30    
    
    def sum_of(self,dices):
        
        total = 0

        for dice in dices:
            total += dice
        
        self.values["sum"] = total

    def yahtzee(self,dices):
        
        self.values["yahtzee"] = 100

    def noyahtzee(self, dices):

        self.values["yahtzee"] = "x"

    def total_score(self):

        totalscore = 0

        for key in self.values:
            if self.values[key] == "x":
                totalscore += 0
            else: totalscore += int(self.values[key])
         
        print totalscore

def game():

    scorecard = Scorecard()

    
    while "empty" in scorecard.values.values():

        turn = Turn()
        turn.take_turn()
        scorecard.show_scorecard()

        while True:
                choice = raw_input("What would you like to take?")

                if choice == "quit":
                    return
                
                if choice == "1s" and scorecard.values["1's"] != 'empty':
                    print "You have already taken 1's"
                    continue

                if choice == "1s":
                    scorecard.take_1s(turn.dice_values)
                    break

                if choice == "2s" and scorecard.values["2's"] != 'empty':
                    print "You have already taken 2's"
                    continue                      
  
                elif choice == "2s":
                    scorecard.take_2s(turn.dice_values)
                    break

                if choice == "3s" and scorecard.values["3's"] != 'empty':
                    print "You have already taken 3's"
                    continue

                elif choice == "3s":
                    scorecard.take_3s(turn.dice_values)
                    break


                if choice == "4s" and scorecard.values["4's"] != 'empty':
                    print "You have already taken 4's"
                    continue

                elif choice == "4s":
                    scorecard.take_4s(turn.dice_values)
                    break

                if choice == "5s" and scorecard.values["5's"] != 'empty':
                    print "You have already taken 5's"
                    continue

                elif choice == "5s":
                    scorecard.take_5s(turn.dice_values)
                    break

                if choice == "6s" and scorecard.values["6's"] != 'empty':
                    print "You have already taken 6's"
                    continue                
                
                elif choice == "6s":
                    scorecard.take_6s(turn.dice_values)
                    break

                if choice == "3 of a kind" and scorecard.values["3 of a kind"] != 'empty':
                    print "You have already taken 3 of a kind"
                    continue

                elif choice == "3 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)

                    if turn.dice_values.count(number) < 3:
                        print "You don't have 3 of that number"
                        decision = raw_input("Do you still want to take 3 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else: scorecard.no_three_of_a_kind
                        break
                    else: scorecard.three_of_kind(turn.dice_values,number)
                    break

                if choice == "4 of a kind" and scorecard.values["4 of a kind"] != 'empty':
                    print "You have already taken 4 of a kind"
                    continue

                elif choice == "4 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)
                    
                    if turn.dice_values.count(number) < 4:
                        print "You don't have 4 of that number"
                        decision = raw_input("Do you still want to take 4 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else:
                            scorecard.no_four_of_a_kind()
                            break
                    
                    else:
                        scorecard.four_of_kind(turn.dice_values, number)
                        break


                if choice == "low run" and scorecard.values["low run"] != 'empty':
                    print "You have already taken low run"
                    continue

                elif choice == "low run":
                    scorecard.low_run(turn.dice_values)
                    break

                if choice == "low run" and collections.Counter(turn.dice_values) == collections.Counter([1,2,4,5,3]):
                    scorecard.low_run(turn.dice_values)
                    break

                elif choice == "low run" and collections.Counter(turn.dice_values) != collections.Counter([2,3,4,5,1]):
                    scorecard.no_low_run(turn.dice_values)
                    break

                if choice == "high run" and scorecard.values["high run"] != 'empty':
                    print "You have already taken high run"
                    continue

                if choice == "high run" and collections.Counter(turn.dice_values) == collections.Counter([2,3,4,5,6]):
                    scorecard.high_run(turn.dice_values)
                    break

                elif choice == "high run" and collections.Counter(turn.dice_values) != collections.Counter([2,3,4,5,6]):
                    scorecard.no_high_run(turn.dice_values)
                    break

                if choice == "full house" and scorecard.values["full house"] != 'empty':
                    print "You have already taken full house"
                    continue

                if choice == "full house":
                    countvalues = collections.Counter(turn.dice_values)
                    if countvalues.values() == [2,3] or countvalues.values() == [3,2] or countvalues.values() == [5]:
                        scorecard.full_house(turn.dice_values)
                        break
                    else: scorecard.no_full_house()
                    break

                if choice == "sum" and scorecard.values["sum"] != 'empty':
                    print "You have already taken sum"
                    continue

                elif choice == "sum":
                    scorecard.sum_of(turn.dice_values)
                    break

                if choice == "yahtzee" and scorecard.values["yahtzee"] != 'empty':
                    print "You have already taken yahtzee"
                    continue

                elif choice == "yahtzee" and collections.Counter(turn.dice_values) == collections.Counter([6,6,6,6,6]):
                    scorecard.yahtzee(turn.dice_values)
                    break

                elif choice == "yahtzee" and collections.Counter(turn.dice_values) != collections.Counter([6,6,6,6,6]):
                    scorecard.noyahtzee(turn.dice_values)
                    break

     

        scorecard.show_scorecard()

    print "End of Game. Your final score is %s" % scorecard.total_score()
    
game()

