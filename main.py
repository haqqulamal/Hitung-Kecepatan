def hitung_kinematika(kecepatan_awal, percepatan, waktu):
    kecepatan_akhir = kecepatan_awal + percepatan * waktu
    jarak = kecepatan_awal * waktu + 0.5 * percepatan * waktu ** 2
    return kecepatan_akhir, jarak

n = int(input("Masukkan jumlah inputan: "))
results = []

for i in range(n):
    kecepatan_awal = float(input(f"Masukkan kecepatan awal (m/s) untuk inputan ke-{i+1}: "))
    percepatan = float(input(f"Masukkan percepatan (m/s^2) untuk inputan ke-{i+1}: "))
    waktu = float(input(f"Masukkan waktu (s) untuk inputan ke-{i+1}: "))
    kecepatan_akhir, jarak = hitung_kinematika(kecepatan_awal, percepatan, waktu)
    results.append((kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak))

print("\nn\tKecepatan awal\tPercepatan\tWaktu\tKecepatan akhir\tJarak")
for i, result in enumerate(results, start=1):
    kecepatan_awal, percepatan, waktu, kecepatan_akhir, jarak = result
    print(f"{i}\t{kecepatan_awal:.2f}\t\t{percepatan:.2f}\t\t{waktu:.2f}\t{kecepatan_akhir:.2f}\t\t{jarak:.2f}")