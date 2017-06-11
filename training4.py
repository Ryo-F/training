# 正規表現
import re


def eliminate_parameters(url):
    return re.sub("\?.*", "", url)


def create_parameter_dict(url):
    if '?' in url:
        idx = url.index('?')
        url = url[idx + 1:]
    p_list = []
    print(url)
    while '&' in url:
        p_list.append(url[:url.index('&')])
        url = url[url.index('&') + 1:]
    p_list.append(url)
    dic = {}
    print(p_list)
    for p in p_list:
        dic.update({p[:-p.index('=') + 2]: p[p.index('=') + 1:]})
    return dic


def correct_email_address(ads):
    at_mk = ['[at]', '_at_', '_atmk_', 'at']
    dt = ['[dot]', 'dot']
    ads = ads.replace('[at]', '@')

    if ' ' in ads:
        ads = ads.replace(' ', '')
        for at in at_mk:
            ads = ads.replace(at, '@')
        for dot in dt:
            ads = ads.replace(dot, '.')

    return print(ads)
