# stdlib
from typing import List

# project
from .entities import LogEntry
from .value_objects import LogStats


class LogParser:

    def __init__(self, start_msg: str, end_msg: str) -> None:
        """
        :param start_msg: Обозначение старта работы сервиса
        :param end_msg: Обозначение конца работы сервиса
        """
        self.start_msg = start_msg
        self.end_msg = end_msg

    def calculate_metrics(self, log_entries: List[LogEntry]) -> LogStats:
        """
        Расчет ключевых метрик
        :param log_entries: Логи
        :return: Метрики логов
        """
        errors = 0
        success = 0
        success_time_sum = 0
        success_count = 0
        service_work = False
        start_time = None

        for entry in log_entries:
            if entry.msg == self.start_msg and not service_work:
                service_work = True
                start_time = entry.time
            elif entry.msg == self.end_msg and service_work:
                service_work = False
                success += 1
                success_time_sum += entry.time - start_time
                success_count += 1
            else:
                errors += 1

        total = success + errors
        mean_time = round(success_time_sum / success_count, 2)

        return LogStats(total, errors, success, mean_time)
