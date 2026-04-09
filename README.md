# Real-Time Data Processing Pipeline

## Overview
This project simulates a real-time telemetry data processing pipeline using Python. It generates device telemetry data, cleans and validates incoming records, computes monitoring metrics, and exports processed outputs for downstream analysis.

The project also includes a Lambda-style handler to simulate serverless processing workflows commonly used in cloud environments.

## Key Features
- Simulates real-time telemetry data streams
- Cleans and validates structured data records
- Computes summary metrics (CPU, memory, temperature)
- Exports processed outputs to JSON
- Includes Lambda-style processing entry point

## Technologies Used
- Python
- Pandas
- AWS Lambda-style architecture
- JSON-based structured data

## Project Structure
real-time-data-processing-pipeline/
├── data_simulator.py  
├── data_processor.py  
├── lambda_handler.py  
├── requirements.txt  
├── sample_data/  
└── output/

## How to Run

Install dependencies:

pip install -r requirements.txt

Generate sample data:

python data_simulator.py

Run processing pipeline:

python data_processor.py

## Why I Built This
I built this project to strengthen my backend engineering and data pipeline skills by simulating a production-style telemetry workflow. This reflects experience with structured data handling, debugging, and serverless-style processing.
