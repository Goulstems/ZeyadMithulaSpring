from Bank import Bank,Account
import json
from json import JSONDecodeError

dataFile = "appStorage/accounts.json"

# for account in Bank.storage:
#     

def saveAccountData():
    data = {"accounts": []}
    # data = "Hello, world!"

    for account in Bank.storage:                #ITERATE appData
        data["accounts"].append({                   #build the data structure to save
            "name": account.name,
            "balance": str(account.balance),
            "accountID": account.accountID
        })
    
    #send the data !! // push it to the `dataFile`! 
    fileWriter = open(dataFile,"w");
    fileWriter.write(json.dumps(data));
    fileWriter.close();

def loadAccountData():
    fileReader = open(dataFile, "r")
    try:
        storedData = json.load(fileReader)
        fileReader.close()
        for AccountDict in storedData["accounts"]:
            Account(AccountDict["name"],AccountDict["balance"],AccountDict["accountID"])
    except (JSONDecodeError):
        Bank.storage.clear()