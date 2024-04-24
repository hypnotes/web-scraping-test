from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from comments.comment_report import CommentReport
from comments.constants import *
from selenium.common.exceptions import StaleElementReferenceException
import time 

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--headless=new')
options.add_experimental_option('detach', True)

start_time = time.time()
class Comments(webdriver.Chrome):
    def __init__(self, url: str, teardown: bool = False):
        self.teardown = teardown
        super(Comments, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()
        self.url = url
        print(f'--- ✨ 강의 {COURSE_ID} 수집 시작 ---')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_and_go_to_comment(self):
        self.get(self.url)
        self.find_element(By.CLASS_NAME, 'tab.min-w-124-px').click()

    def get_title(self):
        title = self.find_element(By.CLASS_NAME, 'wb-product-view__title').text
        print(f'     ➡️ 강의제목: {title}')
        return title
    
    def get_total(self):
        totalReview = self.find_element(By.CLASS_NAME, 'review-count-header').text
        totalRating = self.find_element(By.CLASS_NAME, 'review-point-set').text
        print(totalReview, totalRating)
        return totalReview, totalRating
    
    def click_see_more(self):
        while True:
            try:
                see_more_button = self.find_elements(By.CLASS_NAME, 'review-total-item-more')
                if not see_more_button:
                    break  
                see_more_button[0].click()
            except StaleElementReferenceException:
                continue
        print(f'     ✔️ {round(time.time() - start_time, 2)}: 더보기 버튼 클릭 완료')
        return True

    def report_comments(self):
        self.click_see_more()
        comment_section = self.find_element(By.CLASS_NAME, 'review-list-wrapper')
        
        report_inst = CommentReport(comment_section)
        report = report_inst.pull_attributes()
        print(f'     ✔️ {round(time.time() - start_time, 2)}: 총 {report[-1][0]}개의 리뷰 수집 완료')
        return report

    def write_to_file(self, report: List[List[str]]):
        with open(f'{COURSE_ID}.txt', 'w') as file:
            for comment in report:
                file.write(f'{comment}\n')
        print(f'     ✔️ 총 {round(time.time() - start_time, 2)} 초 소요됨')
