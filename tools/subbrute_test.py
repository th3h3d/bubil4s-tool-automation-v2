from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest
import os


@pytest.mark.recon
@pytest.mark.sub_brute
@pytest.mark.subbrute_test_subdomain_enum
def test_subdomain_enum():
    """should return result of 'subbrute 42qwerty42.com -r resolver.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subbrute-test_subdomain_enum.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        resolver = os.path.join(config["TOOL_FOOD_PATH"], config["SUBBRUTE_RESOLVER_FILE"])
        command = '{} {} -r {}'.format(config["SUBBRUTE_TOOL_PATH"], config["DOMAIN_TEXT"], resolver)
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subbrute-test_subdomain_enum -> {}".format(str(e)))
        assert False


@pytest.mark.check
@pytest.mark.subbrute_get_record_type
def test_get_record_type():
    """should return result of 'subbrute -s subdomain_list.txt 42qwerty42.com -r resolver.txt --type X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subbrute-test_get_record_type.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        input_subs_list = os.path.join(config["INPUT_OUTPUT_PATH"], config["SUB_DOMAIN_FILE_PATH"])
        resolver = os.path.join(config["TOOL_FOOD_PATH"], config["SUBBRUTE_RESOLVER_FILE"])
        command = '{} -s {} {} -r {} --type {}'.format(config["SUBBRUTE_TOOL_PATH"], input_subs_list, config["DOMAIN_TEXT"], resolver, config["SUBBRUTE_TARGETED_RECORD_TYPE"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subbrute-test_get_record_type -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.subbrute_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "subbrute-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["SUBBRUTE_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("subbrute-test_do_custom -> {}".format(str(e)))
        assert False
