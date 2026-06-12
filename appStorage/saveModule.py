from Bank import Bank,Account

dataFile = "appStorage/accounts.json"

def saveAccountData():
    data = {"accounts": []}

    for account in 