import re

def main(text_r):
    columns = []
    values = []
    # 余計な部分を消す
    text_r = text_r.replace("\n", "")
    text_r = text_r.replace(" ", "")
    text_r = text_r.replace("、", "")

    # 複数表現のあるものを統一
    text_r = text_r.replace("たんぱく", "蛋白")
    text_r = text_r.replace("糖質", "炭水化物")
    text_r = text_r.replace("Na", "ナトリウム")

    print(text_r)

    if "蛋白質" in text_r:
        string_value = re.findall('蛋白質(.*)g', text_r)
        float_value = float(string_value[0].split("g")[0])
        columns.append("protein")
        values.append(float_value)
    if "炭水化物" in text_r:
        string_value = re.findall('炭水化物(.*)g', text_r)
        float_value = float(string_value[0].split("g")[0])
        columns.append("carbonhydrate")
        values.append(float_value)
    if "脂質" in text_r:
        string_value = re.findall('脂質(.*)g', text_r)
        float_value = float(string_value[0].split("g")[0])
        columns.append("lipid")
        values.append(float_value)
    if "ナトリウム" in text_r:
        string_value = re.findall('ナトリウム(.*)mg', text_r)
        float_value = float(string_value[0].split("mg")[0])
        columns.append("sodium")
        values.append(float_value)
    if "カルシウム" in text_r:
        string_value = re.findall('カルシウム(.*)mg', text_r)
        float_value = float(string_value[0].split("mg")[0])
        columns.append("calcium")
        values.append(float_value)
    if "食塩相当量" in text_r:
        string_value = re.findall('食塩相当量(.*)g', text_r)
        float_value = float(string_value[0].split("g")[0])
        columns.append("sodium chloride amount")
        values.append(float_value)

    return columns, values
