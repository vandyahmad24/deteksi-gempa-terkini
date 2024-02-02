import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal :01 Februari 2024, 18:36:28 WIB
    Magnitudo: 2.8
    Kedalaman: 10 km
    Lokasi: 10.25 LS - 124.04 BT
    Keterangan: Pusat gempa berada di laut 33 km Tenggara Kabupaten Kupang
    Dampak: Dirasakan (Skala MMI): II Kabupaten Kupang
    """
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        content = requests.get("https://www.bmkg.go.id/", headers=header)
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div',{'class':'gempabumi-home-bg margin-top-13'})
        result = result.findChildren('li')
        i=0
        time = None
        magnitudo = None
        kedalaman=None
        lokasi = None
        keterangan = None
        dampak = None
        for res in result:
            if i==0:
                time=res
            elif i==1:
                magnitudo=res
            elif i==2:
                kedalaman=res
            elif i==3:
                lokasi=res
            elif i==7:
                keterangan=res
            elif i==8:
                dampak=res

            i=i+1


        time = time.text.split(', ')
        # magnitudo = soup.find('span',{'class':'ic magnitude'})
        # kedalaman = soup.find('span', {'class': 'ic kedalaman'})

        hasil = dict()
        hasil['tanggal']=time[0]
        hasil['waktu']=time[1]
        hasil['magnitudo']=magnitudo.text
        hasil['kedalaman']=kedalaman.text
        hasil['lokasi']=lokasi.text
        hasil['keterangan']=keterangan.text
        hasil['dampak']=dampak.text

        return hasil

    return None



def tampilkan_data(result):
    if result is None:
        print("Data tidak ditemukan")
    print(result)
