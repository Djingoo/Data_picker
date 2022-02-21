import json

count_1 = 0
count_2 = 0
table_first_message = []
table_second_message = []

f = open('capture_101_pack.json', encoding="utf8")
data = json.load(f)

index = 0
for paquet in data:
    if "data" in paquet['_source']['layers']:
        for option in paquet['_source']['layers']:
            if option == "data":
                paquet_data = data[index]['_source']['layers']['data']['data.data']
                paquet_data = paquet_data.replace(':', '')
                string_data = bytes.fromhex(paquet_data)
                string_data = string_data.decode("ascii")
                if count_1 > count_2:
                    table_second_message.append([count_2,string_data])
                    count_2 += 1
                elif count_1 == count_2:
                    table_first_message.append([count_1,string_data])
                    count_1 += 1
    index += 1

i = 0
while i < count_1:
    print("[{number}] : {message}".format(number = i, message = table_first_message[i][1]))
    print("[{number}] : {message}".format(number = i, message = table_second_message[i][1]))
    i += 1
