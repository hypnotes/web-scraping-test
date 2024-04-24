COURSE_ID = 2846
# SCRAPE or API
MODE = 'API' 
# MODE = 'SCRAPE'

MAX_COMMENT_REQUEST = 250

BASE_URL = 'https://weolbu.com/product?displaySeq='+str(COURSE_ID)

API_URL = 'https://api.weolbu.com/v1/user/class/product-reviews?productSeq='