import random
import time
import typing

from selenium.common.exceptions import (
    NoAlertPresentException,
    UnexpectedAlertPresentException,
)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import custom_logging

if typing.TYPE_CHECKING:
    pass


def bingSearch(browser: WebDriver, word: str, isMobile: bool):
    from util import ErrorReport, ErrorReporter

    logger: custom_logging.FileStreamLogger = custom_logging.FileStreamLogger(
        console=True, colors=True
    )

    browser.get("https://bing.com")
    time.sleep(2)
    searchbar = browser.find_element(By.ID, "sb_form_q")
    searchbar.send_keys(word)
    searchbar.submit()
    time.sleep(random.randint(10, 15))
    points = 0
    try:
        if not isMobile:
            points = int(
                browser.find_element(By.ID, "id_rc").get_attribute("innerHTML")
            )
        else:
            try:
                browser.find_element(By.ID, "mHamburger").click()
            except UnexpectedAlertPresentException:
                try:
                    browser.switch_to.alert.accept()
                    time.sleep(1)
                    browser.find_element(By.ID, "mHamburger").click()
                except NoAlertPresentException:
                    pass
            time.sleep(1)
            points = int(
                browser.find_element(By.ID, "fly_id_rc").get_attribute("innerHTML")
            )
    except Exception as e:
        errorReport: ErrorReport = ErrorReporter().generate_report(
            browser, accountData="RETRIEVE", exception=e
        )
        logger.critical(
            "Unknown error trying to complete single bing search."
            f"Error report has been generated: {errorReport.file_path}"
        )
    return points
