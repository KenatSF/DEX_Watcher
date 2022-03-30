import pandas as pd

from dotenv import load_dotenv
import os
load_dotenv()

from web3 import Web3
import DEX_ETH as dex
import CEX_Prices as cxp
import time

web3 = Web3(Web3.HTTPProvider(os.getenv("ETH_INFURA_HTTP")))

dex_name = 'sushiswap'

def assing_value(x):
    if 100 <= x and x < 1000:
        return 0.6
    elif 1000 <= x and x < 10000:
        return 0.7
    elif 10000 <= x and x < 100000:
        return 0.8
    elif 100000 <= x and x < 1000000:
        return 0.9
    elif 1000000 <= x:
        return 1
    else:
        return 0

os.chdir(os.getenv("DATA_PATH"))
file_0 = dex_name + '_pair_addresses.csv'
pair_df = pd.read_csv(file_0, index_col=0)

columnas = list(dex.token_name_erc20.keys())
df = pd.DataFrame(columns=columnas)
df_quantities = pd.DataFrame(columns=columnas)
myList = []
myQuantity = []

n = len(columnas)
for i in range(n):
    myList.append([])
    myQuantity.append([])
    for j in range(n):
        i_j = pair_df.iloc[i, j]

        print(columnas[i], columnas[j])
        if i_j == '0x0' or i_j == '0x0000000000000000000000000000000000000000':
            myList[i].append(0)
            myQuantity[i].append("0, 0")
        else:
            time.sleep(2)
            reserves = dex.get_token_reserves(web3, i_j)
            myQuantity[i].append(str(reserves[columnas[j]]) + ", " + str(reserves[columnas[i]]))

            current_price_i = cxp.get_current_price(columnas[i])
            current_price_j = cxp.get_current_price(columnas[j])

            if current_price_i == 0 and current_price_j == 0:
                myList[i].append(0)
            elif current_price_i != 0 and current_price_j == 0:
                price = reserves[columnas[i]] * current_price_i * 2
                myList[i].append(assing_value(price))
            elif current_price_i == 0 and current_price_j != 0:
                price = reserves[columnas[j]] * current_price_j * 2
                myList[i].append(assing_value(price))
            else:
                price_i = reserves[columnas[i]] * current_price_i
                price_j = reserves[columnas[j]] * current_price_j
                myList[i].append(assing_value(price_i + price_j))



for i in range(n):
    df[columnas[i]] = myList[i]
    df_quantities[columnas[i]] = myQuantity[i]

df.index = columnas
df_quantities.index = columnas



file_1 = dex_name + '_pair_pool_quantity_ones.csv'
file_2 = dex_name + '_pair_pool_quantities.csv'
df.to_csv(file_1)
df_quantities.to_csv(file_2)


print("--------------------------------------------------")
print("END")