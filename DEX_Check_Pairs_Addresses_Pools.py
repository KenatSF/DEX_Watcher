import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

from web3 import Web3
import DEX_ETH as dex
import time

web3 = Web3(Web3.HTTPProvider(os.getenv("ETH_INFURA_HTTP")))

dex_name = 'sushiswap'
dex_factory = dex.dex_factory[dex_name]

columnas = list(dex.token_name_erc20.keys())
df = pd.DataFrame(columns=columnas)
myList = []


n = len(columnas)
for i in range(n):
    myList.append([])
    for j in range(n):
        if i == j:
            myList[i].append('0x0')
        else:
            nombre_par = columnas[j] + '/' + columnas[i]
            print(nombre_par)
            time.sleep(2)
            pair_address = dex.get_dex_pair_address(web3, dex_factory, dex.token_name_erc20[columnas[j]],
                                                     dex.token_name_erc20[columnas[i]])
            myList[i].append(pair_address)


for i in range(n):
    df[columnas[i]] = myList[i]

df.index = columnas
print(df)

os.chdir(os.getenv("DATA_PATH"))
file = dex_name + '_pair_addresses.csv'
df.to_csv(file)


print("--------------------------------------------------")
print("END")