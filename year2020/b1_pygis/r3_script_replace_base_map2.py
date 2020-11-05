# 解析html替换地图底图.
import re


def replace_base_map():
    pattern = re.compile(r'https(.*?)png')

    cnt = open('xx_picinfo202008.html', encoding="utf-8")
    cn = cnt.read()
    cnt.close()
    result = re.sub(pattern, 'http://t4.tianditu.gov.cn/DataServer?T=vec_w&X={x}&Y={y}&L={z}&tk=8843d1c1f4c8271a8cbdf40ec4cfae9a', cn)
    cnt_new = open('xx_result.html', 'w', encoding="utf-8")
    cnt_new.write(result)


if __name__ == '__main__':
    replace_base_map()
