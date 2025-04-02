import logging

LOG_FILENAME = "analytics.log"
LOG_FORMAT = "%(asctime)s,%(msecs)03d %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = logging.INFO

logging.basicConfig(
    filename=LOG_FILENAME,
    level=LOG_LEVEL,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT
)

NUM_OF_PREDICTIONS = 3

REPORT_FILENAME = "report.txt"

REPORT_TEMPLATE = (
    "Report\n\n"
    "We have made {total_observations} observations from tossing a coin: {tails_observations} of them were tails and {heads_observations} of them were heads. "
    "The probabilities are {percent_tails:.2f}% and {percent_heads:.2f}%, respectively. "
    "Our forecast is that in the next {num_predictions} observations we will have: {forecast_tails} tail(s) and {forecast_heads} head(s)."
)

TELEGRAM_BOT_TOKEN = "7559128313:AAFO-pCKvcMyw2xS3O9kRx1bausSTfTqHeg"
ID_MY_TELEGRAM_CHANEL = "-1002320534209"

error_occurred = False