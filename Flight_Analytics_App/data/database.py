import duckdb as ddb


def route_query(
    ddb,
    parquet_path: str,
    source_airport: str,
    dest_airport: str,
    month: str,
):  # dataset is between Jan 2018 to June 2025
    # dataset location https://www.kaggle.com/datasets/saibeerao/us-domestic-passenger-flight-delays-bts-otp?select=combinedv2.parquet

    if month == 1:
        month = "BETWEEN '2025-06-01' AND '2025-06-30'"

    if month == 3:
        month = "BETWEEN '2025-04-01' AND '2025-06-30'"

    if month == 6:
        month = "BETWEEN '2025-01-01' AND '2025-06-30'"

    if month == 12:
        month = "BETWEEN '2024-06-30' AND '2025-06-30'"

    if month == 24:
        month = "BETWEEN '2023-06-30' AND '2025-06-30'"

    if month == 90:
        month = "BETWEEN '2018-01-01' AND '2025-06-30'"

    sql = """
    SELECT count(*) AS n
    FROM read_parquet(?)
    WHERE flight_date = ?
      AND ORIGIN = ?
      AND DEST = ?
      AND ARR_DELAY > ?
    """
    return ddb.execute(
        sql, [parquet_path, month, source_airport, dest_airport]
    ).fetchone()[0]
