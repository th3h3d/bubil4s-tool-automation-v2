from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
import pytest
import requests
import re


def cleanup_check(line, root):
    _regex = "(ROOT.com|ROOT.net|ROOT.org|ROOT.info|ROOT.biz|ROOT.name|ROOT.mobi|ROOT.co|ROOT.us)".replace("ROOT", root)
    if len(re.findall(_regex, line)) > 0:
        if len(re.findall("(href)", line)) > 0:
            return 0
        return line.replace("<TD>", "").replace("</TD>", "").replace(" ", "")
    return 0


def process(source_code, root):
    cleaned_text = ""
    for i in source_code.split("\n"):
        if len(i.split("<BR>")) > 1:
            for j in i.split("<BR>"):
                ret = cleanup_check(j, root)
                if ret != 0:
                    cleaned_text = cleaned_text + ret + "\n"
        else:
            ret = cleanup_check(i, root)
            if ret != 0:
                cleaned_text = cleaned_text + ret + "\n"

    return cleaned_text


@pytest.mark.recon
@pytest.sub_passive
@pytest.mark.crtsh_test_get_crt_subdomain
def test_get_crt_subdomain():
    """should return result of 'Get subs from crt'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "crtsh-test_get_crt_subdomain.txt"
    section_file_name = config["SUB_DOMAIN_FILE"]
    try:
        # Execution and dumping
        source_code = requests.get("https://crt.sh/?q="+config["NAME_TEXT"]).text

        FileOperation.dump_all(output_file_name, process(source_code, config["NAME_TEXT"]))
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))

        # Merging
        FileOperation.merge_unique_sort(output_file_name, section_file_name)
        config["LOGGER"].info("File '{}' is now merged with '{}'".format(output_file_name, section_file_name))
        assert True
    except Exception as e:
        config["LOGGER"].error("crtsh-test_get_crt_subdomain -> {}".format(str(e)))
        assert False

