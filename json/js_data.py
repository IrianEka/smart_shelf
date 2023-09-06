import json

# Data JSON yang diberikan
json_data = """
{
    "lcds": [
        {
            "address": "0x25",
            "data": [
                {
                    "line1": "Data 1a",
                    "line2": "Data 1b"
                },
                {
                    "line1": "Data 2a",
                    "line2": "Data 2b"
                }
            ]
        },
        {
            "address": "0x26",
            "data": [
                {
                    "line1": "Data 3a",
                    "line2": "Data 3b"
                },
                {
                    "line1": "Data 4a",
                    "line2": "Data 4b"
                }
            ]
        },
        {
            "address": "0x27",
            "data": [
                {
                    "line1": "Data 5a",
                    "line2": "Data 5b"
                },
                {
                    "line1": "Data 6a",
                    "line2": "Data 6b"
                }
            ]
        }
    ]
}
"""

# Membaca data JSON
data = json.loads(json_data)

# Mengubah nilai "line1" dan "line2" pada alamat tertentu
new_line1 = "New Line 1 Value"
new_line2 = "New Line 2 Value"

# Misalnya, kita ingin mengubah nilai pada alamat "0x25" dan indeks pertama (0)
target_address = "0x25"
target_index = 0

for lcd in data['lcds']:
    if lcd['address'] == target_address:
        if len(lcd['data']) > target_index:
            lcd['data'][target_index]['line1'] = new_line1
            lcd['data'][target_index]['line2'] = new_line2
            break

# Mengonversi data yang telah diubah menjadi JSON
updated_json_data = json.dumps(data, indent=4)

# Menyimpan data JSON yang telah diperbarui ke dalam file
with open("/home/jayamahe/smart_shelf/updated_iot_data.json", "w") as json_file:
    json_file.write(updated_json_data)

print("Nilai line1 dan line2 telah diperbarui dalam JSON.")
