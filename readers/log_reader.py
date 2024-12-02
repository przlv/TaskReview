# stdlib
import os

# project
from domain.logParser.entities import LogEntry


class FileLogReader:
    def __init__(self, log_dir: str) -> None:
        """

        :param log_dir: Директория хранения логов
        """
        self.log_dir = log_dir

    def get_log_files(self) -> list[str]:
        """
        Возвращает список файлов логов в директории.
        """
        return os.listdir(self.log_dir)

    def read_logs(self, file_name: str) -> list[LogEntry]:
        """
        Читает логи из файла
        """
        file_path = os.path.join(self.log_dir, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.readlines()

        results = []
        for line in data:
            msg, time = line.strip().split(" ")
            results.append(
                LogEntry(
                    msg=msg,
                    time=int(time)
                )
            )

        return results
