import os
import pandas as pd
# RUN ONCE OR WHEN NEEDED
SALES_PATH = r"data\raw\sales_forecasting\online_retail_II.csv"
OUT_PATH = r"data\raw\inventory\current_stock.csv"

def main():
    df = pd.read_csv(SALES_PATH)

    # Basic cleaning (same as forecasting)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df = df[~df["Invoice"].astype(str).str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]
    df["Sales"] = df["Quantity"] * df["Price"]

    # Top-10 products
    top10 = (
        df.groupby("StockCode")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .index
        .astype(str)
        .tolist()
    )

    # Daily sales per product
    daily = (
        df[df["StockCode"].astype(str).isin(top10)]
        .groupby([df["InvoiceDate"].dt.date, "StockCode"])["Quantity"]
        .sum()
        .reset_index()
    )
    daily.columns = ["date", "product_id", "quantity"]

    # Average daily quantity → stock for 14 days
    stock = (
        daily.groupby("product_id")["quantity"]
        .mean()
        .round()
        .astype(int) * 14
    ).reset_index()

    stock.columns = ["product_id", "current_stock"]

    os.makedirs("data/raw/inventory", exist_ok=True)
    stock.to_csv(OUT_PATH, index=False)

    print("Generated stock:")
    print(stock)

if __name__ == "__main__":
    main()
