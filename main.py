from comments.comments import Comments
from comments.constants import *

with Comments(url= BASE_URL, teardown=False) as bot:
    bot.land_and_go_to_comment()
    bot.get_title()
    # bot.get_total()
    bot.write_to_file(bot.report_comments())