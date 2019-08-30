# -*- coding: utf-8 -*-
import scrapy
from ..items import HonorItem


class HonorSpider(scrapy.Spider):
    name = 'honor'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        """
        抓取列表页
        :param response:
        :return:
        """
        # 获取英雄详情链接
        honor_list = response.xpath("//ul[@class='herolist clearfix']/li/a/@href").extract()

        for link in honor_list:
            honor_link = "https://pvp.qq.com/web201605/" + link
            yield scrapy.Request(honor_link, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        解析详情页
        :param response:
        :return:
        """
        viability = response.xpath("/html/body/div[3]/div[1]/div/div/div[1]/ul/li[1]/span/i/@style").extract_first()
        ad = response.xpath("/html/body/div[3]/div[1]/div/div/div[1]/ul/li[2]/span/i/@style").extract_first()
        cover_skill = response.xpath("//body/div[3]/div[1]/div/div/div[1]/ul/li[3]/span/i/@style").extract_first()
        difficulity = response.xpath("//body/div[3]/div[1]/div/div/div[1]/ul/li[4]/span/i/@style").extract_first()

        item = HonorItem()

        # 英雄编号
        item["ename"] = response.url[-9:-6]
        # 英雄外号
        item["title"] = response.xpath("//body/div[3]/div[1]/div/div/div[1]/h3/text()").extract_first()
        # 英雄名字
        item["cname"] = response.xpath("/html/body/div[3]/div[1]/div/div/div[1]/h2/text()").extract_first()
        # 生存能力
        item["viability"] = viability[viability.find(":") + 1:]
        # 攻击伤害
        item["ad"] = ad[ad.find(":") + 1:]
        # 技能效果
        item["cover_skill"] = cover_skill[cover_skill.find(":") + 1:]
        # 上手难度
        item["difficulity"] = difficulity[difficulity.find(":") + 1:]
        # 英雄故事
        item["hero_story"] = response.xpath("//*[@id='hero-story']/div[2]/p/text()").extract()
        # 铭文tips
        item["inscr_tips"] = response.xpath(
            "/html/body/div[3]/div[2]/div/div[1]/div[3]/div[2]/p/text()").extract_first()
        # 出装tips
        item["eq_tips"] = response.xpath(
            "/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[1]/p/text()").extract_first()

        yield item
