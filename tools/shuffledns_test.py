from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest
import os


@pytest.mark.recon
@pytest.mark.sub_brute
@pytest.mark.shuffledns_test_subdomain_bruteforcing
def test_subdomain_bruteforcing():
    """should return result of 'shuffledns -silent -d 42qwerty42.com -w wordlist.txt -r resolvers.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "shuffledns-test_subdomain_bruteforcing.txt"
    try:
        # Design
        word_list = os.path.join(config["TOOL_FOOD_PATH"], config["SHUFFLEDNS_WORD_LIST_FILE"])
        resolver = os.path.join(config["TOOL_FOOD_PATH"], config["SHUFFLEDNS_RESOLVER_FILE"])
        command = '{} -silent -d {} -w {} -r {}'.format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], word_list, resolver)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("shuffledns-test_subdomain_bruteforcing -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.sub_resolver
@pytest.mark.shuffledns_test_subdomain_resolving
def test_subdomain_resolving():
    """should return result of 'shuffledns -silent -d example.com -list example-subdomains.txt -r resolvers.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "shuffledns-test_subdomain_resolving.txt"
    try:
        # Design
        input_subs_list = os.path.join(config["TOOL_FOOD_PATH"], config["ALL_SUB_DOMAINS"])
        resolver = os.path.join(config["TOOL_FOOD_PATH"], config["SHUFFLEDNS_RESOLVER_FILE"])
        command = '{} -silent -d {} -list {} -r {}'.format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], input_subs_list, resolver)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("shuffledns-test_subdomain_resolving -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.shuffledns_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "shuffledns-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["SHUFFLEDNS_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("shuffledns-test_do_custom -> {}".format(str(e)))
        assert False