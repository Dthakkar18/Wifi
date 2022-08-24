from cmath import exp
import profile
import subprocess

#getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

#decoding meta data
data = meta_data.decode('utf-8', errors="backslashreplace")

#spliting data up per line
data = data.split('\n')

#list of profiles
profiles = []

for i in data: 
    if 'All User Profile' in i:

        #if found then split
        i = i.split(':')

        #the wifi name at index 1
        i = i[1]

        #formatting the name (first and last character not needed)
        i = i[1:-1]

        profiles.append(i)

print("Name and Passwords")
print("-------------------")
for i in profiles:
    try:
        #using wifi name to get meta data for password
        password_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        

        #decoding data
        passwords = password_data.decode('utf-8', errors="backslashreplace")

        #spliting per line
        passwords = passwords.split('\n')

        for password in passwords:
            if "Key Content" in password:
                #formatting pass 
                password = password.split(':')
                password = password[1][1:-1]
                print(i + ': ' + password)

    except subprocess.CalledProcessError:
        print("Encoding error")