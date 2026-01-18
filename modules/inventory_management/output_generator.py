import os
import pandas as pd
from inventory_logic import inventory_and_discount_logic

FORECAST_PATH = r"data\outputs\sales_forecast.csv"
STOCK_PATH = r"data\raw\inventory\current_stock.csv"

INV_OUT = r"data\outputs\inventory_recommendations.csv"
DISC_OUT = r"data\outputs\discount_recommendations.csv"

def main():
    forecast = pd.read_csv(FORECAST_PATH)
    stock = pd.read_csv(STOCK_PATH)

    inv_df, disc_df = inventory_and_discount_logic(
        forecast_df=forecast[["date","product_id","predicted_sales"]],
        stock_df=stock
    )

    os.makedirs("data/outputs", exist_ok=True)
    inv_df.to_csv(INV_OUT, index=False)
    disc_df.to_csv(DISC_OUT, index=False)

    print("Saved inventory & discount recommendations")

if __name__ == "__main__":
    main()
