from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


@pytest.mark.recon
@pytest.mark.reversewhois
@pytest.mark.amass_test_intel_whois
def test_intel_whois():
    """should return result of 'amass intel -d 42qwerty42.com -whois'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_intel_whois.txt"
    section_file_name = config["REVERSE_WHOIS_FILE"]
    try:
        # Design
        command = "{} intel -d {} -whois".format(config["AMASS_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_intel_whois -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.amass_intel_get_asn
def test_intel_get_asn():
    """should return result of 'amass intel --org 42qwerty42'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_intel_get_asn.txt"

    try:
        # Design
        command = "{} intel --org {}".format(config["AMASS_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_intel_get_asn -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.amass_test_intel_asn
def test_intel_asn():
    """should return result of 'amass intel -asn 42qwerty42'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_intel_asn.txt"

    try:
        # Design
        command = "{} intel -asn {}".format(config["AMASS_TOOL_PATH"], config["ASN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_intel_asn -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.sub_passive
@pytest.mark.amass_test_enum_passive
def test_enum_passive():
    """should return result of 'amass enum -passive -d 42qwerty42.com'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_enum_passive.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = "{} enum -passive -d {}".format(config["AMASS_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_enum_passive -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.sub_active
@pytest.mark.amass_test_enum_active
def test_enum_active():
    """should return result of 'amass enum -active -d 42qwerty42.com'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_enum_active.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Design
        command = "{} enum -active -d {}".format(config["AMASS_TOOL_PATH"], config["DOMAIN_TEXT"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_enum_active -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.amass_test_custom
def test_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "amass-test_custom.txt"
    try:
        # Design
        command = "{}".format(config["AMASS_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("amass-test_custom -> {}".format(str(e)))
        assert False
