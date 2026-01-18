import pandas as pd

def inventory_and_discount_logic(
    forecast_df: pd.DataFrame,
    stock_df: pd.DataFrame,
    horizon_days: int = 7
):
    forecast_df["date"] = pd.to_datetime(forecast_df["date"])

    inventory_rows = []
    discount_rows = []

    for _, row in stock_df.iterrows():
        pid = row["product_id"]
        current_stock = row["current_stock"]

        future = (
            forecast_df[forecast_df["product_id"] == pid]
            .sort_values("date")
            .head(horizon_days)
        )

        predicted_demand = future["predicted_sales"].sum()

        # ---------- Inventory decision ----------
        safety_stock = predicted_demand * 0.2
        required = predicted_demand + safety_stock

        if required > current_stock:
            decision = "REORDER"
            reorder_qty = int(required - current_stock)
            reason = "Predicted demand exceeds stock"
        else:
            decision = "OK"
            reorder_qty = 0
            reason = "Stock sufficient"

        inventory_rows.append({
            "product_id": pid,
            "decision": decision,
            "recommended_order": reorder_qty,
            "reason": reason
        })

        # ---------- Discount decision ----------
        if current_stock > predicted_demand * 1.5:
            discount_rows.append({
                "product_id": pid,
                "discount_action": "DISCOUNT",
                "discount_rate": 20,
                "reason": "High stock and low demand"
            })
        else:
            discount_rows.append({
                "product_id": pid,
                "discount_action": "NONE",
                "discount_rate": 0,
                "reason": "Stock level normal"
            })

    return (
        pd.DataFrame(inventory_rows),
        pd.DataFrame(discount_rows)
    )
