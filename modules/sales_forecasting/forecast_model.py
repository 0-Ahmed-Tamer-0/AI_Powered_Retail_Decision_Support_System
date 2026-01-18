import pandas as pd
from prophet import Prophet

def build_top_products(df: pd.DataFrame, top_n: int = 10) -> list[str]:
    top = (
        df.groupby("StockCode")["Sales"]
          .sum()
          .sort_values(ascending=False)
          .head(top_n)
          .index
          .astype(str)
          .tolist()
    )
    return top

def make_daily_product_sales(df: pd.DataFrame) -> pd.DataFrame:
    daily = (
        df.groupby([df["InvoiceDate"].dt.date, "StockCode"])["Sales"]
          .sum()
          .reset_index()
    )
    daily.columns = ["date", "product_id", "sales"]
    daily["product_id"] = daily["product_id"].astype(str)
    return daily

def forecast_one_product(daily_prod: pd.DataFrame, product_id: str, periods: int = 30) -> pd.DataFrame:
    sub = daily_prod[daily_prod["product_id"] == product_id].copy()
    sub = sub.rename(columns={"date": "ds", "sales": "y"})
    sub["ds"] = pd.to_datetime(sub["ds"])

    # Simple safety: Prophet needs enough history
    if len(sub) < 14:
        return pd.DataFrame(columns=["ds", "yhat", "product_id"])

    m = Prophet()
    m.fit(sub)

    future = m.make_future_dataframe(periods=periods)
    fc = m.predict(future)[["ds", "yhat"]].copy()
    fc["product_id"] = product_id
    return fc

def forecast_top_products(daily_prod: pd.DataFrame, product_ids: list[str], periods: int = 30) -> pd.DataFrame:
    all_fc = []
    for pid in product_ids:
        fc = forecast_one_product(daily_prod, pid, periods=periods)
        if not fc.empty:
            all_fc.append(fc)

    if not all_fc:
        return pd.DataFrame(columns=["ds", "yhat", "product_id"])

    out = pd.concat(all_fc, ignore_index=True)
    return out
