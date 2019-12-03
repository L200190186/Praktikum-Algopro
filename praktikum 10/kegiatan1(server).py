import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "server penjawab otomatis sudah siap"
data = ''
kamus = {'nama': 'Dian Permatasari', 'NIM': 'L200190186', 'angkatan': '2019', 'keluar':'Siap!!'}
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            s.close()
            break
        print 'Perintah:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
