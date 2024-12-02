class LogEntry:
    def __init__(self, msg: str, time: int) -> None:
        """
        :param msg: Сообщение в логах СТАРТ\СТОП
        :param time: Время
        """
        self.msg = msg
        self.time = time
