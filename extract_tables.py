import pdftotext
import camelot
import os
import json


def get_file_names():
    return [fname for fname in os.listdir() if fname.endswith(".pdf")]


def get_page_numbers(pdf):
    for i in range(len(pdf)):
        if "TABLO LİSTESİ" in pdf[i]:
            page = pdf[i]
            break

    page = [l.strip() for l in page.split("\n")]

    page_nums = [-1, -1]

    for i, p in enumerate(page):
        if "Bina Hasar" in p:
            try:
                page_nums[0] = int(p[-2:])
            except ValueError:
                page_nums[0] = int(page[i + 1][-2:])

        elif "Can Kaybı" in p:
            try:
                page_nums[1] = int(p[-2:])
            except ValueError:
                page_nums[1] = int(page[i + 1][-2:])

    return [str(i) for i in page_nums]


def convert_to_object(data):
    col_names = [c.replace("\n", " ") for c in data[0]]

    obj = {}

    for r in data[1:]:
        sub_obj = {}
        for i in range(1, len(r)):
            sub_obj[col_names[i]] = int(r[i].replace(".", ""))
        obj[r[0]] = sub_obj

    return obj


def write_to_json(obj):
    with open("data.json", "w") as f:
        f.write(json.dumps(obj, indent=4, ensure_ascii=False))


def main():
    files = get_file_names()
    main_object = {}
    for filename in files:
        with open(filename, "rb") as f:
            pdf = pdftotext.PDF(f)

        page_nums = get_page_numbers(pdf)

        tables = camelot.read_pdf(filename, pages=",".join(page_nums), process_background=True)

        main_object[filename[:-4]] = {
            "BİNA HASARI": convert_to_object(tables[0].data),
            "CAN KAYBI": convert_to_object(tables[1].data)
        }

    write_to_json(main_object)
    return main_object


if __name__ == "__main__":
    main_object = main()
