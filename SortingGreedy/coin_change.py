def coin_change(coins, amount):
    """
    Coin Change (Greedy Works When Canonical)
    ✅ Works for US/EU coins.
    ⚠️ Not always correct for arbitrary denominations (need DP there).
    """
    coins.sort(reverse=True)
    count = 0
    for c in coins:
        while amount >= c:
            amount -= c
            count += 1
    return count if amount == 0 else -1
