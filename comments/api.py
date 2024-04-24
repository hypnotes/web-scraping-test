from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumwire.utils import decode 
from comments.constants import *
import requests

# TODO: 여기서 seleniumwire로 하나를 더 여는데, 비효율적일 것 같지만 일단 고
options = Options()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)

class CommentApi: 
    def __init__(self, totalCommentCount = 0):
        self.comment_api_url = ''
        self.total_comment_count = totalCommentCount      

    def get_modified_api(self, request):
        if (API_URL in request.url):
            a, _ = request.url.split('pageSize=')
            self.comment_api_url = f'{a}pageSize='
            print('     ⑇ 🔗 ', self.comment_api_url )

    def intercept_api_request(self):
        driver.request_interceptor = self.get_modified_api
        driver.get(BASE_URL)

    def divide_apis(self):
        pageSize = MAX_COMMENT_REQUEST
        pageNo = 0
        report = []
        # TODO: 컷 안당하려면 api 호출 사이에 랜덤 딜레이를 줘야할 것 같음
        while pageSize * pageNo < self.total_comment_count:
            pageNo += 1
            new_url = self.comment_api_url + str(pageSize) + f'&pageNo={pageNo}'
            response = requests.get(new_url)
            print(f'          {pageNo}번째 request 중... ({pageSize-MAX_COMMENT_REQUEST}~{pageSize*pageNo})')
            report.extend(response.json()['data']['items'])
        return report
    
    def get_comments(self):
        return self.divide_apis()