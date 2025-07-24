# fetch_etf_flows.py
import json
from datetime import datetime

# Примерные ETF-данные (можно заменить на API позже)
etf_data = {
    "BlackRock_ETHA": {
        "inflow_usd": 5300000000,
        "change_24h": 12500000
    },
    "Fidelity_FETH": {
        "inflow_usd": 1650000000,
        "change_24h": 4000000
    }
}

# Сохраняем в файл
with open("data/eth_etf_flows.json", "w") as f:
    json.dump({
        "timestamp": datetime.now().isoformat(),
        "data": etf_data
    }, f, indent=2)

print("ETF flows updated.")
