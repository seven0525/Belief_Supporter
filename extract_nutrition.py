# -*- coding: UTF-8 -*-
import re

def edit(text_r):
    # 余計な部分を消す
    text_r = text_r.replace("\n", "")
    text_r = text_r.replace(" ", "")
    text_r = text_r.replace("、", "")

    # 複数表現のあるものを統一
    text_r = text_r.replace("たんぱく", "蛋白")
    text_r = text_r.replace("糖質", "炭水化物")
    text_r = text_r.replace("Na", "ナトリウム")

    return text_r


def main(text_r):
    columns = []
    values = []
    # 熱量以降のみを対象とする
    text_n = text_r.split("cal")[1]
    print(text_n)

    if "蛋白質" in text_n:
        string_value = re.findall('蛋白質(.*)g', text_n)
        float_value = float(string_value[0].split("g")[0])
        columns.append("protein(g)")
        values.append(float_value)
    if "炭水化物" in text_n:
        string_value = re.findall('炭水化物(.*)g', text_n)
        float_value = float(string_value[0].split("g")[0])
        columns.append("carbonhydrate(g)")
        values.append(float_value)
    if "脂質" in text_n:
        string_value = re.findall('脂質(.*)g', text_n)
        float_value = float(string_value[0].split("g")[0])
        columns.append("lipid(g)")
        values.append(float_value)
    if "ナトリウム" in text_n:
        string_value = re.findall('ナトリウム(.*)g', text_n)
        string_value = re.search(r'[0-9]+', string_value[0])
        float_value = float(string_value[0].split("g")[0])
        columns.append("sodium(mg)")
        values.append(float_value)
    if "カルシウム" in text_n:
        string_value = re.findall('カルシウム(.*)g', text_n)
        string_value = re.search(r'[0-9]+', string_value[0])
        float_value = float(string_value[0].split("g")[0])
        columns.append("calcium(mg)")
        values.append(float_value)
    if "食塩相当量" in text_n:
        string_value = re.findall('食塩相当量(.*)g', text_n)
        float_value = float(string_value[0].split("g")[0])
        columns.append("sodium chloride amount(g)")
        values.append(float_value)

    return columns, values
