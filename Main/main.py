from win10toast import ToastNotifier
def notify(title,msg,duration):
    notif = ToastNotifier()
    notif.show_toast(title=title,msg=msg,duration=duration,icon_path="C:\\Users\\ACER\\Downloads\\profile.ico",threaded=True)
title = input("Input your notification title: \n")
msg = input("Input your message: \n")
duration = int(input("Input duration that you want: \n"))
notify(title,msg,duration)
