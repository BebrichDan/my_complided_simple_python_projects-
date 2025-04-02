import os
from random import randint
import logging

import requests 

from config import TELEGRAM_BOT_TOKEN, ID_MY_TELEGRAM_CHANEL

def logger(func):
    def wrapper(*args, **kwargs):
        """Декоратор логирования."""
        try:
            result = func(*args, **kwargs)
            logging.info(f"Function {func.__name__} completed correctly")
            return result
        except Exception as error:
            logging.error(f"In {func.__name__} error: {error}")
            error_occurred = True
            Research.send_report_status(token=TELEGRAM_BOT_TOKEN, 
                                        chat_id=ID_MY_TELEGRAM_CHANEL, 
                                        error=error_occurred)
            raise
    return wrapper


class Research:
    @logger
    def __init__(self, file_path):
        if not file_path:
            raise ValueError("Error: File path is not specified.")
        if not os.path.exists(file_path):
            raise ValueError(f"Error: File '{file_path}' not found or does not exist.")
        self.file_path = file_path

    @logger
    def file_reader(self, has_header=True):
        """Функция проверки коректности содержимого, 
        если дынне коректны, возвращает набор значений."""
        try:
            with open(self.file_path, "r") as file:
                lines = file.readlines()
                if len(lines) < 2:
                    raise ValueError("Error: The file is too short.")
                if has_header:
                    header = lines[0].strip().split(",")
                    if len(header) != 2 or not all(part.isalpha() for part in header):
                        raise ValueError("Error: Invalid header format.")
                    data_lines = lines[1:]
                else:
                    data_lines = lines
                data = []
                for _, line in enumerate(data_lines, start=1):
                    values = line.strip().split(",")
                    if len(values) != 2:
                        raise ValueError("Error: Incorrect data format.")
                    if not all(v in {"0", "1"} for v in values):
                        raise ValueError("Error: Value in line is not correct.")
                    data.append([int(val) for val in values])
                return data
        except:
            raise

    class Calculations:
        @staticmethod
        @logger
        def counts(data_list):
            """Подсчёт количества орлов и решек."""
            heads, tails = 0, 0
            for row in data_list:
                if row[0] == 1:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        @staticmethod
        @logger
        def fractions(heads, tails):
            """Соотношение в процетах количества орлов и решек."""
            total = heads + tails
            percent_heads = (heads / total) * 100 if total else 0
            percent_tails = (tails / total) * 100 if total else 0
            return percent_heads, percent_tails

        @staticmethod
        @logger
        def predict_last(data_list):
            """Возвращает последний элемент данных из file_reader()"""
            if not data_list:
                raise ValueError("Error: No data to predict.")
            return data_list[-1]
    
    @staticmethod
    def send_report_status(token, chat_id, error: bool) -> bool:
        """Отправка в телеграм канал статуса формирования отчета."""
        if error:
            message = "The report hasn been created due to an error"
        else:
            message = "The report has been successfully created"

        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message}

        try:
            response = requests.post(url, data=payload)
            response.raise_for_status()  # Если статус код не 200, исключение
            logging.info("Sending the report is completed: %s", message)
            return True
        except Exception as error:
            logging.error("Error when sending a message to the telegram channel: %s", error)
            return False


class Analytics(Research.Calculations):
    @staticmethod
    @logger
    def predict_random(n):
        """Генерация случайных предсказаний."""
        predictions = []
        for _ in range(n):
            if randint(0, 1) == 0:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        return predictions

    
    @staticmethod
    @logger
    def save_file(data, file_name, extension):
        """Cохраняет любой заданный результат в файл с заданным расширением."""
        full_name = f"{file_name}.{extension}"
        with open(full_name, "w") as f:
            f.write(data)


