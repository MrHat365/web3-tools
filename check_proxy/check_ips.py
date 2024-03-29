"""
  @ Author:   Mr.Hat
  @ Date:     2024/3/30 01:47
  @ Description: IP地址批量检测是否可用，可用的将存在available.txt总，不可用的将存在unavailable.txt中
  @ History:
"""

import requests
from multiprocessing.dummy import Pool
from loguru import logger


def check_ip(ip_):
    try:
        # 设置timeout
        response = requests.get('http://icanhazip.com/', proxies={"http": 'http://' + ip_}, timeout=10)
    except Exception as e:
        with open('unavailable.txt', 'a', encoding='utf-8') as fp:
            fp.write(ip_)
            fp.write('\n')
    else:
        logger.success(f"{ip_}, 请求成功！")
        with open('available.txt', 'a', encoding='utf-8') as fp:
            fp.write(ip_)
            fp.write("\n")
        with open('google.txt', 'a', encoding='utf-8') as fp:
            fp.write(response.text)


if __name__ == '__main__':
    f = open('ips', 'r')
    line = f.readline()
    ips = []
    while line:
        ips.append(line.strip())
        line = f.readline()
    f.close()

    pool = Pool(10)
    pool.map(check_ip, ips)