import csv
import json
import logging
from pathlib import Path

# ---------- Logging ----------


def setup_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


# ---------- CSV Reading ----------


def read_sales_csv(path: Path) -> list[dict]:
    """Read sales data from CSV."""
    sales = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for sale in reader:
            sale["price"] = float(sale["price"])
            sales.append(sale)
    return sales


# ---------- Metrics ----------


def calculate_metrics(sales: list[dict]) -> dict:
    """Calculate total sales and average price."""
    total = 0
    count = 0

    for sale in sales:
        total += sale["price"]
        count += 1
    average = total / count if count > 0 else 0

    return {
        "total_sales": total,
        "average_price": average,
        "items_sold": count,
    }


# ---------- JSON Writing ----------


def save_metrics(path: Path, data: dict) -> None:
    """Save metrics to JSON file."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ---------- Main Process ----------

if __name__ == "__main__":
    setup_logger()

    base = Path("test_data")
    base.mkdir(exist_ok=True)

    csv_file = base / "sales.csv"
    json_file = base / "metrics.json"

    if not csv_file.exists():
        with csv_file.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["product", "price"])
            writer.writerow(["Laptop", 1600])
            writer.writerow(["Mouse", 250])
            writer.writerow(["Keyboard", 650])

        logging.info("Sample CSV file created.")

    logging.info("Reading sales data")
    sales = read_sales_csv(csv_file)

    logging.info("Calculating metrics")
    metrics = calculate_metrics(sales)

    logging.info("Saving metrics to JSON")
    save_metrics(json_file, metrics)

    logging.info("Process completed.")
