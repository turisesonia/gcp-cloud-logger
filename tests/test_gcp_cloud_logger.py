from gcp_cloud_logger import cloud_logger


def test_logger_info():
    credential_path = "service_account.json"
    cloud_logger.setup(name="test_cloud_logger", credential_path=credential_path)
    cloud_logger.info("test info log")


def test_credential_json():
    credential_path = "service_account.json"
    credential_json = '{"type":"service_account","project_id":"","private_key_id":"","private_key":"","client_email":","client_id":"","auth_uri":"","token_uri":"","auth_provider_x509_cert_url":"","client_x509_cert_url":""}'

    cloud_logger.setup(
        name="test_cloud_logger",
        credential_path=credential_path,
        credential_json=credential_json,
    )

    cloud_logger.info("test info log")