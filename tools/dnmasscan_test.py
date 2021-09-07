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
@pytest.mark.dnmasscan_test_one_port_scan
def test_one_port_scan():
    """should return result of 'dnmasscan input_file.txt output_file.txt -pX -oG masscan.log --rate=500'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "dnmasscan-test_one_port_scan.txt"

    try:
        thread_holder(config["DNMASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["INPUT_OUTPUT_PATH"], config["SUB_DOMAIN_FILE_PATH"])

        output_ip_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                           "dnmasscan-test_do_one_port_scan-ip-default_output.txt")

        output_masscan_log_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                                    "dnmasscan-test_do_one_port_scan-masscan_log-default_output.log")

        command = '{} {} {} -p{} -oG {} --rate=500'.format(config["DNMASSCAN_TOOL_PATH"], input_full_path, output_ip_full_path, config["DNMASSCAN_TARGETED_SINGLE_PORT"], output_masscan_log_full_path)

        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("dnmasscan-test_one_port_scan -> {}".format(str(e)))
        assert False


@pytest.mark.port_scan
@pytest.mark.dnmasscan_test_many_port_scan
def test_many_port_scan():
    """should return result of 'dnmasscan input_file.txt output_file.txt -pX -oG masscan.log --rate=500'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "dnmasscan-test_many_port_scan.txt"
    try:
        thread_holder(config["DNMASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["INPUT_OUTPUT_PATH"], config["SUB_DOMAIN_FILE_PATH"])

        output_ip_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                           "dnmasscan-test_do_one_port_scan-ip-default_output.txt")

        output_masscan_log_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                                    "dnmasscan-test_do_one_port_scan-masscan_log-default_output.log")

        command = '{} {} {} -p{} -oG {} --rate=500'.format(config["DNMASSCAN_TOOL_PATH"], input_full_path, output_ip_full_path, config["DNMASSCAN_TARGETED_MULTIPLE_PORTS"], output_masscan_log_full_path)

        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("dnmasscan-test_many_port_scan -> {}".format(str(e)))
        assert False


@pytest.mark.port_scan
@pytest.mark.dnmasscan_port_range_scan
def test_port_range_scan():
    """should return result of 'dnmasscan input_file.txt output_file.txt -pX -oG masscan.log --rate=500'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "dnmasscan-test_port_range_scan.txt"
    try:
        thread_holder(config["DNMASSCAN_TIMEOUT_SECONDS"], config["LOGGER"])
        # Design
        input_full_path = os.path.join(config["INPUT_OUTPUT_PATH"], config["SUB_DOMAIN_FILE_PATH"])

        output_ip_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                           "dnmasscan-do_port_range_scan-ip-default_output.txt")

        output_masscan_log_full_path = os.path.join(config["DNMASSCAN_OUTPUT_FILE_PATH"],
                                                    "dnmasscan-do_port_range_scan-masscan_log-default_output.log")

        command = '{} {} {} -p{} -oG {} --rate=500'.format(config["DNMASSCAN_TOOL_PATH"], input_full_path, output_ip_full_path, config["DNMASSCAN_TARGETED_PORT_RANGE"], output_masscan_log_full_path)

        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("dnmasscan-test_port_range_scan -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.dnmasscan_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "dnmasscan-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["DNMASSCAN_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("dnmasscan-test_do_custom -> {}".format(str(e)))
        assert False
