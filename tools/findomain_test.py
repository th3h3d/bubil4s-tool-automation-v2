from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.sub_passive
@pytest.mark.findomain_test_fastest_subdomain_finding
def test_fastest_subdomain_finding():
    """should return result of 'findomain -t 42qwerty42.com -o'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "findomain-test_fastest_subdomain_finding.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = '{} -t {} -q'.format(config["FINDOMAIN_TOOL_PATH"], config["DOMAIN_TEXT"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("findomain-test_fastest_subdomain_finding -> {}".format(str(e)))
        assert False


@pytest.mark.skip
@pytest.mark.findomain_do_fastest_screenshot
def test_fastest_screenshot():
    """should return result of 'findomain -t 42qwerty42.com -s ./'"""
    config = ReadConfig.get_all_settings()
    try:
        config["LOGGER"].warning("The function body is missing!")
        assert True
    except Exception as e:
        config["LOGGER"].error("findomain-test_do_fastest_screenshot -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.findomain_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "findomain-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["FINDOMAIN_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("findomain-test_do_custom -> {}".format(str(e)))
        assert False
