from selenium import webdriver
import time
from utilities.utility_logger import UtilityLogger


class PythonFunction:
    class_path = "python_func.PythonFunction"
    ulogger = UtilityLogger()

    @classmethod
    def take_website_screenshot(cls, url, browser_type, output_path, driver_path, logger):
        """should return name of screenshot"""
        browser = ""
        try:
            if browser_type == 'chrome':
                browser = webdriver.Firefox(executable_path="{}".format(driver_path))
            elif browser_type == 'firefox':
                browser = webdriver.Firefox(executable_path="{}".format(driver_path))
            else:
                raise ValueError("Defined browser has not been matched!")

            if "https://" not in url and "http://" not in url:
                url = "http://{}".format(url)

            browser.get(url)
            time.sleep(4)
            ss_full_path = "{}/{}.png".format(output_path, url.replace("/", "").replace("http:", "").replace("https:", ""))
            browser.save_screenshot(ss_full_path)
            browser.close()
            return ss_full_path
        except Exception as e:
            browser.close()
            # Manual logger for logging
            cls.ulogger.log_this("{} -> get_all_settings -> {}\n".format(str(time.strftime("%Y%m%d-%H:%M:%S - ", time.localtime()))+cls.class_path, str(e)))
