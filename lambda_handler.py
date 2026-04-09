from data_processor import run_pipeline


def lambda_handler(event, context):
    result = run_pipeline()
    return {
        "statusCode": 200,
        "message": "Telemetry data processed successfully.",
        "metrics": result["metrics"],
    }
