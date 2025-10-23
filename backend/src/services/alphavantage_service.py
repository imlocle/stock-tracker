import httpx
from typing import Any, Dict, Optional
from src.config.settings import settings
from src.utils.dummy_data import (
    DUMMY_DATA,
    get_dummy_time_series_data,
)


class AlphaVantageService:
    """Handles all interactions with the Alpha Vantage API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.ALPHAVANTAGE_API_KEY
        self.base_url = settings.ALPHAVANTAGE_URL

    async def _fetch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch data from Alpha Vantage, return empty dict on error."""
        async with httpx.AsyncClient(timeout=15) as client:
            try:
                response = await client.get(
                    self.base_url, params={**params, "apikey": self.api_key}
                )
                print(response.json())
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                print(f"HTTP error: {e.response.status_code} - {e.response.text}")
            except httpx.RequestError as e:
                print(f"Request error: {str(e)}")
            except Exception as e:
                print(f"Unknown fetch error: {str(e)}")
        return {}

    async def get_company_overview(self, symbol: str) -> Dict[str, Any]:
        """Fetch general company overview (name, sector, description, etc.)"""

        params = {"function": "OVERVIEW", "symbol": symbol}
        data = await self._fetch(params)

        if not data or "Symbol" not in data:
            data = DUMMY_DATA.get(symbol, {})
            if data["Symbol"] == symbol:
                return {
                    "data": data,
                    "message": "API rate limit reached. Using local data.",
                }

        return {"data": data, "message": None}

    async def get_time_series_daily(
        self, symbol: str, output_size: str = "compact"
    ) -> Dict[str, Any]:
        """Fetch daily time series data for a symbol (up to 100 data points)."""

        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "outputsize": output_size,
        }
        data = await self._fetch(params)

        if data.get("Information"):
            return {
                "data": get_dummy_time_series_data(),
                "message": "API rate limit reached. Using artifically created data.",
            }

        time_series = data.get("Time Series (Daily)", {})
        return {"data": time_series, "message": None}


alpha_service = AlphaVantageService()
