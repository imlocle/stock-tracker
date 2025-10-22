import httpx
from typing import Any, Dict, Optional
from src.config.settings import settings


class AlphaVantageService:
    """Handles all interactions with the Alpha Vantage API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.alphavantage_api_key
        self.base_url = settings.alphavantage_url

    async def _fetch(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Low-level helper to fetch data from Alpha Vantage."""
        try:
            async with httpx.AsyncClient(timeout=15) as client:
                response = await client.get(
                    self.base_url, params={**params, "apikey": self.api_key}
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(e)

    async def get_company_overview(self, symbol: str) -> Dict[str, Any]:
        """Fetch general company overview (name, sector, description, etc.)"""
        params = {"function": "OVERVIEW", "symbol": symbol}
        data = await self._fetch(params)

        if "Note" in data:
            raise RuntimeError(
                "API rate limit reached. Please wait a minute and retry."
            )
        if "Error Message" in data:
            raise ValueError(
                f"Invalid request for symbol '{symbol}': {data['Error Message']}"
            )
        if not data or "Symbol" not in data:
            raise ValueError(f"No company overview found for symbol '{symbol}'")

        return data

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
        if "Note" in data:
            return {
                "data": {},
                "message": "API rate limit reached. Please try again later.",
            }
        if "Information" in data:
            return {"data": {}, "message": data["Information"]}
        if "Error Message" in data:
            return {"data": {}, "message": data["Error Message"]}

        time_series = data.get("Time Series (Daily)", {})
        return {"data": time_series, "message": None}

    async def get_income_statement(self, symbol: str) -> Dict[str, Any]:
        """Fetch annual and quarterly income statements."""
        params = {"function": "INCOME_STATEMENT", "symbol": symbol}
        data = await self._fetch(params)
        if not data or "annualReports" not in data:
            raise ValueError(f"No income statement data found for symbol '{symbol}'")
        return data


alpha_service = AlphaVantageService()
