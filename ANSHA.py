import os, platform, time, sys
os.system('git pull')
print('\033[1;32m Tools Is On Updating Please wait...\033[0;m')
exit()
bit = platform.architecture()[0]
if bit == '64bit':
    from ANSHA import anshu
    anshu()
