from utilities.file_operations import FileOperation
from utilities.read_configs import ReadConfig
from utilities.os_operations import OSOperations
import pytest

def get_urls(domain, name):
    urls = dict()
    urls['password_domain'] = "https://github.com/search?q=%22$1%22+password&type=Code"
    urls['password_name'] = "https://github.com/search?q=%22$without_suffix%22+password&type=Code"
    urls['npmrc_auth_domain'] = "https://github.com/search?q=%22$1%22+npmrc%20_auth&type=Code"
    urls['npmrc_auth_name'] = "https://github.com/search?q=%22$without_suffix%22+npmrc%20_auth&type=Code"
    urls['dockercfg_domain'] = "https://github.com/search?q=%22$1%22+dockercfg&type=Code"
    urls['dockercfg_name'] = "https://github.com/search?q=%22$without_suffix%22+dockercfg&type=Code"
    urls['pem_private_domain'] = "https://github.com/search?q=%22$1%22+pem%20private&type=Code"
    urls['pem_private_name'] = "https://github.com/search?q=%22$without_suffix%22+extension:pem%20private&type=Code"
    urls['id_rsa_domain'] = "https://github.com/search?q=%22$1%22+id_rsa&type=Code"
    urls['id_rsa_name'] = "https://github.com/search?q=%22$without_suffix%22+id_rsa&type=Code"
    urls['aws_access_key_id_domain'] = "https://github.com/search?q=%22$1%22+aws_access_key_id&type=Code"
    urls['aws_access_key_id_name'] = "https://github.com/search?q=%22$without_suffix%22+aws_access_key_id&type=Code"
    urls['s3cfg_domain'] = "https://github.com/search?q=%22$1%22+s3cfg&type=Code"
    urls['s3cfg_name'] = "https://github.com/search?q=%22$without_suffix%22+s3cfg&type=Code"
    urls['htpasswd_domain'] = "https://github.com/search?q=%22$1%22+htpasswd&type=Code"
    urls['htpasswd_name'] = "https://github.com/search?q=%22$without_suffix%22+htpasswd&type=Code"
    urls['git_credentials_domain'] = "https://github.com/search?q=%22$1%22+git-credentials&type=Code"
    urls['git_credentials_name'] = "https://github.com/search?q=%22$without_suffix%22+git-credentials&type=Code"
    urls['bashrc_password_domain'] = "https://github.com/search?q=%22$1%22+bashrc%20password&type=Code"
    urls['bashrc_password_name'] = "https://github.com/search?q=%22$without_suffix%22+bashrc%20password&type=Code"
    urls['sshd_config_domain'] = "https://github.com/search?q=%22$1%22+sshd_config&type=Code"
    urls['sshd_config_name'] = "https://github.com/search?q=%22$without_suffix%22+sshd_config&type=Code"
    urls['xoxp_OR_xoxb_OR_xoxa_domain'] = "https://github.com/search?q=%22$1%22+xoxp%20OR%20xoxb%20OR%20xoxa&type=Code"
    urls['xoxp_OR_xoxb_OR_xoxa_name'] = "https://github.com/search?q=%22$without_suffix%22+xoxp%20OR%20xoxb&type=Code"
    urls['SECRET_KEY_domain'] = "https://github.com/search?q=%22$1%22+SECRET_KEY&type=Code"
    urls['SECRET_KEY_name'] = "https://github.com/search?q=%22$without_suffix%22+SECRET_KEY&type=Code"
    urls['client_secret_domain'] = "https://github.com/search?q=%22$1%22+client_secret&type=Code"
    urls['client_secret_name'] = "https://github.com/search?q=%22$without_suffix%22+client_secret&type=Code"
    urls['sshd_config_domain'] = "https://github.com/search?q=%22$1%22+sshd_config&type=Code"
    urls['sshd_config_name'] = "https://github.com/search?q=%22$without_suffix%22+sshd_config&type=Code"
    urls['github_token_domain'] = "https://github.com/search?q=%22$1%22+github_token&type=Code"
    urls['github_token_name'] = "https://github.com/search?q=%22$without_suffix%22+github_token&type=Code"
    urls['api_key_domain'] = "https://github.com/search?q=%22$1%22+api_key&type=Code"
    urls['api_key_name'] = "https://github.com/search?q=%22$without_suffix%22+api_key&type=Code"
    urls['FTP_domain'] = "https://github.com/search?q=%22$1%22+FTP&type=Code"
    urls['FTP_name'] = "https://github.com/search?q=%22$without_suffix%22+FTP&type=Code"
    urls['app_secret_domain'] = "https://github.com/search?q=%22$1%22+app_secret&type=Code"
    urls['app_secret_name'] = "https://github.com/search?q=%22$without_suffix%22+app_secret&type=Code"
    urls['passwd_domain'] = "https://github.com/search?q=%22$1%22+passwd&type=Code"
    urls['passwd_name'] = "https://github.com/search?q=%22$without_suffix%22+passwd&type=Code"
    urls['s3_yml_domain'] = "https://github.com/search?q=%22$1%22+.env&type=Code"
    urls['s3_yml_name'] = "https://github.com/search?q=%22$without_suffix%22+.env&type=Code"
    urls['exs_domain'] = "https://github.com/search?q=%22$1%22+.exs&type=Code"
    urls['exs_name'] = "https://github.com/search?q=%22$without_suffix%22+.exs&type=Code"
    urls['beanstalkd_yml_domain'] = "https://github.com/search?q=%22$1%22+beanstalkd.yml&type=Code"
    urls['beanstalkd_yml_name'] = "https://github.com/search?q=%22$without_suffix%22+beanstalkd.yml&type=Code"
    urls['deploy_rake_domain'] = "https://github.com/search?q=%22$1%22+deploy.rake&type=Code"
    urls['deploy_rake_name'] = "https://github.com/search?q=%22$without_suffix%22+deploy.rake&type=Code"
    urls['mysql_domain'] = "https://github.com/search?q=%22$1%22+mysql&type=Code"
    urls['mysql_name'] = "https://github.com/search?q=%22$without_suffix%22+mysql&type=Code"
    urls['credentials_domain'] = "https://github.com/search?q=%22$1%22+credentials&type=Code"
    urls['credentials_name'] = "https://github.com/search?q=%22$without_suffix%22+credentials&type=Code"
    urls['PWD_domain'] = "https://github.com/search?q=%22$1%22+PWD&type=Code"
    urls['PWD_name'] = "https://github.com/search?q=%22$without_suffix%22+PWD&type=Code"
    urls['deploy_rake_domain'] = "https://github.com/search?q=%22$1%22+deploy.rake&type=Code"
    urls['deploy_rake_name'] = "https://github.com/search?q=%22$without_suffix%22+deploy.rake&type=Code"
    urls['bash_history_domain'] = "https://github.com/search?q=%22$1%22+.bash_history&type=Code"
    urls['bash_history_name'] = "https://github.com/search?q=%22$without_suffix%22+.bash_history&type=Code"
    urls['sls_domain'] = "https://github.com/search?q=%22$1%22+.sls&type=Code"
    urls['sls_name'] = "https://github.com/search?q=%22$without_suffix%22+PWD&type=Code"
    urls['secrets_domain'] = "https://github.com/search?q=%22$1%22+secrets&type=Code"
    urls['secrets_name'] = "https://github.com/search?q=%22$without_suffix%22+secrets&type=Code"
    urls['composer_json_domain'] = "https://github.com/search?q=%22$1%22+composer.json&type=Code"
    urls['composer_json_name'] = "https://github.com/search?q=%22$without_suffix%22+composer.json&type=Code"
    urls['dotfile_domain'] = "https://github.com/search?q=%22$1%22+dotfile&type=Code"
    urls['dotfile_name'] = "https://github.com/search?q=%22$without_suffix%22+dotfile&type=Code"

    for i in urls.keys():
        urls[i] = urls[i].replace("$1", domain)
        urls[i] = urls[i].replace("$without_suffix", name)

    return urls


@pytest.mark.recon
@pytest.mark.githubdork_test_github_dorking
def test_github_dorking():
    """should return result of 'GITHUB DORK!'"""
    config = ReadConfig.get_all_settings()
    output_file_name = "github-test_github_dorking.html"

    try:
        # Design
        result = ""
        urls = get_urls(config["DOMAIN_TEXT"], config["NAME_TEXT"])
        for i in urls.keys():
            result = result + '<tr><td>'+i+'</td><td><a href="'+urls[i]+'">'+urls[i]+'</a></td></tr>'
        html_first = """<!DOCTYPE html><html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style></head><body><h2>GitHub Dorks</h2><p>Please log in Github before going through links</p><table><tr><th>Search For</th><th>URL</th></tr>"""
        html_last = """"</table></body></html>"""
        full_html = html_first +result + html_last
        # Execution and dumping
        FileOperation.dump_all(output_file_name, full_html)
        config["LOGGER"].info("Result dumped into '{}'".format(output_file_name))
        # Merging

        assert True
    except Exception as e:
        config["LOGGER"].error("github-test_github_dorking -> {}".format(str(e)))
        assert False
