# for this we need win10toast
# install usig : python -m pip install win10toast
from win10toast import ToastNotifier
import time

# create an object to the class win10toast
toaster = ToastNotifier()

# now we can use method show_toast to show notification
# parameter input: title, message, icon path, duration, threaded
toaster.show_toast("Sample Notification Title", "Text message for Sample Notification",icon_path=None,threaded=True, duration=5)

