def find_change(coin_values,change,known_results=[0]*64):
    """Takes a list of coin values and desired change 
    returning the minimum number of coins necessary to
    achieve the change value.
    """
    minimum = change
    if change in coin_values:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:    
        for value in [c for c in coin_values if c <= change]:
            num_coins = 1 + find_change(coin_values, change - value, known_results)
            if num_coins < minimum:
                minimum = num_coins
                known_results[change] = minimum
    return minimum

