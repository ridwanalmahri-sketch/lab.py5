
def main():
    # Buat dictionary daftar kontak: Nama -> Nomor
    contacts = {
        'wan': '08123456789',
        'wennn': '08211223344',
        'ridwan': '08999888777'
    }

    print('Awal daftar kontak:')
    for name, number in contacts.items():
        print(f'  {name}: {number}')
    print('\n--- Permintaan operasi ---\n')

    print('1) Tampilkan kontak wan:')
    wan = contacts.get('wan')
    if wan:
        print(f'  wan: {wan}')
    else:
        print('  Kontak wan tidak ditemukan')
    print()

    print('2) Tambah kontak baru wennn (087654544):')
    contacts['wennn'] = '087654544'
    print('  Kontak ditambahkan.')
    print()

    print('3) Ubah kontak ridwan menjadi 088999776:')
    if 'ridwan' in contacts:
        contacts['ridwan'] = '088999776'
        print('  Kontak ridwan diperbarui.')
    else:
        print('  Kontak ridwan tidak ditemukan, tidak ada perubahan.')
    print()

    print('4) Tampilkan semua Nama:')
    for i, name in enumerate(contacts.keys(), start=1):
        print(f'  {i}. {name}')
    print()

    print('5) Tampilkan semua Nomor:')
    for i, number in enumerate(contacts.values(), start=1):
        print(f'  {i}. {number}')
    print()

    print('6) Tampilkan daftar Nama dan Nomornya:')
    for i, (name, number) in enumerate(contacts.items(), start=1):
        print(f'  {i}. {name}: {number}')
    print()

    print('7) Hapus kontak ridwan:')
    removed = contacts.pop('ridwan', None)
    if removed:
        print('  Kontak ridwan telah dihapus.')
    else:
        print('  Kontak ridwan tidak ditemukan (tidak ada yang dihapus).')
    print()

    print('Daftar kontak akhir:')
    for i, (name, number) in enumerate(contacts.items(), start=1):
        print(f'  {i}. {name}: {number}')

if __name__ == '__main__':
    main()
