import os, platform, time, sys
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from ANSHA import anshu
    anshu()
