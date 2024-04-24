from comments.comments import Comments
from comments.constants import *

with Comments(url= BASE_URL, teardown=False, mode=MODE) as bot:
    bot.land_and_go_to_comment()
    bot.get_title()
    bot.get_total()
    report = bot.report_comments()
    bot.write_to_file(report)

