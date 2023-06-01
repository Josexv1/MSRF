import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import custom_logging
import util


def complete_more_promotion_quiz(*, browser: WebDriver, cardNumber: int):
    logger: custom_logging.FileStreamLogger = custom_logging.FileStreamLogger(
        console=True, colors=True
    )
    browser.find_element(
        By.XPATH,
        '//*[@id="more-activities"]/div/mee-card['
        + str(cardNumber)
        + "]/div/card-content/mee-rewards-more-activities-card-item/div/a",
    ).click()
    time.sleep(1)
    browser.switch_to.window(window_name=browser.window_handles[1])
    time.sleep(8)
    if not util.waitUntilQuizLoads(browser):  # error report is done by caller
        # check that quiz isnt already done...
        logger.critical("Quiz did not load. Resetting tabs and exiting module")
        raise Exception("Forced exception due to missing quiz load.")

    browser.find_element(By.XPATH, '//*[@id="rqStartQuiz"]').click()
    util.waitUntilVisible(
        browser, By.XPATH, '//*[@id="currentQuestionContainer"]/div/div[1]', 10
    )
    time.sleep(3)
    numberOfQuestions = browser.execute_script(
        "return _w.rewardsQuizRenderInfo.maxQuestions"
    )
    numberOfOptions = browser.execute_script(
        "return _w.rewardsQuizRenderInfo.numberOfOptions"
    )
    logger.info(f"iterating {numberOfQuestions} for current quiz")
    for question in range(numberOfQuestions):
        logger.info(f"Question {question}/{numberOfQuestions}")
        if numberOfOptions == 8:
            answers = []
            for i in range(8):
                if (
                    browser.find_element(By.ID, "rqAnswerOption" + str(i))
                    .get_attribute("iscorrectoption")
                    .lower()
                    == "true"
                ):
                    answers.append("rqAnswerOption" + str(i))
            for answer in answers:
                browser.find_element(By.ID, answer).click()
                time.sleep(5)
                if not util.waitUntilQuestionRefresh(browser):
                    return
            time.sleep(5)
        elif numberOfOptions == 4:
            correctOption = browser.execute_script(
                "return _w.rewardsQuizRenderInfo.correctAnswer"
            )
            for i in range(4):
                if (
                    browser.find_element(
                        By.ID, "rqAnswerOption" + str(i)
                    ).get_attribute("data-option")
                    == correctOption
                ):
                    browser.find_element(By.ID, "rqAnswerOption" + str(i)).click()
                    time.sleep(5)
                    if not util.waitUntilQuestionRefresh(browser):
                        return
                    break
            time.sleep(5)
    time.sleep(5)
    browser.close()  # closes current window?
    time.sleep(2)
    logger.info("Returning to main window.")
    browser.switch_to.window(window_name=browser.window_handles[0])
    time.sleep(2)
