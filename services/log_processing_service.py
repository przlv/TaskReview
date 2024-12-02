# project
from domain.logParser.root import LogParser
from readers.log_reader import FileLogReader
from writers.log_writer import FileLogWriter


class LogProcessingService:

    def __init__(self, log_reader: FileLogReader, log_writer: FileLogWriter, start_msg: str, end_msg: str) -> None:
        """

        :param log_reader: Ридер логов
        :param log_writer: Запись логов
        :param start_msg: Сообщение о начале работы сервиса
        :param end_msg: Сообщение о конце работы сервиса
        """
        self.log_reader = log_reader
        self.log_writer = log_writer
        self.log_parser = LogParser(start_msg, end_msg)

    def processing(self) -> None:
        """
        Обработка логов
        :return: None
        """
        log_files = self.log_reader.get_log_files()
        for file_name in log_files:
            logs = self.log_reader.read_logs(file_name)
            stats = self.log_parser.calculate_metrics(logs)
            self.log_writer.save_json(file_name, stats)
