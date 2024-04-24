from comments.comments import Comments
from comments.constants import *
import time 

start_time = time.time()
print(f'--- ✨ 강의 {COURSE_ID} 수집 시작 ---')
with Comments(url= BASE_URL, teardown=False) as bot:
    bot.land_and_go_to_comment()
    bot.get_title()
    # bot.get_total()
    bot.write_to_file(bot.report_comments())

print(f'     ⑇ {round(time.time() - start_time, 2)} 초 소요됨')