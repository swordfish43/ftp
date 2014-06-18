from ftplib import FTP

# ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp = FTP()     # connect to host, default port
ftp.connect('192.168.1.240', 8888)
ftp.login(user='swordfish', passwd='password')                     # user anonymous, passwd anonymous@
# ftp.login()                     # user anonymous, passwd anonymous@
# ftp.cwd('debian')               # change into "debian" directory
ftp.retrlines('LIST')           # list directory contents
ftp.quit()