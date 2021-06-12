from morsepy import Morsepy
from gtts import gTTS
import pybase64,os,time,base64
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def txt_morse():
    morse = Morsepy.encrypt(input("inserisci il testo da tradurre in morse  "))
    print(morse)
    x = input('vuoi ascoltare il morse? (y/n)  ')
    if x == 'y':
        Morsepy.beep(morse)
        menu()
    else:
        menu()
    input('invio per tornare al menù   ')
    menu()
def morse_txt():
    txt = input("inserisci il morse da tradurre in testo  ")
    morse = Morsepy.decrypt(txt)
    print(morse)
    x = input('vuoi sentire il testo parlato? y/n  ')
    if x == 'y':
        tts = gTTS(morse)
        tts.save('audio.mp3')
        #sistema
        dir = os.getcwd()
        os.popen("audio.mp3")
        time.sleep(5)
        os.popen('del audio.mp3')
    sel = input("vuoi criptare il testo tradotto? (y/n))   ")
    if sel == 'y':
        criptato = base64.b64encode(morse.encode('utf-8'))
        criciao = list(str(criptato))
        del criciao[0]
        del criciao[0]
        del criciao[-1]
        for idx, s in enumerate(criciao):
            pp = "%s" % (s)
            print(pp,end='')
        menu()
    ok = input('vuoi salvare un file con il testo tradotto? (y/n)   ')
    if ok == 'y':
        filename = input('inserisci il percorso di un file di testo (.txt)  ')
        file = open(filename, 'w')
        file.write(morse)
        file.close()
    else:
        menu()
def crp_dec_txt():  
    x = input('vuoi criptare o decriptare un messaggio? (1/2)  ')
    if x == '1':
        criptato = base64.b64encode(input('inserisci il messaggio da criptare' ).encode('utf-8'))
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
    x = input('scegli voce menù: (1/2/3)  ')
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