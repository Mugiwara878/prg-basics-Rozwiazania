###
# Returns the minimum number of coins (1, 2, 5 PLN) needed to pay an amount
#
def min_coins(amount_to_pay):
    coins_5 = amount_to_pay // 5
    remainder = amount_to_pay % 5
    coins_2 = remainder // 2
    coins_1 = remainder % 2
    return coins_5 + coins_2 + coins_1