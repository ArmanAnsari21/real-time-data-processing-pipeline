# real-time-data-processing-pipeline

Python-based real-time telemetry pipeline that simulates data ingestion, cleaning, transformation, and Lambda-style processing.

# Real-Time Data Processing Pipeline

## Overview
This project simulates a real-time telemetry processing pipeline using Python. It generates sample device telemetry data, cleans and validates incoming records, computes summary metrics, and writes processed output to a JSON file. The project also includes an AWS Lambda-style handler to reflect serverless deployment workflows.

## Features
- Simulates real-time telemetry data from multiple devices
- Cleans and validates structured records
- Computes summary metrics for system monitoring
- Exports processed data to JSON
- Includes a Lambda-style entry point for serverless workflows

## Technologies Used
- Python
- Pandas
- AWS Lambda-style handler
- JSON

## Project Structure
```text
real-time-data-processing-pipeline/
├── README.md
├── requirements.txt
├── data_simulator.py
├── data_processor.py
├── lambda_handler.py
├── sample_data/
│   └── telemetry_sample.json
└── output/
    └── processed_data.json
