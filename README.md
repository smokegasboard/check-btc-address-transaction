# check btc address transaction


**Bitcoin Transaction Fetcher**

This Python script efficiently retrieves transaction IDs associated with a given Bitcoin address using the Blockchain.info API. It leverages asynchronous programming with `aiohttp` for faster processing.

**Features:**

* **Asynchronous I/O:** Enhances performance by handling multiple API requests concurrently.
* **Error Handling:** Implements retries and logging for robust error management.
* **Validation:** Ensures the provided Bitcoin address adheres to valid address formats.
* **Output:** Saves retrieved transaction IDs to a file (default: `transaction_ids.txt`).
* **Flexibility:** Adjustable parameters for retries and delay between requests.

**Requirements:**

* Python 3 (compatible with both Windows and Unix-based systems)
* `aiohttp` library (can be installed using `pip install aiohttp`)

**Installation:**

1. Clone or download this repository.
2. Install the required library: `pip install aiohttp`

**Usage:**

1. Open a terminal and navigate to the directory containing the script (`check_trans.py`).
2. Run the script:

   ```bash
   python check_trans.py
   ```

3. Enter a valid Bitcoin address when prompted.
4. The script will attempt to fetch transaction IDs and save them to `transaction_ids.txt`.

**Output:**

* If successful, the script logs and prints a message indicating transaction IDs are written to the output file.
* If no transaction IDs are found or an error occurs, the script logs and prints an appropriate message.

**Configuration (Optional):**

* `MAX_RETRIES`: Defines the maximum number of attempts to retrieve transaction IDs for an address (default: 3).
* `DELAY_BETWEEN_REQUESTS`: Sets the delay (in seconds) between API requests (default: 1). These values can be modified within the script itself.

**Contributing:**

* Feel free to report issues or suggest improvements by opening an issue on GitHub.
* We welcome pull requests for bug fixes, new features, or code enhancements.

**License:**

MIT License

**Additional Notes:**

* The script utilizes asynchronous programming for efficiency, but it might require minor adjustments for deployment in specific environments.
* Consider adding command-line arguments to allow users to specify the output file and other parameters directly.

**Example Usage:**

```bash
python bitcoin_transactions.py -o my_transactions.txt  # Output to a different file
```

Buy Me Coffee 3KFthrrU1xKsYrAVVWZ8iqqmqzg6RQwMXB
