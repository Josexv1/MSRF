import custom_logging
import util
from selenium.webdriver.chrome.webdriver import WebDriver


from ..models.dashboard_data import DashboardData


def load_dashboard_data(browser: WebDriver) -> DashboardData | None:
    logger: custom_logging.FileStreamLogger = custom_logging.FileStreamLogger(colors=True, console=True)
    logger.info("loading dashboard data")
    browser.get("https://rewards.bing.com")
    try:
        return util.DashboardData(**browser.execute_script("return dashboard"))
    except Exception as e:
        # Since this is breaking, it may be ideal to exit the thread with sys.exit(). tbd.
        logger.critical(f"Unable to load dashboard data. {e}")

