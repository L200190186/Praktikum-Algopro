Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Dian Permatasari'
>>> NIM = 186
>>> Tinggi = 1.55
>>> Berat = 49
>>> Tahunlahir = 2001
>>> Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
>>> Data = [Tahunlahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # karena data "Aku" ditulis didalam tanda kurung
>>> Aku[0]
2001
>>> # karena objek pertama didalam "Aku" adalah "Tahunlahir",yaitu 2001
>>> a = NIM % 4; Aku[a]
1.55
>>> # karena 186 dibagi 4 sisanya adalah 2,jadi hasil dari Aku[2] adalah 1.55
>>> type(Aku[a])
<class 'float'>
>>> # karena nilai dari "Tinggi" adalah 2, 2 adalah data tipe float
>>> Aku[a:4]
(1.55, 186)
>>> # karena data yang diminta dari "Aku" mulai dari ke-2 sampai ke-3 yaitu"Tinggi", "NIM"
>>> type(Aku[4])
<class 'str'>
>>> # karena data ke-4 dari "Aku" adalah "Nama",nilai dari data "Nama" adalah "Dian Permatasari"
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # karena data tuple tidak dapat diganti
>>> type(Data)
<class 'list'>
>>> # karena data "Data" ditulis dengan tanda kurung siku
>>> type(Data[4])
<class 'str'>
>>> # karena nilai dari "Nama" adalah "Dian Permatasari" adalah data tipe string
>>> Data[4][5]
'P'
>>> # karena data dari "Nama" adalah "Dian Permatasari" yang indeks ke-5 adalah 'P'
>>> Data[4][a:6]
'an P'
>>> # karena data dari "Nama" adalah "Dian Permatasari",lalu indeks yang diminta dari 2 sampai 6,nilainya adalah 'an P'
>>> Data[0] = 'ok'; Data
['ok', 49, 1.55, 186, 'Dian Permatasari']
>>> # karena data "Tahublahir" diubah menjadi 'ok' dan menampilkan "Data"
>>> Data[-a]
186
>>> # karena yang diminta data "NIM" yaitu 186
>>> range(a)
range(0, 2)
>>> # karena "range(2)" adalah range 0 sampai 2
