#шифровка
s = input()
cipher = input()
if cipher == 'caesar':
    k = int ( input ( ) )
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i]) > 96:
                if (ord(s[i]) - 96 + k) % 26 == 0:
                    s = s[:i] + chr(96 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 96 + k) % 26 + 96) + s[i + 1:]
            else:
                if (ord(s[i]) - 64 + k) % 26 == 0:
                    s = s[:i] + chr(64 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 64 + k) % 26 + 64) + s[i + 1:]
else:
    k = input()
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i]) > 96:
                t = ord(k[i])-96
                if (ord(s[i]) - 96 + t) % 26 == 0:
                    s = s[:i] + chr(96 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 96 + t) % 26 + 96) + s[i + 1:]
            else:
                t = ord(k[i]) - 65
                if (ord(s[i]) - 64 + t) % 26 == 0:
                    s = s[:i] + chr(64 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 64 + t) % 26 + 64) + s[i + 1:]
print(s)




#дешифровка


s = input()
cipher = input()
if cipher == 'caesar':
    k = int(input())
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i]) > 96:
                if (ord(s[i]) - 96 - k) % 26 == 0:
                    s = s[:i] + chr(96 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 96 - k) % 26 + 96) + s[i + 1:]
            else:
                if (ord(s[i]) - 64 - k) % 26 == 0:
                    s = s[:i] + chr(64 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 64 - k) % 26 + 64) + s[i + 1:]
else:
    k = input()
    for i in range(len(s)):
        if s[i].isalpha():
            if ord(s[i]) > 96:
                t = ord(k[i])-96
                if (ord(s[i]) - 96 - t) % 26 == 0:
                    s = s[:i] + chr(96 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 96 - t) % 26 + 96) + s[i + 1:]
            else:
                t = ord(k[i]) - 65
                if (ord(s[i]) - 64 - t) % 26 == 0:
                    s = s[:i] + chr(64 + 26) + s[i + 1:]
                else:
                    s = s[:i] + chr((ord(s[i]) - 64 - t) % 26 + 64) + s[i + 1:]
print(s)
