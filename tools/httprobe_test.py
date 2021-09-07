from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest
import os


@pytest.mark.check
@pytest.mark.httprobe_test_get_live_sites
def test_get_live_sites():
    """should return result of 'cat ./projects/<project name>/file_io/subdomains.txt | httprobe'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "httprobe-test_get_live_sites.txt"
    try:
        # Design
        input_full_path = os.path.join(config["INPUT_OUTPUT_PATH"], config["SUB_DOMAIN_FILE_PATH"])
        command = 'cat {} | {}'.format(input_full_path, config["DOMAIN_TEXT"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("httprobe-test_get_live_sites -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.httprobe_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "httprobe-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["HTTPROBE_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("httprobe-test_do_custom -> {}".format(str(e)))
        assert False
