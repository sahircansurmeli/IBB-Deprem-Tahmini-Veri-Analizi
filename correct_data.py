import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

top_keys = ["BİNA HASARI", "CAN KAYBI"]

cid_numbers_map = {
    "17": "",
    "19": "0",
    "20": "1",
    "21": "2",
    "22": "3",
    "23": "4",
    "24": "5",
    "25": "6",
    "26": "7",
    "27": "8",
    "28": "9"
}

cid_map = {f"(cid:{k})": cid_numbers_map[k] for k in cid_numbers_map}

for ilce in data:
    for kategori in top_keys:
        for mahalle in data[ilce][kategori]:
            for veri in data[ilce][kategori][mahalle]:
                for cid in cid_map:
                    data[ilce][kategori][mahalle][veri] = data[ilce][kategori][mahalle][veri].replace(cid, cid_map[cid])
                try:
                    data[ilce][kategori][mahalle][veri] = int(data[ilce][kategori][mahalle][veri])
                except ValueError:
                    print("Value Error", ilce)

with open("correct_data.json", "w", encoding="utf-8") as out:
    out.write(json.dumps(data, indent=4, ensure_ascii=False))
