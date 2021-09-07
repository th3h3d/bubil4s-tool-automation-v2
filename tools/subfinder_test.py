from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.sub_passive
@pytest.mark.subfinder_test_fast_finder
def test_fast_finder():
    """should return result of 'subfinder -silent -d 42qwerty42.com -t 5'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subfinder-test_fast_finder.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = '{} -silent -d {} -t 5'.format(config["SUBFINDER_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_both(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subfinder-test_fast_finder -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.sub_active
@pytest.mark.subfinder_test_slow_finder
def test_slow_finder():
    """should return result of 'subfinder -silent -d 42qwerty42.com -t 5 -all'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subfinder-test_slow_finder.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = '{} -silent -d {} -t 5 -all'.format(config["SUBFINDER_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subfinder-test_slow_finder -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.subfinder_do_custom
def test_do_custom():
    """should return result of 'subfinder 42qwerty42'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subfinder-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["SUBFINDER_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subfinder-test_do_custom -> {}".format(str(e)))
        assert False

