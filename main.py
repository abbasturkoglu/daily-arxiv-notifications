# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from bs4 import BeautifulSoup as bs
import urllib.request


from config import NEW_SUB_URL, KEYWORD_LIST


def main():
    page = urllib.request.urlopen(NEW_SUB_URL)
    soup = bs(page, features="html.parser")
    content = soup.body.find("div", {'id': 'content'})

    issue_title = content.find("h3").text
    dt_list = content.dl.find_all("dt")
    dd_list = content.dl.find_all("dd")
    arxiv_base = "https://arxiv.org/abs/"

    assert len(dt_list) == len(dd_list)

    keyword_list = KEYWORD_LIST
    keyword_dict = {key: [] for key in keyword_list}

    for i in range(len(dt_list)):
        paper = {}
        paper_number = dt_list[i].text.strip().split(" ")[2].split(":")[-1]
        paper['main_page'] = arxiv_base + paper_number
        paper['pdf'] = arxiv_base.replace('abs', 'pdf') + paper_number

        paper['title'] = dd_list[i].find("div", {"class": "list-title mathjax"}).text.replace("Title: ", "").strip()
        paper['authors'] = dd_list[i].find("div", {"class": "list-authors"}).text.replace("Authors:\n", "").replace(
            "\n", "").strip()
        paper['subjects'] = dd_list[i].find("div", {"class": "list-subjects"}).text.replace("Subjects: ", "").strip()
        paper['abstract'] = dd_list[i].find("p", {"class": "mathjax"}).text.replace("\n", " ").strip()

        for keyword in keyword_list:
            if keyword.lower() in paper['abstract'].lower():
                keyword_dict[keyword].append(paper)
    total_paper = 0
    full_report = ''
    for keyword in keyword_list:
        full_report = full_report + '## Keyword: ' + keyword + '\n'

        if len(keyword_dict[keyword]) == 0:
            full_report = full_report + 'There is no result \n'

        for paper in keyword_dict[keyword]:
            report = '### {}\n - **Authors:** {}\n - **Subjects:** {}\n - **Arxiv link:** {}\n - **Pdf link:** {}\n - **Abstract**\n {}' \
                .format(paper['title'], paper['authors'], paper['subjects'], paper['main_page'], paper['pdf'],
                        paper['abstract'])
            full_report = full_report + report + '\n'
        total_paper = total_paper + keyword_dict[keyword]
    
    # Opening the existing HTML file
    Func = open("mail.html","w")

    # Adding input data to the HTML file
    Func.write(full_report)

    # Saving the data into the HTML file
    Func.close()
    return total_paper
if __name__ == '__main__':
    main()
    
