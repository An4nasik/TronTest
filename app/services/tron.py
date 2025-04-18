import httpx
from typing import Dict

TRON_API_URL = "https://api.shasta.trongrid.io"

async def get_tron_info(address: str) -> Dict[str, int]:
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    payload = {
        "address": address,
        "visible": True
    }

    async with httpx.AsyncClient() as client:
        # Получение информации об аккаунте
        account_response = await client.post(f"{TRON_API_URL}/wallet/getaccount", json=payload, headers=headers)
        account_data = account_response.json()
        balance = account_data.get("balance", 0)

        # Получение информации о ресурсах
        resource_response = await client.post(f"{TRON_API_URL}/wallet/getaccountresource", json=payload, headers=headers)
        resource_data = resource_response.json()
        bandwidth = resource_data.get("freeNetLimit", 0)
        energy = resource_data.get("EnergyLimit", 0)

    return {
        "address": address,
        "balance": balance,
        "bandwidth": bandwidth,
        "energy": energy
    }
