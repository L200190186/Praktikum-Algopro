Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Dian Permatasari'
>>> NIM = 'L200190186'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # karena data X harus diubah kedalam bentuk integer
>>> type(b)
<class 'int'>
>>> # karena "Nama" memiliki instruksi len
>>> a / b
74.125
>>> # karena 1186 dibagi 16 hasilnya adalah 74.125
>>> a // b
74
>>> # karena hasil bagi dari 1186 dan 16 jika dibulatkan adalah 74
>>> 10 * (a - 999)
1870
>>> # karena a dikurangi 999 hasilnya adalah 187 kemudian dikali 10 hasilnya 1870
>>> b ** 2
256
>>> # karena b dipangkatkan 2 hasilnya adalah 256
>>> a % b
2
>>> # karena a dibagi b sisanya adalah 2
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # karena 12.5 merupakan angka desimal
>>> a / c
94.88
>>> # karena a dibagi b hasilnya adalah 94.88
>>> a // b
74
>>> a // c
94.0
>>> # karena hasil bagi dari a dan c jika dibulatkan adalah 94.0
>>> a % c
11.0
>>> #karena a dibagi c sisanya adalah 11.0
