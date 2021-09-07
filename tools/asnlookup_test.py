from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
import pytest
import requests


@pytest.mark.asnlookup_get_ipv4_space
def test_get_ipv4_space():
    # Retrieve ipv4 space from asnlookup.com
    API = 'http://asnlookup.com/api/lookup?org='
    headers = {'User-Agent': 'ASNLookup PY/Client'}
    config = ReadConfig.get_all_settings()
    output_file_name = "asnlookup-test_get_ipv4_space.txt"
    try:
        # Execution and dumping
        return_value = ""
        response = requests.get(API + config["DOMAIN_TEXT"].replace('_', ' '), headers=headers).text.replace("[", "").replace("]", "").replace("\n", "").replace('"', "")
        for i in response.split(","):
            if ':' not in i:
                return_value = return_value + i + "\n"
            else:
                pass
        config["LOGGER"].info("Returned Value".format(return_value))
        FileOperation.dump_all(output_file_name, return_value)
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("asnlookup-test_get_ipv4_space -> {}".format(str(e)))
        assert False


@pytest.mark.asnlookup_get_ipv6_space
def test_get_ipv6_space():
    # Retrieve ipv6 space from asnlookup.com
    API = 'http://asnlookup.com/api/lookup?org='
    headers = {'User-Agent': 'ASNLookup PY/Client'}
    config = ReadConfig.get_all_settings()
    output_file_name = "asnlookup-test_get_ipv6_space.txt"
    try:
        # Execution and dumping
        return_value = ""
        response = requests.get(API + config["DOMAIN_TEXT"].replace('_', ' '), headers=headers).text.replace("[", "").replace("]", "").replace("\n", "").replace('"', "")
        for i in response.split(","):
            if ':' not in i:
                pass
            else:
                return_value = return_value + i + "\n"
        FileOperation.dump_all(output_file_name, return_value)
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("asnlookup-test_get_ipv6_space -> {}".format(str(e)))
        assert False
