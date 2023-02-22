# Extract the zip file with a given password in txt file
#  Need a file txt with various common passwords and a zip file compressed with password

from zipfile import ZipFile

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('passqords.txt','r') as f:
            fp=f.readlines()
            print(fp)
            for pw in fp:
                pw=pw.strip()
                try:
                    zf.extractall(pwd=pw.encode())
                    print("correct "+pw)
                    break
                except:
                    pass
                else:          
                    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
