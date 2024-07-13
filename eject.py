import win32api
import win32file
import os
drives = []
while True:
# Returns a list containing letters from removable drives
  drive_list = win32api.GetLogicalDriveStrings()
  drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
  for letter in drive_list:
      if (win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE) and (letter not in drives):
           drives.append(letter)
  def findencrypt():
    try:
      for path in drives:
           print(drives)
           files = os.listdir(path)
           if "encrypted.txt" in files:
              encrypted_text = open(fr"{path}encrypted.txt")
              coded = encrypted_text.readline()
              if coded == "U2FsdGVkX1/zJW+OcOnPiXdV8FJP6pt8SxHWinEp6YN0w6KkD42Tt45U1qXxqlE57W1tKqzhoJiYfcmeJmO9RYxacf2vrXnBjvaDzW4XwI3dTfJAfHKdaooFgcGavOTQSFIF9RKH7gdMjbqz9N/lP3yd97QqcgES4rN63sx8YbuQJtjBldm8cFa6BAPWDYvKkAWp82UeOa3gFZ9liDvjC4vRxpOEPL7wCYUmeKtXgvujK9YAvPKEt2jWws/Yqs2wS4urI3VwbtUMpmI/Eotc/V87xYp7X3ENe5H3ZtCsX017bXsbDjhVzwE4gZ9dLzd2xTo90qxqRkY48b28AfDaAy47qQ5ehL0EvFvi8iFk3qIwICLw6FRS2zqD747DA4GxJ4BNo/RHNzVIh38mh1S/PqsKcHfDQLrpxX2uxVHUQL7wsvHB0ShW1Fi+tcS4jdes9mSg3Kt1qa1Ksk9Rw0kaG5fmp0T5WrQRmNN8WeAyzo6nV0gws9x8OPx50a7VdE6IbLyMToqMs1CVlBxsQM/hLv/A5DpG9ANsmsVPz3peZnUE/JCi033S6EuTFUng9H0kqEyR7AXE1aACg205mOGmtLjuuIeKg2RfOT3le5Xad0EVxWEMGAA6mocY6nHEpsgjPKQBDUoqXBseDoI/oz5U0U0hNUxxGlSNLVdMf0te+dqNP2oDluyJw55AMnSThWkb28fMDpcaZ6ryXWZPm7limoSyKJGdVgbsjzyrEESk4PVXg5rCQl2dn9yvRVNODWwvjrT55fHfM3zzP4OPwfnOcCMULRj0j7ZS1jCjDXQ1HEDRksPiAmw01q8xJobQIkx05TrgimXIJl2J4gRs6SdcqHpSid1iMVC1pWwdTYPWEed2vYHzIRaA4olNGwFiwUB399hwkh19R7xjtL08FGvD90mKbAzuHWpRwmaDg4S+Q1lTpYZje697Ka8NE/rCnRXRFW3elp7saiyS6pRrC4h4wpjAS0AKA+gMEytISYrSr3X3G8qP++GeV0KNsxyccV6ERl0CNafswbnshiJTReuc4kZdDW8kJuOeTNsjghpl56xvCPe9sXjPv/o31C8ppEQMK+Q2oHjQvOayrOc4F8V/c9Y9yfBQ/jhC5XTzsw86BeaBPpiHT/Ue2A668dkNrepm++j8LnC1G5ceZw2s6RLr8Uu4Cnot2l2KbJulUdOLzd1v7nHknkJaUSmsUA7IYgYVH7WZ9HxTLBkQ/VHL6HmKY+NJS5fVXrsUZ//n04WhB9mC914MAUX1MhOWvJb3t7R4VmGJL+CTMq9DyQW6nFlO9B1C40WSQr44g1zavfLz9AjP6gX9jn6K7qURyjKBfndsgAFQbVw3QaW5lhGv50OUeAcImmv8rjtnOa0UnGtScAl2Dh7EHyCqxtiuNYnm7WoSItebhXYs6YrziR9BEMq1DJ/K2/PCPItNC59VhHgPdUQvd9RquhuSCp9UGVfhacn68K0Z+xgpRaWLC7LTm4607wsNbByojOXNn0gy":
                  encrypted_text.close()
                  if len(drives) >= 2:
                     drives.remove(path)
              else:
                 encrypted_text.close()
                 os.system(f'powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""{path}""").InvokeVerb("""Eject""")')
                 drives.remove(path)
           elif "encrypted.txt" not in files:
              os.system(f'powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""{path}""").InvokeVerb("""Eject""")')   
              drives.remove(path)
    except:
        try:
            if len(drives >= 2):
               os.system(f'powershell $driveEject = New-Object -comObject Shell.Application; $driveEject.Namespace(17).ParseName("""{drives[-1]}""").InvokeVerb("""Eject""")')   
        except:
            pass
       
  succesful = findencrypt()

