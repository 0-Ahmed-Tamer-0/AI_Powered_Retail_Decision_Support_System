import os
import pandas as pd

from forecast_model import (
    build_top_products,
    make_daily_product_sales,
    forecast_top_products,
)

DATA_PATH = r"data\raw\sales_forecasting\online_retail_II.csv"
OUT_PATH = r"data\outputs\sales_forecast.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    # Basic cleaning
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df = df[~df["Invoice"].astype(str).str.startswith("C")]
    df = df[df["Quantity"] > 0]
    df = df[df["Price"] > 0]

    df["Sales"] = df["Quantity"] * df["Price"]

    # Top-10 products
    top10 = build_top_products(df, top_n=10)

    # Daily sales per product
    df_top = df[df["StockCode"].astype(str).isin(top10)].copy()
    daily_prod = make_daily_product_sales(df_top)

    # Forecast top-10
    fc = forecast_top_products(daily_prod, top10, periods=30)
    if fc.empty:
        raise RuntimeError("No forecasts generated. Check data/history length.")

    # Merge actual and predicted on date/product
    fc["date"] = fc["ds"].dt.date
    fc = fc.drop(columns=["ds"])

    merged = pd.merge(
        daily_prod,
        fc,
        on=["date", "product_id"],
        how="left"
    )

    # Output schema
    out = pd.DataFrame({
        "date": merged["date"],
        "product_id": merged["product_id"],
        "actual_sales": merged["sales"],
        "predicted_sales": merged["yhat"]
    })

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    out.to_csv(OUT_PATH, index=False)

    print("Saved:", OUT_PATH)
    print("Products:", top10)
    print(out.head())

if __name__ == "__main__":
    main()
