import re

class CommentApiReport: 
    def __init__(self, comment_boxes):
        self.comment_boxes = comment_boxes
        
    # html 태그, 공백, \r, \n 제거
    def remove_html_tags(self, text):
        clean_text = re.sub(r'<[^>]*>|&nbsp;|\r|\n', ' ', text)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        return clean_text.strip()
    
    def pull_attributes(self):
        report = []
        for index, commentBox in enumerate(self.comment_boxes):
            reviewer = commentBox['nickName']
            rating = commentBox['reviewPoint']
            comment = self.remove_html_tags(commentBox['reviewText'])
            date = commentBox['regDate']
            likes = commentBox['likeCount']
            report.append([index+1, reviewer, date, rating, comment, likes])
        return report


