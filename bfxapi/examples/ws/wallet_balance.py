import os
import sys
sys.path.append('../../../')
from bfxapi import Client
from bfxapi.constants import WS_HOST, REST_HOST

API_KEY=os.getenv("BFX_KEY")
API_SECRET=os.getenv("BFX_SECRET")

# Checking wallet balances requires private hosts
bfx = Client(
  API_KEY=API_KEY,
  API_SECRET=API_SECRET,
  logLevel='INFO',
  ws_host=WS_HOST,
  rest_host=REST_HOST
)

@bfx.ws.on('wallet_snapshot')
def log_snapshot(wallets):
  for wallet in wallets:
    print (wallet)
  
  # or bfx.ws.wallets.get_wallets()

@bfx.ws.on('wallet_update')
def log_update(wallet):
  print ("Balance updates: {}".format(wallet))

@bfx.ws.on('error')
def log_error(msg):
  print ("Error: {}".format(msg))

bfx.ws.run()
