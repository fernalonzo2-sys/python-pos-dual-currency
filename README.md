# CLI Point of Sale (POS) - Dual Currency System

A command-line Point of Sale terminal built in Python. This system is designed for environments that handle multiple currencies simultaneously, automatically fetching and caching the official daily exchange rate to calculate totals dynamically.

## Features
- **Third-Party API Integration:** Fetches the real-time official exchange rate (BCV) using `ve.dolarapi.com`.
- **Smart Local Caching:** Implements a JSON-based caching system (`tasa_dolar.json`) that saves the daily rate. This minimizes external API requests and speeds up the program's execution.
- **Dual-Currency Cart Logic:** Allows users to add products to a cart in USD, while automatically calculating and formatting the final receipt in both USD and local currency (Bs).
- **Interactive CLI:** A user-friendly console loop that handles input validation, item quantities, and generates a formatted text-based invoice.
- **Transaction Logging:** Integrates with a custom `facturas` module to register and store completed sales.

## Tech Stack
- **Language:** Python 3.x
- **Standard Libraries:** `json` (Caching), `datetime` (Temporal validation)
- **External Libraries:** `requests` (HTTP API consumption)

## Project Structure
- `main.py`: The entry point containing the core logic and CLI loop.
- `facturas.py`: Module responsible for logging and storing the completed transactions.
- `tasa_dolar.json`: Auto-generated cache file for the daily exchange rate.

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)