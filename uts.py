class Document:
    def __init__(self):
        self.__title = "Surat Perintah Sebelas Maret"  # Atribut private untuk judul dokumen

    def __get_secret_info(self):
        return "Ini adalah informasi rahasia tentang dokumen"

    # Getter untuk __title
    def get_title(self):
        return self.__title

    # Setter untuk __title
    def set_title(self, new_title):
        self.__title = new_title

    # Metode publik untuk mengakses __get_secret_info
    def access_secret_info(self):
        return self.__get_secret_info()

    def display_info(self):
        print("Ini adalah informasi dokumen.")
        # Metode publik ini bisa mengakses metode dan data pribadi
        print(self.__get_secret_info())
        print(f"Title: {self.__title}")

class OfficialDocument(Document):
    def __init__(self):
        super().__init__()
        self.__document_number = "111966"  # Atribut private untuk nomor dokumen

    # Getter untuk __document_number
    def get_document_number(self):
        return self.__document_number

    # Setter untuk __document_number
    def set_document_number(self, new_number):
        self.__document_number = new_number

    def demo_official_document(self):
        # Menggunakan getter dari kelas induk
        title = self.get_title()
        print(f"Title dari dokumen resmi: {title}")

        # Mengubah judul dokumen melalui setter kelas induk
        self.set_title("SUPERSEMAR")
        new_title = self.get_title()
        print(f"Judul setelah diubah: {new_title}")

        # Mengakses informasi rahasia dari kelas induk melalui metode publik
        secret_info = self.access_secret_info()
        print(f"Hasil akses informasi rahasia: {secret_info}")

        # Menampilkan nomor dokumen
        print(f"Nomor Dokumen: {self.get_document_number()}")

# Membuat objek dari OfficialDocument dan memanggil demonya
objek_dokumen_resmi = OfficialDocument()
objek_dokumen_resmi.demo_official_document()