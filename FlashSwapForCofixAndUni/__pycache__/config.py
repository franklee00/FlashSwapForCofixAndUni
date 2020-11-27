# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (default, Mar 10 2020, 15:43:33) 
# [Clang 11.0.0 (clang-1100.0.33.17)]
# Embedded file name: /Users/priest/Documents/GitHub/FlashSwapForCofixAndUni/FlashSwapForCofixAndUni/config.py
# Compiled at: 2020-11-10 01:06:26
# Size of source mod 2**32: 1200 bytes
from web3 import Web3
SETTING = {'ROPSTEN_URL':'https://ropsten.infura.io/v3/d7340332552745c199ea10f2597984c9', 
 'MAINNET_URL':'https://mainnet.infura.io/v3/d7340332552745c199ea10f2597984c9', 
 'CONTRACT_ADDRESS':'XXX', 
 'WALLET_PRIVATEKEY':'d7a972df4693952bc4eaaa38c2614c759c50f73394094238184f3f05a96d6448', 
 'WALLET_ADDRESS':'0x40e04b3Cb845e39b960174c31919A14dA09790Fa', 
 'ETH_SPAN':[
  1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900]}
w3 = Web3(Web3.HTTPProvider(SETTING['MAINNET_URL']))

def sendTransation(tx_dic):
    nonce = w3.eth.getTransactionCount(SETTING['WALLET_ADDRESS'])
    tx_dic['nonce'] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=(SETTING['WALLET_PRIVATEKEY']))
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


def sendTransationWithMoreGas(tx_dic, gwei):
    nonce = w3.eth.getTransactionCount(SETTING['WALLET_ADDRESS'])
    tx_dic['nonce'] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=(SETTING['WALLET_PRIVATEKEY']))
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)
# okay decompiling config.cpython-37.pyc
