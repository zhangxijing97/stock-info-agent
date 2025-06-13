import yfinance as yf
from google.adk.tools.tool_context import ToolContext

def get_stock_price(ticker: str, tool_context: ToolContext):
    stock = yf.Ticker(ticker)
    price = stock.info.get("currentPrice", "Price not available")

    if "recent_searches" not in tool_context.state:
        tool_context.state["recent_searches"] = []

    recent_searches = tool_context.state["recent_searches"]
    if ticker not in recent_searches:
        recent_searches.append(ticker)
        tool_context.state["recent_searches"] = recent_searches

    return {"price": price, "ticker": ticker}