NUM_OF_PREDICTIONS = 3

REPORT_TEMPLATE = (
    "Report\n\n"
    "We have made {total_observations} observations from tossing a coin: {tails_observations} of them were tails and {heads_observations} of them were heads. "
    "The probabilities are {percent_tails:.2f}% and {percent_heads:.2f}%, respectively. "
    "Our forecast is that in the next {num_predictions} observations we will have: {forecast_tails} tail(s) and {forecast_heads} head(s)."
)

REPORT_FILENAME = "report.txt"

