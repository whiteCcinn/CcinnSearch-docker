import scrapy
from scrapy.loader.processors import MapCompose
from ccinnSearch.utils.function import *
from w3lib.html import remove_tags
import datetime


class ZhihuQuestionItem(scrapy.Item):
    url_object_id = scrapy.Field()
    question_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field(
        input_processor=MapCompose(exclude_none),
    )
    topics = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()

    def clean_data(self):
        self["question_id"] = self["question_id"][0]
        self["topics"] = ",".join(self["topics"])
        self["url"] = self["url"][0]
        self["title"] = "".join(self["title"])
        try:
            self["content"] = "".join(self["content"])
            self["content"] = remove_tags(self["content"])
        except BaseException:
            self["content"] = "无"

        try:
            self["answer_num"] = extract_num("".join(self["answer_num"]))
        except BaseException:
            self["answer_num"] = 0
        self["comments_num"] = extract_num("".join(self["comments_num"]))

        if len(self["watch_user_num"]) == 2:
            watch_user_num_click = self["watch_user_num"]
            self["watch_user_num"] = extract_num_include_dot(watch_user_num_click[0])
            self["click_num"] = extract_num_include_dot(watch_user_num_click[1])
        else:
            watch_user_num_click = self["watch_user_num"]
            self["watch_user_num"] = extract_num_include_dot(watch_user_num_click[0])
        self["crawl_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def save_to_mysql(self):
        # 插入知乎question表的sql语句
        insert_sql = """
                    insert into zhihu_question(url_object_id,question_id, title, content,topics,
                     answer_num, comments_num,watch_user_num, click_num, url,
                      crawl_time
                      )
                    VALUES (%s, %s, %s, %s, %s
                    , %s, %s, %s, %s, %s,
                    %s)
                    ON DUPLICATE KEY UPDATE
                    content=VALUES(content), answer_num=VALUES(answer_num), comments_num=VALUES(comments_num),
                    watch_user_num=VALUES(watch_user_num), click_num=VALUES(click_num)
                """
        self.clean_data()
        sql_params = (
            self['url_object_id'][0], self["question_id"], self["title"], self["content"], self["topics"],
            self["answer_num"], self["comments_num"], self["watch_user_num"], self["click_num"], self['url'],
            self["crawl_time"])

        print ('\n'.join(['%s:%s' % item for item in self.__dict__.items()]))

        return insert_sql, sql_params

    def help_fields(self):
        for field in self.fields:
            print(field, "= scrapy.Field()")


class ZhihuAnswerItem(scrapy.Item):
    url_object_id = scrapy.Field()
    answer_id = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    author_name = scrapy.Field()

    content = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    url = scrapy.Field()
    create_time = scrapy.Field()

    update_time = scrapy.Field()
    crawl_time = scrapy.Field()
