


module.exports = { 
    dex : {
        'routers': {    'eth': {    'uniswap': '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D',
                                    'sushiswap': '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F',
                                    'uniswapv3': '0xE592427A0AEce92De3Edee1F18E0157C05861564'}, 
                        'polygon': {    'quickswap': '0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff',
                                        'sushiswap': '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'},
                        'avalanche': {  'joe': '0x60aE616a2155Ee3d9A68541Ba4544862310933d4',
                                        'sushiswap': '0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506',
                                        'pangolin': '0xE54Ca86531e17Ef3616d22Ca28b0D458b6C89106'}
                    },
        'factories': {    'eth': {    'uniswap': '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f',
                                    'sushiswap': '0xC0AEe478e3658e2610c5F7A4A2E1777cE9e4f2Ac'},
                        'polygon': {    'quickswap': '0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32',
                                        'sushiswap': '0xc35DADB65012eC5796536bD9864eD8773aBc74C4'},
                        'avalanche': {  'joe': '0x9Ad6C38BE94206cA50bb0d90783181662f0Cfa10',
                                        'sushiswap': '0xc35DADB65012eC5796536bD9864eD8773aBc74C4',
                                        'pangolin': '0xefa94DE7a4656D787667C749f7E1223D71E9FD88'}
                    }
    }
};