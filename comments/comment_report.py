from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class CommentReport: 
    def __init__(self, comment_section: WebElement):
        self.comment_section = comment_section
        self.comment_boxes = self.pull_comment_boxes()

    def pull_comment_boxes(self):
        return self.comment_section.find_elements(By.CLASS_NAME, 'review-list-item-wrapper')
    
    def pull_attributes(self):
        report = []

        for index, commentBox in enumerate(self.comment_boxes):
            info_set = commentBox.find_element(By.CLASS_NAME, 'review-list-item-info')
            reviewer = info_set.find_element(By.CSS_SELECTOR, ':first-child').text
            rating = info_set.find_element(By.CLASS_NAME, 'info-star-set').text
            comment = commentBox.find_element(By.CLASS_NAME, 'review-list-item-contents').get_attribute('innerText').strip().replace('\n', ' ')
            review_footer = commentBox.find_element(By.CLASS_NAME, 'review-item-foot')
            date = review_footer.find_element(By.CSS_SELECTOR, ':first-child').text
            likes = review_footer.find_element(By.CLASS_NAME, 'thumb-count').text
            report.append([index+1, reviewer, date, rating, comment, likes])
        return report


