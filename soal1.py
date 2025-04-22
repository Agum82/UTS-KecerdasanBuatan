def identifikasi_hama(daun_menguning, bercak_hitam, daun_berlubang, tanaman_layu):
    if daun_menguning and tanaman_layu:
        return "Kutu Daun"
    elif daun_berlubang and bercak_hitam:
        return "Ulat Grayak"
    elif daun_menguning and bercak_hitam:
        return "Jamur Patogen"
    elif daun_berlubang and tanaman_layu:
        return "Wereng Batang Coklat"
    else:
        return "Hama tidak diketahui"

# Contoh input
gejala = {
    "daun_menguning": True,
    "bercak_hitam": False,
    "daun_berlubang": False,
    "tanaman_layu": True
}

print("Hama terdeteksi:", identifikasi_hama(**gejala))
