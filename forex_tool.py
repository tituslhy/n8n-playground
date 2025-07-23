import httpx
from fastmcp import FastMCP

mcp = FastMCP(name="Exchange rate tool", port=3000)

@mcp.tool()
async def get_exchange_rate(
    currency_from: str = "USD",
    currency_to: str = "EUR",
):
    """Use this to get current exchange rate.

    Args:
        currency_from: The currency to convert from (e.g., "USD").
        currency_to: The currency to convert to (e.g., "EUR").

    Returns:
        A dictionary containing the exchange rate data, or an error message if the request fails.
    """    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.frankfurter.app/latest",
                params={"from": currency_from, "to": currency_to},
            )
            response.raise_for_status()

            data = response.json()
            if "rates" not in data:
                return {"error": "Invalid API response format."}
            return data
    except httpx.HTTPError as e:
        return {"error": f"API request failed: {e}"}
    except ValueError:
        return {"error": "Invalid JSON response from API."}

if __name__ == "__main__":
    print("🚀Starting server... ")
    mcp.run(transport="sse")