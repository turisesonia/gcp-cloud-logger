__version__ = "0.1.0"

import json
from google.cloud import logging as cloud_logging


class CloudLogger(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, **kwargs):

        credential_path = kwargs.get("credential_path")

        if not credential_path:
            __client = cloud_logging.Client.from_service_account_json(credential_path)
        else:
            __client = {}

        __handler = __client.get_default_handler()

        self.__logger = __client.logger(kwargs.get("name", "google_cloud_logger"))

    def info(self, content):
        self.log_text(content, severity="INFO")

    def warn(self, content):
        self.log_text(content, severity="WARNING")

    def error(self, content):
        self.log_text(content, severity="ERROR")

    def critical(self, content):
        self.log_text(content, severity="CRITICAL")

    def log_text(self, content, **kwargs):
        if type(content) in (dict, list):
            content = json.dumps(content)

        self.__logger.log_text(content, severity=kwargs.get("severity", "INFO"))


cloud_logger = CloudLogger()