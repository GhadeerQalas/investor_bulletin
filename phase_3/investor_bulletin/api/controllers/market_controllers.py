from fastapi import APIRouter, Query, HTTPException
from resources.market.market_service import MarketService
from typing import List
from enum import Enum
from resources.market.market_schema import MarketData

router = APIRouter()

class SymbolsEnums(Enum):
    AAPL = "AAPL"
    MSFT = "MSFT"
    GOOG = "GOOG"
    AMZN = "AMZN"
    META = "META"


@router.get("/market-prices", response_model=List[MarketData])
def get_market_data_route(symbols: list[SymbolsEnums] = Query(None, description="List of symbols to fetch market data for")):
    # In case no symbols are provided, return a 400 Bad Request
    if symbols is None or len(symbols) == 0:
        raise HTTPException(status_code=400, detail="No symbols provided")
    symbol_values = [symbol.value for symbol in symbols]

    return MarketService().get_market_data(symbol_values)
