from fastapi import APIRouter, HTTPException, Query
from src.services.alphavantage_service import alpha_service

router = APIRouter(prefix="/api")


@router.get("/company-overview")
async def company_overview(symbol: str = Query(..., description="Stock ticker")):
    """
    Returns the company overview for a given stock symbol.
    """
    try:
        data = await alpha_service.get_company_overview(symbol)
        return data
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except RuntimeError as re:
        raise HTTPException(status_code=429, detail=str(re))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@router.get("/time-series-daily")
async def time_series_daily(
    symbol: str = Query(..., description="Stock ticker"),
    output_size: str = Query("compact", description="full or compact"),
):
    """
    Returns the daily time series for a given stock symbol.
    """
    try:
        response = await alpha_service.get_time_series_daily(symbol, output_size)
        return response
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
