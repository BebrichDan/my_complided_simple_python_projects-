import os
from analytics import Research, Analytics
from config import NUM_OF_PREDICTIONS, REPORT_TEMPLATE, REPORT_FILENAME

if __name__ == '__main__':
    args = os.sys.argv
    if len(args) < 2:
        print("Error: Please provide the data file path as an argument.")
        os._exit(1)

    file_path = args[1]
    research = Research(file_path)
    data = research.file_reader(has_header=True)

    heads, tails = Analytics.counts(data)
    total_observations = len(data)
    percent_heads, percent_tails = Analytics.fractions(heads, tails)

    forecast = Analytics.predict_random(NUM_OF_PREDICTIONS)
    forecast_heads, forecast_tails = Analytics.counts(forecast)

    report = REPORT_TEMPLATE.format(
        total_observations=total_observations,
        tails_observations=tails,
        heads_observations=heads,
        percent_tails=percent_tails,
        percent_heads=percent_heads,
        num_predictions=NUM_OF_PREDICTIONS,
        forecast_tails=forecast_tails,
        forecast_heads=forecast_heads
    )

    name_part, ext_part = REPORT_FILENAME.split(".")
    Analytics.save_file(report, name_part, ext_part)

    print(report)
