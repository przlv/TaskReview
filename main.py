# project
from readers.log_reader import FileLogReader
from writers.log_writer import FileLogWriter
from services.log_processing_service import LogProcessingService
from common.const import (
    PATH_LOGS,
    PATH_RESULTS_LOGS_SAVE,
    START_MSG,
    END_MSG
)


def client():
    log_reader = FileLogReader(PATH_LOGS)
    log_writer = FileLogWriter(PATH_RESULTS_LOGS_SAVE)

    log_service = LogProcessingService(
        log_reader=log_reader,
        log_writer=log_writer,
        start_msg=START_MSG,
        end_msg=END_MSG,
    )

    log_service.processing()

    print("INFO: Обработка логов завершена.")


if __name__ == "__main__":
    client()
