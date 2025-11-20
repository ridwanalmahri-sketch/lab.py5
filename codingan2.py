import sys

students = {}  # Nim/id (string), value: dict{name, tugas, uts, uas, akhir}

WEIGHTS = {'tugas': 0.30, 'uts': 0.35, 'uas': 0.35}


def hitung_nilai_akhir(tugas, uts, uas):
    return tugas * WEIGHTS['tugas'] + uts * WEIGHTS['uts'] + uas * WEIGHTS['uas']


def tambah_data():
    Nim = input('Masukkan Nim/ID mahasiswa: ').strip()
    if not Nim:
        print('NIM tidak boleh kosong.')
        return
    if Nim in students:
        print('Data dengan NIM ini sudah ada. Gunakan Ubah Data untuk mengedit.')
        return
    nama = input('Masukkan nama mahasiswa: ').strip()
    try:
        tugas = float(input('Nilai Tugas (0-100): '))
        uts = float(input('Nilai UTS (0-100): '))
        uas = float(input('Nilai UAS (0-100): '))
    except ValueError:
        print('Input nilai harus berupa angka.')
        return
    akhir = hitung_nilai_akhir(tugas, uts, uas)
    students[Nim] = {'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas, 'akhir': akhir}
    print(f'Data untuk {nama} (NIM: {Nim}) berhasil ditambahkan. Nilai akhir: {akhir:.2f}')


def ubah_data():
    Nim = input('Masukkan Nim/ID yang ingin diubah: ').strip()
    if Nim not in students:
        print('Data tidak ditemukan.')
        return
    data = students[Nim]
    print(f"Mengubah data {data['nama']} (NIM: {Nim}). Biarkan kosong untuk tidak mengubah field.")
    nama = input(f"Nama [{data['nama']}]: ").strip()
    if nama:
        data['nama'] = nama
    try:
        tugas_in = input(f"Nilai Tugas [{data['tugas']}]: ").strip()
        uts_in = input(f"Nilai UTS [{data['uts']}]: ").strip()
        uas_in = input(f"Nilai UAS [{data['uas']}]: ").strip()
        if tugas_in:
            data['tugas'] = float(tugas_in)
        if uts_in:
            data['uts'] = float(uts_in)
        if uas_in:
            data['uas'] = float(uas_in)
    except ValueError:
        print('Input nilai harus berupa angka. Perubahan dibatalkan.')
        return
    data['akhir'] = hitung_nilai_akhir(data['tugas'], data['uts'], data['uas'])
    print(f'Data NPM {Nim} berhasil diperbarui. Nilai akhir sekarang: {data["akhir"]:.2f}')


def hapus_data():
    Nim = input('Masukkan NPM/ID yang ingin dihapus: ').strip()
    if Nim in students:
        confirm = input(f"Yakin ingin menghapus data {students[Nim]['nama']} (NPM: {Nim})? (y/n): ").lower()
        if confirm == 'y':
            del students[Nim]
            print('Data berhasil dihapus.')
        else:
            print('Penghapusan dibatalkan.')
    else:
        print('Data tidak ditemukan.')


def tampilkan_data():
    if not students:
        print('Belum ada data mahasiswa.')
        return
    print('\nDaftar Nilai Mahasiswa:')
    print('-' * 84)
    print(f"{'No':<4} {'NPM':<12} {'Nama':<25} {'Tugas':>6} {'UTS':>6} {'UAS':>6} {'Akhir':>8}")
    print('-' * 84)
    for idx, (npm, d) in enumerate(students.items(), start=1):
        print(f"{idx:<4} {npm:<12} {d['nama']:<25} {d['tugas']:6.1f} {d['uts']:6.1f} {d['uas']:6.1f} {d['akhir']:8.2f}")
    print('-' * 84)


def cari_data():
    k = input('Cari berdasarkan (1) NPM atau (2) Nama? (1/2): ').strip()
    if k == '1':
        npm = input('Masukkan NPM: ').strip()
        d = students.get(npm)
        if d:
            print(f"Ditemukan: NPM: {npm}, Nama: {d['nama']}, Tugas: {d['tugas']}, UTS: {d['uts']}, UAS: {d['uas']}, Akhir: {d['akhir']:.2f}")
        else:
            print('Data tidak ditemukan.')
    elif k == '2':
        nama = input('Masukkan nama (atau bagian nama): ').strip().lower()
        hasil = []
        for npm, d in students.items():
            if nama in d['nama'].lower():
                hasil.append((npm, d))
        if hasil:
            print(f'Ditemukan {len(hasil)} hasil:')
            for i, (npm, d) in enumerate(hasil, start=1):
                print(f"{i}. NPM: {npm}, Nama: {d['nama']}, Akhir: {d['akhir']:.2f}")
        else:
            print('Tidak ada data yang cocok.')
    else:
        print('Pilihan tidak valid.')


def menu():
    print('\n=== Aplikasi Daftar Nilai Mahasiswa ===')
    print('1. Tambah Data')
    print('2. Ubah Data')
    print('3. Hapus Data')
    print('4. Tampilkan Data')
    print('5. Cari Data')
    print('6. Keluar')


def main():
    while True:
        menu()
        pilihan = input('Pilih menu (1-6): ').strip()
        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            ubah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            tampilkan_data()
        elif pilihan == '5':
            cari_data()
        elif pilihan == '6':
            print('Keluar. Sampai jumpa!')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih 1-6.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram dihentikan.')
