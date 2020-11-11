from gcp_cloud_logger import __version__, CloudLogger


def test_version():
    assert __version__ == "0.1.0"


def test_logger_info():
    credential_path = ""

    logger = CloudLogger(
        name="test_cloud_logger",
        credential_path=credential_path,
    )

    logger.info("test info log")
