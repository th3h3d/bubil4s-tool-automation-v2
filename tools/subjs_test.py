from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.check
@pytest.mark.subjs_test_fetch_js_file
def test_fetch_js_file():
    """should return result of 'subjs -i urls.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subjs-test_fetch_js_file.txt"
    section_file_name = config["JS_URLS_FILE"]
    try:
        # Design
        command = '{} -i {}'.format(config["SUBJS_TOOL_PATH"], config["URLS_FILE"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subjs-test_fetch_js_file -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.subjs_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subjs-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["SUBJS_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subjs-test_do_custom -> {}".format(str(e)))
        assert False
