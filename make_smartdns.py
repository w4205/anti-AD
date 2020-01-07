import os
import re

basedir = os.path.abspath(os.path.dirname(__file__))


def trans(data):
    regex = r"^.*?(\/.*?\/)$"
    subst = "address \\1#"
    result = re.sub(regex, subst, data, 0, re.MULTILINE)
    # 取消淘宝相关屏蔽
    regex = r"^.*\.taobao\.com.*\n"
    result = re.sub(regex, '', result, 0, re.MULTILINE)
    return result


def main():
    # 读取 dnsmasq 配置
    with open(basedir + '/adblock-for-dnsmasq.conf', 'r', encoding='utf-8') as f:
        data = f.read()
    # 添加自定义
    with open(basedir + '/special-rule.conf', 'r', encoding='utf-8') as f:
        data += f.read()
    # 转换为 smartdns 格式
    with open(basedir + '/adblock-for-smartdns.conf', 'w', encoding='utf-8') as f:
        f.write(trans(data))


if __name__ == '__main__':
    main()