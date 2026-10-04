#Duel RPG Sederhana - Kelompok 31
WATERMARK = "DUEL RPG | KELOMPOK 31 "


class Karakter:
    def __init__(self, nama, hp, serangan, skill):
        self.nama = nama
        self.hp = hp
        self.hp_maks = hp
        self.serangan = serangan
        self.skill = skill  # array 2D: [nama_skill, bonus_damage]

    # method return, tanpa parameter
    def masih_hidup(self):
        return self.hp > 0

    # method return, berparameter
    def hitung_damage(self, indeks):
        return self.serangan + self.skill[indeks][1]

    # method non-return, berparameter
    def terima_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    # method non-return, tanpa parameter
    def tampilkan_status(self):
        bar = "#" * (self.hp // 10)
        print(f"{self.nama:<9} HP {self.hp:>3}/{self.hp_maks} [{bar}]")


# function non-return, tanpa parameter
def tampilkan_banner():
    print(WATERMARK)
    print("Dua petarung saling serang hingga salah satu kalah\n")


# function return, tanpa parameter
def ambil_batas_ronde():
    return 10


# function return, berparameter
def pilih_skill(ronde):
    if ronde % 3 == 0:
        return 2
    elif ronde % 2 == 0:
        return 1
    else:
        return 0


# function return, berparameter
def tentukan_pemenang(a, b):
    if a.hp > b.hp:
        return a.nama
    elif b.hp > a.hp:
        return b.nama
    else:
        return "Seri"


# function non-return, berparameter (berisi nested loop)
def tampilkan_daftar_skill(peserta):
    for p in peserta:
        print(f"Skill {p.nama}:")
        for s in p.skill:
            print(f"  - {s[0]} (+{s[1]} damage)")


# program utama
tampilkan_banner()

ksatria = Karakter("Ksatria", 120, 12,
                   [["Tebasan", 3], ["Tameng Hantam", 8], ["Pedang Cahaya", 18]])
penyihir = Karakter("Penyihir", 100, 10,
                    [["Bola Api", 5], ["Petir", 12], ["Meteor", 25]])
peserta = [ksatria, penyihir]

tampilkan_daftar_skill(peserta)

ronde = 1
batas = ambil_batas_ronde()
while ksatria.masih_hidup() and penyihir.masih_hidup() and ronde <= batas:
    print(f"\nRonde {ronde} ")
    indeks = pilih_skill(ronde)
    for penyerang, lawan in [(ksatria, penyihir), (penyihir, ksatria)]:
        if penyerang.masih_hidup():
            damage = penyerang.hitung_damage(indeks)
            lawan.terima_damage(damage)
            print(f"{penyerang.nama} memakai {penyerang.skill[indeks][0]}: {damage} damage")
    for p in peserta:
        p.tampilkan_status()
    ronde += 1

print("\nHASIL AKHIR")
print(f"Pemenang: {tentukan_pemenang(ksatria, penyihir)}")
print(WATERMARK)