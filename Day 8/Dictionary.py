# Membuat dictionary mahasiswa
data_mahasiswa = {
    1: {'nama': 'Ambar', 'usia': 18, 'jurusan': 'Informatika'},
    2: {'nama': 'Sinta', 'usia': 19, 'jurusan': 'Manajemen'},
    3: {'nama': 'Afifa', 'usia': 20, 'jurusan': 'PGSD'}
}

# Menampilkan informasi setiap mahasiswa
for id_mahasiswa, info in data_mahasiswa.items():
    print(f'Mahasiswa ID: {id_mahasiswa}')
    for kunci, nilai in info.items():
        print(f'{kunci.capitalize()}: {nilai}')
    print('---')
