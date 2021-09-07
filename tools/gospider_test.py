from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest


def clean_response(response):
    response = response.replace("\n[", "@th3h3d@[").replace("\nh", "@th3h3d@h")
    response = response.replace("\n", "")
    response = response.split("@th3h3d@")
    return_val = ""
    for i in response:
        return_val = return_val + i + "\n"
    return return_val


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.gospider_test_single_site_all
def test_single_site_all():
    """should return result of 'gospider -s "https://42qwerty42.com/" -c 10 -d 5'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gospider-test_single_site_all.txt"
    section_file_name = config["URLS_FILE"]
    try:
        # Design
        command = '{} -s "https://{}/" -c 10 -d {}'.format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], 3)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, clean_response(OSOperations.execute_shell_command(command)))
        FileOperation.dump_all('cleaned_'+output_file_name, clean_response(OSOperations.execute_shell_command(command)))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        FileOperation.clean_all('cleaned_'+output_file_name, ["[href] - ", "[url] - ", "[javascript] - ", "[linkfinder] - ", "[code-200] - ", "[robots] - "])
        config["LOGGER"].info("File '{}' is now cleaned".format(output_file_name))
        FileOperation.merge_both('cleaned_'+output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("gospider-test_single_site_all -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.gospider_test_single_site_only_urls
def test_single_site_only_urls():
    """should return result of 'gospider -q -s "https://42qwerty42.com/" -c 10 -d 5'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gospider-test_single_site_only_urls.txt"
    try:
        command = '{} -q -s "https://{}/" -c 10 -d {}'.format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], 3)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, clean_response(OSOperations.execute_shell_command(command)))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("gospider-test_single_site_only_urls -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.gospider_test_single_site_blacklist
def test_single_site_blacklist():
    """should return result of 'gospider -s "https://42qwerty42.com/" -c 10 -d 5 --blacklist ".(woff|pdf)"'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gospider-test_single_site_blacklist.txt"
    try:
        command = '{} -s "https://{}/" -c 10 -d {} --blacklist ".({})"'\
            .format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], 3, config["GOSPIDER_BLACK_LIST"])
        # Execution and dumping
        FileOperation.dump_all(output_file_name, clean_response(OSOperations.execute_shell_command(command)))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("gospider-test_single_site_blacklist -> {}".format(str(e)))
        assert False


@pytest.mark.recon
@pytest.mark.findasset
@pytest.mark.gospider_test_single_site_other_source
def test_single_site_other_source():
    """should return result of 'gospider -s "https://42qwerty42.com/" -c 10 -d 5 --other-source'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gospider-test_single_site_other_source.txt"
    try:
        command = '{} -s "https://{}/" -c 10 -d {} --other-source'.format(config["GOSPIDER_TOOL_PATH"], config["DOMAIN_TEXT"], 3)
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, clean_response(OSOperations.execute_shell_command(command)))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging
        assert True
    except Exception as e:
        config["LOGGER"].error("gospider-test_single_site_other_source -> {}".format(str(e)))
        assert False


@pytest.mark.custom
@pytest.mark.gospider_do_custom
def test_do_custom():
    """should return result of 'X'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "gospider-test_do_custom.txt"
    try:
        # Design
        command = "{}".format(config["GOSPIDER_CUSTOM_COMMAND"])
        config["LOGGER"].info("'{}' is executed!".format(command))
        # Execution and dumping
        FileOperation.dump_all(output_file_name, OSOperations.execute_shell_command(command))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("gospider-test_do_custom -> {}".format(str(e)))
        assert False

