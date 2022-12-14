import requests
from lxml import etree

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 ',
}


def get_icon(url):
    """
    获取指定网站的图标

    :param url: 网站地址
    :return: 图标地址(列表)
    """
    home_page = get_website_home_page(url)
    # todo 缓存逻辑
    data = {}
    if home_page in data.keys():
        return data[home_page]
    response = requests.get(url, headers=HEADERS, timeout=5)
    html = etree.HTML(response.text)
    if html is None:
        return []
    items = html.xpath('//head/link[contains(@rel,"icon")]')
    icons = [i.get("href") for i in items]
    # 如果href中是相对路径, 则补上首页地址
    for i in range(len(icons)):
        if icons[i].startswith("http"):
            pass
        else:
            icons[i] = home_page + icons[i]
    return icons


def get_website_home_page(url):
    """
    获取网站主页链接，格式为 http[s]://domain[:port]
    """
    return "/".join(url.split("/")[:3])


if __name__ == '__main__':
    # test
    print(get_icon("https://bxs.ink/"))
