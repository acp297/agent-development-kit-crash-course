import yfinance as yf


def get_current_price(ticker_symbol: str) -> float:
    """
    Fetches the current (latest close) price for the given stock ticker.

    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'WMT').

    Returns:
        float: The latest price.
    """
    stock = yf.Ticker(ticker_symbol)
    # Get today's historical data
    hist = stock.history(period="1d")
    if not hist.empty:
        # Use closing price as current
        return hist['Close'].iloc[-1]
    else:
        raise ValueError(f"No data found for ticker '{ticker_symbol}'")

if __name__ == "__main__":
    ticker = "WMT"
    try:
        price = get_current_price(ticker)
        print(f"Current price of {ticker}: ${price:.2f}")
    except Exception as e:
        print(f"Error fetching price: {e}")