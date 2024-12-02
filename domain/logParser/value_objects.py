# stdlib
from typing import Union


class LogStats:

    def __init__(self, total: int, errors: int, success: int, success_mean_time: Union[int, float]) -> None:
        """

        :param total: Общее число задач
        :param errors: Число успешно выполненных задач
        :param success: Число незавершенных задач
        :param success_mean_time: Среднее время выполнения задачи на сервисе
        """
        self.total = total
        self.errors = errors
        self.success = success
        self.success_mean_time = success_mean_time

    def to_dict(self) -> dict:
        """

        :return: Словарь метрик
        """
        return {
            'total': self.total,
            'errors': self.errors,
            'success': self.success,
            'success_mean_time': self.success_mean_time
        }
