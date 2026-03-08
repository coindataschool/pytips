"""
Combine Dictionaries
    ref: https://peps.python.org/pep-0448/
"""

majors = {
    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "WETH": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "WSOL": "So11111111111111111111111111111111111111112",
}
alts = {
    "WHYPE": "0x5555555555555555555555555555555555555555",
    "ZRO": "0x6985884C4392D348587B19cb9eAAf157F13271cd",
    "UNI": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",
    "AAVE": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9",
}

# method 1
majors | alts

# method 2
{**majors, **alts}
# what if there are duplicated keys?
more_alts = {
    "FARTCOIN": "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump",
    "WHYPE": "fake fake fake address",
    "UNI": "fake addy",
    "PUMP": "pumpCmXqMfrsAkQ5r49WcJnRayYRqmXz6ae8H7H9Dfn",
}
# the values from the 2nd dictionary get used
{**alts, **more_alts}
{**more_alts, **alts}

# method 3
# Use .update() to change dictionaries in place.
# Any existing keys will have their old values updated by the new ones.
more_alts.update(alts)
more_alts
