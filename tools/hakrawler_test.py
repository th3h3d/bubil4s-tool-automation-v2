from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.hakrawler_test_crawling
def test_crawling():
    """should return result of 'echo https://42qwerty42.com | hakrawler'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "hakrawler-test_crawling.txt"
    try:
        # Design
        if config["DOMAIN_TEXT"].find("https://") == -1 and config["DOMAIN_TEXT"].find("http://") == -1:
            command = 'echo https://{} | {}'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        else:
            # no need http or https
            command = 'echo {} | {}'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("hakrawler-test_crawling -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.hakrawler_test_crawling_http
def test_crawling_http():
    """should return result of 'echo http://42qwerty42.com | hakrawler'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "hakrawler-test_crawling_http.txt"
    try:
        if config["DOMAIN_TEXT"].find("https://") == -1 and config["DOMAIN_TEXT"].find("http://") == -1:
            command = 'echo http://{} | {}'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        else:
            # no need http or https
            command = 'echo {} | {}'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("hakrawler-test_crawling_http -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.hakrawler_test_deep_crawling
def test_deep_crawling():
    """should return result of 'echo https://42qwerty42.com | hakrawler -d 5'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "hakrawler-test_deep_crawling.txt"
    try:
        if config["DOMAIN_TEXT"].find("https://") == -1 and config["DOMAIN_TEXT"].find("http://") == -1:
            command = 'echo https://{} | {} -d 5'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        else:
            # no need http or https
            command = 'echo {} | {} -d 5'.format(config["DOMAIN_TEXT"], config["HAKRAWLER_TOOL_PATH"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("hakrawler-test_deep_crawling -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.hakrawler_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "hakrawler-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["HAKRAWLER_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("hakrawler-test_do_custom -> {}".format(str(e)))
        assert False
