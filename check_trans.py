import logging
import aiohttp
import asyncio
import json
import re
import sys

logging.basicConfig(filename='bitcoin_transactions.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_URL = "https://blockchain.info/rawaddr/"
OUTPUT_FILE = "transaction_ids.txt"   # output file or you can change it as you desired
MAX_RETRIES = 3
DELAY_BETWEEN_REQUESTS = 1  # seconds

def is_valid_bitcoin_address(address):
    """Validate Bitcoin address format."""
    legacy_pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'
    bech32_pattern = r'^bc1[a-zA-HJ-NP-Z0-9]{39,59}$'
    return bool(re.match(legacy_pattern, address) or re.match(bech32_pattern, address))

async def get_transaction_ids(session, address, offset=0):
    """Fetches transaction IDs for a given Bitcoin address."""
    url = f"{API_URL}{address}?offset={offset}"
    for attempt in range(MAX_RETRIES):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                return [tx['hash'] for tx in data.get('txs', [])], data.get('n_tx', 0)
        except aiohttp.ClientError as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(DELAY_BETWEEN_REQUESTS * (attempt + 1))
    logging.error(f"Failed to fetch transaction IDs for {address} after {MAX_RETRIES} attempts")
    return None, 0

async def write_transactions_to_file(address):
    """Fetches and writes transaction IDs to a file."""
    if not is_valid_bitcoin_address(address):
        logging.error(f"Invalid Bitcoin address: {address}")
        return

    async with aiohttp.ClientSession() as session:
        offset = 0
        all_tx_ids = []
        while True:
            tx_ids, n_tx = await get_transaction_ids(session, address, offset)
            if tx_ids is None:
                break
            all_tx_ids.extend(tx_ids)
            if len(all_tx_ids) >= n_tx:
                break
            offset += len(tx_ids)
            await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

        if all_tx_ids:
            with open(OUTPUT_FILE, 'w') as f:
                for tx_id in all_tx_ids:
                    f.write(f"{tx_id}\n")
            logging.info(f"Transaction IDs for {address} written to {OUTPUT_FILE}")
            print(f"Transaction IDs for {address} written to {OUTPUT_FILE}")
        else:
            logging.warning(f"No transaction IDs retrieved for {address}")
            print(f"No transaction IDs retrieved for {address}")

async def main():
    """Prompts user for a Bitcoin address and writes transaction IDs to a file."""
    address = input("Enter a Bitcoin address: ")
    await write_transactions_to_file(address)

if __name__ == "__main__":
    if sys.platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
