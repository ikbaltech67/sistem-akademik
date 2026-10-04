from collections import deque


class SistemAkademik:

    def __init__(self):
        # 4a. Dynamic Array (List) untuk penyimpanan berurutan
        self.daftar_mahasiswa = []

        # 4b. Stack untuk fitur Undo
        self.stack_undo = []

        # 4c. Queue untuk antrean pemrosesan data
        self.antrean_pengolahan = deque()

        # 4d. Hash Table (Dictionary) untuk pencarian cepat via Key (NIM)
        self.map_mahasiswa = {}

    def tambah_mahasiswa(self, nim: str, nama: str, jurusan: str):
        mahasiswa = {"nim": nim, "nama": nama, "jurusan": jurusan}

        # Penggunaan Array - O(1)
        self.daftar_mahasiswa.append(mahasiswa)

        # Penggunaan Hash Table - O(1)
        self.map_mahasiswa[nim] = mahasiswa

        # Penggunaan Stack untuk riwayat aksi
        self.stack_undo.append({"aksi": "TAMBAH", "data": mahasiswa})

    def tambah_antrean(self, id_transaksi: str, deskripsi: str):
        # Penggunaan Queue (Enqueue) - O(1)
        self.antrean_pengolahan.append(
            {"id": id_transaksi, "deskripsi": deskripsi}
        )

    def proses_antrean(self):
        # Penggunaan Queue (Dequeue) - O(1)
        if self.antrean_pengolahan:
            transaksi = self.antrean_pengolahan.popleft()
            print(
                f"Memproses Transaksi: {transaksi['id']} - {transaksi['deskripsi']}"
            )
            return transaksi
        print("Antrean kosong.")
        return None

    def cari_mahasiswa_by_key(self, nim: str):
        # Penggunaan Hash Table Lookup - O(1)
        return self.map_mahasiswa.get(nim, "Data tidak ditemukan.")

    def undo(self):
        # Penggunaan Stack Pop - O(1)
        if not self.stack_undo:
            print("Tidak ada aksi untuk dibatalkan.")
            return

        aksi_terakhir = self.stack_undo.pop()
        if aksi_terakhir["aksi"] == "TAMBAH":
            mhs = aksi_terakhir["data"]
            self.daftar_mahasiswa.remove(mhs)
            del self.map_mahasiswa[mhs["nim"]]
            print(f"Undo Berhasil: Pendaftaran {mhs['nama']} dibatalkan.")


if __name__ == "__main__":
    sistem = SistemAkademik()

    # 1. Penyimpanan Berurutan & Hash Table
    sistem.tambah_mahasiswa("2024001", "Budi Santoso", "Teknik Informatika")
    sistem.tambah_mahasiswa("2024002", "Siti Aminah", "Sistem Informasi")

    # 2. Pencarian Berdasarkan Key
    print("Hasil Pencarian NIM 2024001:")
    print(sistem.cari_mahasiswa_by_key("2024001"))

    # 3. Antrean Pemrosesan (FIFO)
    sistem.tambah_antrean("TRX01", "Cetak KSM")
    sistem.tambah_antrean("TRX02", "Validasi UKT")
    sistem.proses_antrean()

    # 4. Undo Aksi Terakhir (LIFO)
    sistem.undo()