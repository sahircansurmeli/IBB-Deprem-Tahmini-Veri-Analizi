import camelot
import json


def convert_to_object(data, col_names):
    obj = {}

    for r in data:
        sub_obj = {}
        for i in range(1, len(r)):
            sub_obj[col_names[i-1]] = r[i].replace(".", "")
        obj[r[0]] = sub_obj

    return obj


def write_to_json(obj):
    with open("data_append.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(obj, indent=4, ensure_ascii=False))


files = {
    "BEYKOZ": [43, 50],
    "BEYOĞLU": [43, 50],
    "ÇATALCA": [43, 50],
    "ESENYURT": [43, 50],
    "FATİH": [43, 50],
    "PENDİK": [43, 50],
    "SARIYER": [43, 50],
    "ŞİLE": [43, 50],
}

main_object = {}

for f in files:
    filename = f + ".pdf"
    print("Processing", filename)

    page_nums = [str(n) for n in files[f]]

    tables = camelot.read_pdf(f"../Kitapçıklar/{filename}", pages=",".join(page_nums), process_background=True)

    main_object[filename[:-4]] = {
        "BİNA HASARI": convert_to_object(tables[0].data, ["ÇOK AĞIR HASARLI", "AĞIR HASARLI", "ORTA HASARLI", "HAFİF HASARLI"]),
        "CAN KAYBI": convert_to_object(tables[1].data, ["CAN KAYBI SAYISI", "AĞIR YARALI SAYISI", "HASTANEDE TEDAVİ SAYISI", "HAFİF YARALI SAYISI"])
    }

    print("Processing completed", filename)

write_to_json(main_object)
