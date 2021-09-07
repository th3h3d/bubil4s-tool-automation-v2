from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.check
@pytest.mark.httpx_test_fast_probing
def test_fast_probing():
    """should return result of 'httpx -l subsdomains.txt --silent'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "httpx-test_fast_probing.txt"
    section_file_name = config["PROBED_DOMAIN_FILE"]
    try:
        # Design
        command = '{} -l {} --silent'.format(config["HTTPX_TOOL_PATH"], config["SUB_DOMAIN_FILE"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("httpx-test_fast_probing -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.httpx_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "httpx-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["HTTPX_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("httpx-test_do_custom -> {}".format(str(e)))
        assert False
