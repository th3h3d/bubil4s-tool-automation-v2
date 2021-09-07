from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest
import os
import time


def thread_holder(second, logger):
    """This function will help to stacked process to stop"""
    try:
        logger.info("Thread has started!")
        time.sleep(int(second))
        command = "ping -c 1 google.com"
        logger.info("'{}' is executed!".format(command))
        OSOperations.execute_shell_command(command)
    except Exception as e:
        logger.error("dnmasscan-thread_holder -> {}".format(str(e)))


@pytest.mark.port_scan
@pytest.mark.masscan_test_one_port_scan
def test_one_port_scan():
    """should return result of 'masscan -p80 54.250.0.0/16 --rate=500 -oG output.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "masscan-test_one_port_scan.txt"
    try:
        thread_holder(config["MASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["MASSCAN_OUTPUT_FILE_PATH"], "masscan-do_one_port_scan-default_output.txt")
        command = '{} -p{} {} --rate=500 -oG {}'.format(config["MASSCAN_TOOL_PATH"], config["MASSCAN_TARGETED_SINGLE_PORT"], config["MASSCAN_TARGETED_IP_RANGE"], input_full_path)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("masscan-test_one_port_scan -> {}".format(str(e)))
        assert False


@pytest.mark.port_scan
@pytest.mark.masscan_test_many_port_scan
def test_many_port_scan():
    """should return result of 'masscan -p80,443 54.250.0.0/16 --rate=500 -oG output.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "masscan-test_many_port_scan.txt"
    try:
        thread_holder(config["MASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["MASSCAN_OUTPUT_FILE_PATH"], "masscan-do_many_port_scan-default_output.txt")
        command = '{} -p{} {} --rate=500 -oG {}'.format(config["MASSCAN_TOOL_PATH"], config["MASSCAN_TARGETED_MULTIPLE_PORTS"], config["MASSCAN_TARGETED_IP_RANGE"], input_full_path)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("masscan-test_many_port_scan -> {}".format(str(e)))


@pytest.mark.port_scan
@pytest.mark.masscan_test_port_range_scan
def test_port_range_scan():
    """should return result of 'masscan -p1-80 54.250.0.0/16 --rate=500 -oG output.txt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "masscan-test_port_range_scan.txt"
    try:
        thread_holder(config["MASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["MASSCAN_OUTPUT_FILE_PATH"], "masscan-do_port_range_scan-default_output.txt")
        command = '{} -p{} {} --rate=500 -oG {}'.format(config["MASSCAN_TOOL_PATH"], config["MASSCAN_TARGETED_PORT_RANGE"], config["MASSCAN_TARGETED_IP_RANGE"], input_full_path)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("masscan-test_port_range_scan -> {}".format(str(e)))


@pytest.mark.custom
@pytest.mark.masscan_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "masscan-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["MASSCAN_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("masscan-test_do_custom -> {}".format(str(e)))
        assert False
