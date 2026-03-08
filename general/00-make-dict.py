"""
Dictionary Creation
"""

# create a dictionary with defaultdict in the collections module
from collections import defaultdict

coins = [
    "majors - BTC",
    "majors - ETH",
    "majors - SOL",
    "alts - HYPE",
    "alts - ZRO",
    "alts - AAVE",
]

by_cointype = defaultdict(list)
for coin in coins:
    cointype, ticker = coin.split(" - ")
    by_cointype[cointype].append(ticker)
by_cointype


# create a dictionary with setdefault
by_coin_type = dict()
for coin in coins:
    cointype, ticker = coin.split(" - ")
    by_coin_type.setdefault(cointype, []).append(ticker)
by_coin_type


# create a dictionary from two sequences
seq1 = "WBTC", "WETH", "WSOL", "WHYPE"
seq2 = [
    "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "So11111111111111111111111111111111111111112",
    "0x5555555555555555555555555555555555555555",
]
dict(zip(seq1, seq2))


# create dictionaries with **kwargs in a function
def mk_dict(**x):
    return x


mk_dict(
    WBTC="0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    WETH="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    WSOL="So11111111111111111111111111111111111111112",
    WHYPE="0x5555555555555555555555555555555555555555",
)
