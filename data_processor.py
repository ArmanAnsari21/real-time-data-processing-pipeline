import json
import os
from typing import Any

import pandas as pd


INPUT_FILE = "sample_data/telemetry_sample.json"
OUTPUT_FILE = "output/processed_data.json"


def load_data(filename: str) -> pd.DataFrame:
    with open(filename, "r", encoding="utf-8") as file:
        records = json.load(file)
    return pd.DataFrame(records)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["device_id", "timestamp", "temperature", "cpu_usage", "memory_usage", "status"])

    df = df[
        (df["temperature"].between(0, 150)) &
        (df["cpu_usage"].between(0, 100)) &
        (df["memory_usage"].between(0, 100))
    ]

    return df


def compute_metrics(df: pd.DataFrame) -> dict[str, Any]:
    return {
        "record_count": int(len(df)),
        "average_temperature": round(df["temperature"].mean(), 2),
        "average_cpu_usage": round(df["cpu_usage"].mean(), 2),
        "average_memory_usage": round(df["memory_usage"].mean(), 2),
        "critical_count": int((df["status"] == "critical").sum()),
        "warning_count": int((df["status"] == "warning").sum()),
        "devices_seen": sorted(df["device_id"].unique().tolist()),
    }


def build_output(df: pd.DataFrame, metrics: dict[str, Any]) -> dict[str, Any]:
    processed_records = df.to_dict(orient="records")

    for record in processed_records:
        if hasattr(record["timestamp"], "isoformat"):
            record["timestamp"] = record["timestamp"].isoformat()

    return {
        "metrics": metrics,
        "processed_records": processed_records,
    }


def save_output(payload: dict[str, Any], filename: str) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def run_pipeline(input_file: str = INPUT_FILE, output_file: str = OUTPUT_FILE) -> dict[str, Any]:
    df = load_data(input_file)
    cleaned_df = clean_data(df)
    metrics = compute_metrics(cleaned_df)
    output = build_output(cleaned_df, metrics)
    save_output(output, output_file)
    return output


if __name__ == "__main__":
    result = run_pipeline()
    print("Pipeline completed successfully.")
    print(json.dumps(result["metrics"], indent=2))
