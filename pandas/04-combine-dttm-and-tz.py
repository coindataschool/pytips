"""Given two string columns in a dataframe, one contains datetime values and the
other time zone abbreviation. How to combine the two columns and create a new
column of datetime type?
"""

import pandas as pd

df = pd.DataFrame(
    {
        "datetime": [
            "2001-10-28 01:00",
            "2001-10-28 01:15",
            "2001-10-28 01:30",
            "2001-05-07 01:00",
            "2001-05-07 01:15",
            "2001-05-07 01:30",
        ],
        "tz": ["MST", "MST", "MST", "MDT", "MDT", "MDT"],
    }
)

# 1. replace time zone abbreviations with the corresponding numeric date offsets
tz_num_offsets = df["tz"].replace("MST", "-0700").replace("MDT", "-0600")

# 2. chain datetime and time zone numeric date offsets together
dttm_wtz_str = df["datetime"] + tz_num_offsets

# 3. convert to datetime type under UTC because of mixed timezones ('MST', 'MDT')
dttm_utc = pd.to_datetime(dttm_wtz_str, utc=True)
dttm_utc

# 4. convert to local timezone
dttm_local = dttm_utc.dt.tz_convert("America/Denver")
dttm_local

# Alternatively, localize with numeric offsets, and convert to local timezone
df["tz"] = df["tz"].replace("MDT", "MST7MDT")
df.groupby("tz")["datetime"].transform(
    lambda ser: (
        pd.to_datetime(ser)
        .dt.tz_localize(ser.name, ambiguous=True)  # same as step 2
        .dt.tz_convert("America/Denver")  # same as step 4
        # Note step 3 is skipped.
    )
)
