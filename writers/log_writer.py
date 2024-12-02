# stdlib
import os
import json

# project
from domain.logParser.value_objects import LogStats

class FileLogWriter:
    def __init__(self, save_dir: str) -> None:
        """

        :param save_dir: Директория для хранения метрик по логам
        """
        self.save_dir = save_dir

    def save_json(self, file_name: str, stats: LogStats) -> None:
        """

        :param file_name: имя файла логов
        :param stats: метрики логов
        """
        save_path = os.path.join(self.save_dir, f"{file_name[:-4]}-results.json")
        with open(save_path, 'w', encoding='utf-8') as file:
            json.dump(stats.to_dict(), file)
        print(f"INFO: Результаты логов сохранены | {file_name}")
