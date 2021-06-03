from morsepy import Morsepy
import pybase64
from gtts import gTTS
import base64
import os
while True:
    def txt_morse():
        print(Morsepy.encrypt(input("inserisci il testo da tradurre in morse")))
    def morse_txt():
        print(Morsepy.decrypt(input("inserisci il morse da tradurre in testo")))
        if input("vuoi criptare il testo tradotto? (y/n))") == 'y':
            criciao = list(str(base64.b64encode(Morsepy.decrypt(input("inserisci il morse da tradurre in testo")).encode('utf-8'))))
            del criciao[0]
            del criciao[0]
            del criciao[-1]
            for idx, s in enumerate(criciao):
                pp = "%s" % (s)
                print(pp,end='')
    def crp_dec_txt():
        if input('vuoi criptare o decriptare un messaggio? (1/2) ') == '1':
            criciao = list(str(base64.b64encode(input('inserisci il messaggio da criptare').encode('utf-8'))))
            del criciao[0]
            del criciao[0]
            del criciao[-1]
            for idx, s in enumerate(criciao):
                pp = "%s" % (s)
                print(pp,end='')
        elif input('vuoi criptare o decriptare un messaggio? (1/2) ') == '2':
            try:
                decodificato = list(str(base64.decodebytes(input("inserisci il messaggio da decriptare:..  ").encode('utf-8'))))
                del decodificato[0]
                del decodificato[0]
                del decodificato[-1]
                for idx, s in enumerate(decodificato):
                    pp = "%s" % (s)
                    print(pp,end='')
            except:
                print("errore, riprova")
    def menu():
        print('1 da testo a morse')
        print('2 da morse a testo')
        print('3 cripta e decripta testo')
        if input('scegli voce menù: (1/2/3)') == '1':
            txt_morse()
        elif input('scegli voce menù: (1/2/3)') == '2':
            morse_txt()
        elif input('scegli voce menù: (1/2/3)') == '3':
            crp_dec_txt()
    menu()