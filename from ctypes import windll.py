from ctypes import windll
import string
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    print(bitmask)
    # for letter in string.uppercase:
    #     if bitmask & 1:
    #         drives.append(letter)
    #     bitmask >>= 1

    # return drives

if __name__ == '__main__':
    print(get_drives() )