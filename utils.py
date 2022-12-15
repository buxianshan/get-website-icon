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
    # 处理href中为相对路径的情况
    for i in range(len(icons)):
        if icons[i].startswith("http"):
            continue
        if icons[i].startswith("/"):
            icons[i] = home_page + icons[i]
            continue
        # href为相对路径且不是以/开头
        if "#" in url:
            base_url = url.split("#")[0]
        else:
            base_url = url
        sections = base_url.split("/")
        sections[-1] = icons[i]
        icons[i] = "/".join(sections)

    return icons


def get_website_home_page(url):
    """
    获取网站主页链接，格式为 http[s]://domain[:port]
    """
    return "/".join(url.split("/")[:3])


if __name__ == '__main__':
    # test
    print(get_icon("https://bxs.ink/"))
