import json
import random
import time
from datetime import datetime


DEVICES = ["sensor-A", "sensor-B", "sensor-C", "sensor-D"]
STATUSES = ["ok", "warning", "critical"]


def generate_telemetry_record() -> dict:
    return {
        "device_id": random.choice(DEVICES),
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(60.0, 100.0), 2),
        "cpu_usage": round(random.uniform(10.0, 95.0), 2),
        "memory_usage": round(random.uniform(20.0, 98.0), 2),
        "status": random.choices(
            STATUSES,
            weights=[0.75, 0.2, 0.05],
            k=1
        )[0],
    }


def generate_telemetry_batch(batch_size: int = 25) -> list[dict]:
    return [generate_telemetry_record() for _ in range(batch_size)]


def save_batch_to_file(records: list[dict], filename: str = "sample_data/telemetry_sample.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


if __name__ == "__main__":
    batch = generate_telemetry_batch()
    save_batch_to_file(batch)
    print(f"Generated {len(batch)} telemetry records and saved to sample_data/telemetry_sample.json")
