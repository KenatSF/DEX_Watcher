const { initializeProvider ,initializeSigner, getNameERC20, getTokensDecimals, getPairAddress, getTokenReserves} = require('./quick_utils');
const { dex } = require('./data/dexes');

require('dotenv').config();

const ethereum = process.env.ETH_INFURA_HTTP;
const polygon = process.env.POLYGON_INFURA;
const avalanche = process.env.AVALANCHE_QUICKNODE;
const private_key = process.env.PRIVATE_KEY;

const provider = initializeProvider(avalanche);
const signer = initializeSigner(private_key, provider);

const token_a = "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7";
const token_b = "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70";
const factory = dex.factories.avalanche.joe;

async function main() {
    const pairAddress = await getPairAddress(signer, factory, token_a, token_b);
    const reserves = await getTokenReserves(signer, pairAddress);
    console.log(reserves);
    
}

main();