# Write your code here :-)
import sys

passwordFile = open('SecretPasswordFile.txt')

#    secretPassword = f.read().splitlines()
secretPasswordFile = passwordFile.read()
secretPassword = secretPasswordFile.rstrip('\n')

print('Seccret pass read from the file is:', secretPassword)
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    sys.exit()
if typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')
    sys.exit()
else:
    print('Access denied')
sys.exit()
