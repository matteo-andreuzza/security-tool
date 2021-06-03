from io import TextIOWrapper
from morsepy import Morsepy
import pybase64
from gtts import gTTS
import os
import time
import base64
import pyperclip
def txt_morse():
    txt = input("inserisci il testo da tradurre in morse")
    mors = Morsepy.encrypt(txt)
    print(mors)
    input('invio per tornare al menù')
    menu()
def morse_txt():
    txt = input("inserisci il morse da tradurre in testo")
    print(Morsepy.decrypt(txt))
    x = input('vuoi sentire il testo parlato? y/n')
    if x == 'y':
        tts = gTTS(Morsepy.decrypt(txt))
        tts.save('audio.mp3')
        #sistema
        dir = os.getcwd()
        os.popen("audio.mp3")
        time.sleep(5)
        os.popen('del audio.mp3')
    sel = input("vuoi criptare il testo tradotto? (y/n))")
    if sel == 'y':
        criptato = base64.b64encode(Morsepy.decrypt(txt).encode('utf-8'))
        criciao = list(str(criptato))
        del criciao[0]
        del criciao[0]
        del criciao[-1]
        for idx, s in enumerate(criciao):
            pp = "%s" % (s)
            print(pp,end='')
        menu()
    else:
        menu()
def crp_dec_txt():
    x = input('vuoi criptare o decriptare un messaggio? (1/2)')
    if x == '1':
        criptato = base64.b64encode(input('inserisci il messaggio da criptare').encode('utf-8'))
        criciao = list(str(criptato))
        del criciao[0]
        del criciao[0]
        del criciao[-1]
        for idx, s in enumerate(criciao):
            pp = "%s" % (s)
            print(pp,end='')
        menu()
    elif x == '2':
        try:
            deco = base64.decodebytes(input("inserisci il messaggio da decriptare:..  ").encode('utf-8'))
            decodificato = list(str(deco))
            del decodificato[0]
            del decodificato[0]
            del decodificato[-1]
            for idx, s in enumerate(decodificato):
                pp = "%s" % (s)
                print(pp,end='')
            menu()
        except:
            print("errore, riprova")
    else:
        print('non valido, ritorno al menù')
        menu()
def menu():
    print('1 da testo a morse')
    print('2 da morse a testo')
    print('3 cripta e decripta testo')
    x = input('scegli voce menù: (1/2/3)')
    if x == '1':
        txt_morse()
    elif x == '2':
        morse_txt()
    elif x == '3':
        crp_dec_txt()
    else:
        print('invalid')
        menu()    
menu()