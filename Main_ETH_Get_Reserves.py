import time

start_time = time.time()
from web3 import Web3

import DEX_ETH as dex

from dotenv import load_dotenv
import os
load_dotenv()


#web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
web3 = Web3(Web3.HTTPProvider(os.getenv("ETH_INFURA_HTTP")))

token_a = 'WETH'
token_b = 'MATIC'

def reserves_filter(web3, dex_name, pair_address):
    if pair_address != '0x0000000000000000000000000000000000000000':
        reserves = dex.get_token_reserves(web3, pair_address)
        print("Reservas en {}:   {}".format(dex_name, reserves))
    else:
        print("No hay liquidez en {}".format(dex_name))

def reserves_filter_v3(web3, dex_name, pool_address, token_0, token_1):
    if pool_address != '0x0000000000000000000000000000000000000000':
        reserves = dex.get_token_reserves_v3(web3, pool_address, token_0, token_1)
        print("Reservas en {}:   {}".format(dex_name, reserves))
    else:
        print("No hay liquidez en {}".format(dex_name))



pair_address_1 = dex.get_dex_pair_address(web3, dex.dex_factory['uniswap'], dex.token_name_erc20[token_a], dex.token_name_erc20[token_b])
pair_address_2 = dex.get_dex_pair_address(web3, dex.dex_factory['sushiswap'], dex.token_name_erc20[token_a], dex.token_name_erc20[token_b])
#pair_address_v3 = dex.get_dex_pool_address(web3, ky.token_name_erc20[token_a], ky.token_name_erc20[token_b], 3000)
print("-------------------------------------------------------")
print("Pair address: ")
print(pair_address_1)
print(pair_address_2)
#print(pair_address_v3)
print("-------------------------------------------------------")
print("Reserves")
reserves_filter(web3, 'Uniswap', pair_address_1)
reserves_filter(web3, 'Sushiswap', pair_address_2)
#reserves_filter_v3(web3, 'Uniswap V3', pair_address_v3, ky.token_name_erc20[token_a], ky.token_name_erc20[token_b])

print("--- %s seconds ---" % (time.time() - start_time))
