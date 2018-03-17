"""
A program to probablistically determine the optimal play for a round of Yahtzee.
Simplifications:  only allow discard and roll, only score against upper level
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    if len(hand) > 0:
        return max([val * hand.count(val) for val in hand])
    else:
        return 0


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    values = []
    possible_vals = [num for num in range(1,num_die_sides + 1)]
    new_roll = gen_all_sequences(possible_vals, num_free_dice)
    for roll in new_roll:
        test = held_dice + roll
        values.append(score(test))
    return float(sum(values)/float(len(new_roll)))


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    full_set = set([()])
    for hold in range(1, len(hand) + 1):
        #creates a holding set
        answer_set = set([()])
    #    iterates through values up to a specified length
        for dummy_idx in range(hold):
    #        creates a temporary set to hold current values
            temp_set = set()
            #grabs each individual tuple in the holding set
            for partial_sequence in answer_set:
    #            iterates through the possible outcomes
                temp_outcomes = list(hand)[:]
                for num in partial_sequence:
    #                print("num is", num)
                    temp_outcomes.remove(num) 
    #            print(temp_outcomes)
                for item in temp_outcomes:
                    new_sequence = list(partial_sequence)
                    new_sequence.append(item)
                    temp_set.add(tuple(new_sequence))
            answer_set = temp_set
    #        print(answer_set)
        full_set = answer_set | full_set
    return set(tuple(sorted(sequence)) for sequence in full_set)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_value = {}
    old_max = float(0)
    for hold in gen_all_holds(hand):
        num_free_dice = len(hand) - len(hold)
        new_max = float(expected_value(hold, num_die_sides, num_free_dice))
        if new_max > old_max:
            max_value[new_max] = [hold]
            old_max = new_max
        elif new_max == old_max:
            max_value[new_max].append(hold)
    answer = tuple()
    for val in max_value.get(old_max):
        answer = answer + val
    return tuple([old_max, answer])

def run_yahtzee_test(num_die_sides,hand):
   """
   Compute the dice to hold and expected score for the given hand
   and number of dice sides.
   """
   hand_score, hold = strategy(hand, num_die_sides)
   print ("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)
      
run_yahtzee_test(6,(1, 1, 1, 5, 6))
