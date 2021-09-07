from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.assetfinder_test_find_assets
def test_find_assets():
    """should return result of 'assetfinder --subs-only 42qwerty42.com'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "assetfinder-test_find_assets.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = '{} --subs-only {} -q'.format(config["ASSETFINDER_TOOL_PATH"], config["DOMAIN_TEXT"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("assetfinder-test_find_assets -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.assetfinder_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "assetfinder-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["ASSETFINDER_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("assetfinder-test_do_custom -> {}".format(str(e)))
        assert False
