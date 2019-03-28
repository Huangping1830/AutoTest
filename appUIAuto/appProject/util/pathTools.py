import os
root_path = os.path.dirname(__file__)
apk_path = root_path.replace("\\","/").replace("util","apk/")
apk_name_path = apk_path + os.listdir(apk_path)[0]
conf_path = root_path.replace("\\","/").replace("util","")
resultReport_path = root_path.replace("\\","/").replace("util","resultReport/")
screenShot_path = root_path.replace("\\","/").replace("util","screenShot/")
log_path = root_path.replace("\\","/").replace("util","log/")
