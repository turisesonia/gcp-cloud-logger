import ujson
from gcp_cloud_logger import cloud_logger

credential_path = "service_account.json"

credential_json = '{"type":"service_account","project_id":"","private_key_id":"","private_key":"","client_email":"","client_id":"","auth_uri":"","token_uri":"","auth_provider_x509_cert_url":"","client_x509_cert_url":""'


def test_setup_credential_path():
    cloud_logger.setup(name="test_cloud_logger", credential_path=credential_path)
    cloud_logger.info("test info log with file credential")


def test_setup_credential_json():
    cloud_logger.setup(
        name="test_cloud_logger",
        credential_json=credential_json,
    )

    cloud_logger.info("test info log with json credential")


def test_log_dict_content():
    cloud_logger.setup(
        name="test_cloud_logger",
        credential_json=credential_json,
    )

    cloud_logger.info({"type": "dict", "message": "test dict log"})


def test_log_list_content():
    cloud_logger.setup(
        name="test_cloud_logger",
        credential_json=credential_json,
    )

    cloud_logger.info(ujson.dumps([{"type": "list", "message": "test list log"}]))
