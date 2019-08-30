# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HonorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 英雄编号
    ename = scrapy.Field()
    # 英雄外号
    title = scrapy.Field()
    # 英雄名字
    cname = scrapy.Field()
    # 英雄视频
    hvideo_url = scrapy.Field()
    # 生存能力
    viability = scrapy.Field()
    # 攻击伤害
    ad = scrapy.Field()
    # 技能效果
    cover_skill = scrapy.Field()
    # 上手难度
    difficulity = scrapy.Field()
    # 英雄故事
    hero_story = scrapy.Field()
    # 铭文tips
    inscr_tips = scrapy.Field()
    # 出装tips
    eq_tips = scrapy.Field()
    # 英雄介绍视频
    honor_link = scrapy.Field()
