# use get() when accessing a dictionary's values
ethereum_token_addr_lookup = {
    "WBTC": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599",
    "WETH": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
    "FXS": "0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0",
}
ethereum_token_addr_lookup["GMX"]  # throws KeyError
# get() doesn't throw KeyError when they key is not in the dict,
# instead, it returns the default argument supplied by user.
ethereum_token_addr_lookup.get("GMX", "GMX is NOT on Ethereum.")
