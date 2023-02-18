#A secure password consists of at least eight characters that are a combination of letters, numbers, and symbols
#(@, #, $, %, etc.) if allowed. Passwords distinguish between uppercase and lowercase letters, so a secure
#password contains both uppercase and lowercase letters.

import pandas as pd

# read CSV 
df = pd.read_csv("ClientADIdentities.csv")


for index, row in df.iterrows():
    # Get the vakue of each password to compare
    word = row["Password"]

    # Check the length of the password in csv file
    if len(word) >= 8:
        usname=row["Name"]
        print(usname)
        
