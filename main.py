"""
Aplikasi Deteksi Gempa Terkini
"""
from gempa_terkini import ekstraksi_data, tampilkan_data

if __name__ == "__main__":
    print("Running deteksi gempa")
    result = ekstraksi_data()
    tampilkan_data(result)


