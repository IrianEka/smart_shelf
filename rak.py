import json
import smbus2
import time
from RPLCD.i2c import CharLCD

# Inisialisasi I2C Bus
bus = smbus2.SMBus(1)  # Ganti angka 1 dengan 0 jika menggunakan Raspberry Pi model lama

# Baca data dari file JSON
def read_json_data(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

# Tampilkan data di LCD I2C
def display_data_on_lcd(lcd, data):
    line1 = data['line1']
    line2 = data['line2'] 
    if line1 is not None and line2 is not None:
        lcd.clear()
        lcd.write_string(line1)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(line2)

if __name__ == "__main__":
    # Ganti dengan jalur lengkap ke file JSON Anda yang sesuai dengan struktur yang baru
    json_file_path = "/home/jayamahe/libre/lcd_info.json"

    # Inisialisasi LCD I2C dengan alamat yang sesuai dari JSON
    lcd_info = read_json_data(json_file_path)
    
    lcds = {}
    for lcd_data_group in lcd_info['lcds']:
        address = int(lcd_data_group['address'], 16)
        lcd = CharLCD(i2c_expander='PCF8574', address=address, port=1, cols=16, rows=2)
        lcds[address] = lcd

    try:
        while True:
            for lcd_data_group in lcd_info['lcds']:
                address = int(lcd_data_group['address'], 16)
                lcd = lcds[address]
                for lcd_data in lcd_data_group['data']:
                    display_data_on_lcd(lcd, lcd_data)
                    time.sleep(2)  # Tunggu 2 detik sebelum berpindah ke data berikutnya
            
    except KeyboardInterrupt:
        for lcd in lcds.values():
            lcd.clear()
            lcd.close()
        print("LCD display stopped.")
