from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.gau_test_get_all_urls
def test_get_all_urls():
    """should return result of 'gau 42qwerty42.com'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gau-test_get_all_urls.txt"
    section_file_name = config["URLS_FILE"]
    try:
        # Design
        command = '{} -b {} {}'.format(config["GAU_TOOL_PATH"], config["GAU_SKIP_EXTENSIONS"], config["DOMAIN_TEXT"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_both(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("gau-test_get_all_urls -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.gau_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gau-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["GAU_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("gau-test_do_custom -> {}".format(str(e)))
        assert False
