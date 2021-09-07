from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.check
@pytest.mark.subjack_test_subtakeover_list
def test_subtakeover_list():
    """should return result of 'subjack -w subdomains.txt -timeout 30 -ssl'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subjack-test_subtakeover_list.txt"
    try:
        # Design
        command = '{} -w {} -timeout 30 -ssl'.format(config["SUBJACK_TOOL_PATH"], config["SUB_DOMAIN_FILE"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging

        assert True
    except Exception as e:
        config["LOGGER"].error("subjack-test_subtakeover_list -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.subjack_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subjack-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["SUBJACK_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subjack-test_do_custom -> {}".format(str(e)))
        assert False
