import csv
import time

from selenium import webdriver
from lxml import etree


def skillOptimize(skills: list) -> str:
    skillStr = ''
    for skill in skills:
        skillStr += str(skill) + ','
    return skillStr.strip(',')


def descriptionOptimize(descriptions: list) -> str:
    descriptionStr = ''
    for description in descriptions:
        descriptionStr += description + '\n'
    return descriptionStr.strip('\n')


def salaryOptimize(salary:str) -> str:
    return salary.split('·')[0]


base_url = 'https://www.zhipin.com'
edge = webdriver.Edge('./msedgedriver.exe')
for page in range(1, 11):
    edge.get('https://www.zhipin.com/web/geek/job?query=%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83&city=100010000'
             '&experience=101&degree=203&position=100508&page={}'.format(page))
    time.sleep(5.0)
    tree = etree.HTML(edge.page_source)
    hrefs = tree.xpath('//a[@class="job-card-left"]/@href')
    with open('./exmaple.csv', 'a', encoding='utf-8') as fp:
        for href in hrefs:
            url = base_url + href
            edge.get(url)
            time.sleep(5.0)
            itemTree = etree.HTML(edge.page_source)
            try:
                jobname = itemTree.xpath('//div[@class="name"]/h1/text()')[0]
                salary = salaryOptimize(itemTree.xpath('//span[@class="salary"]/text()')[0])
                city = itemTree.xpath('//a[@class="text-desc text-city"]/text()')[0]
                skill = skillOptimize(itemTree.xpath('//ul[@class="job-keyword-list"]/li/text()'))
                experinece = itemTree.xpath('//span[@class="text-desc text-experiece"]/text()')[0]
                degree = itemTree.xpath('//span[@class="text-desc text-degree"]/text()')[0]
                description = descriptionOptimize(itemTree.xpath('//div[@class="job-sec-text"]/text()'))
                company = itemTree.xpath('//li[@class="company-name"]/text()')[0]
            except Exception as e:
                print('page: {}, href: {}'.format(page, href))
                continue
            else:
                row = [jobname,
                       '数据开发,数据分析',
                       salary,
                       city,
                       company,
                       skill,
                       experinece,
                       '社招',
                       '数据中心其他',
                       '2023-01-06',
                       description]
                writer = csv.writer(fp)
                writer.writerow(row)
