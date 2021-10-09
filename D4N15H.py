#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 infect.xo")

try:
    os.mkdir("/sdcard/infect-tool")
except OSError:
    pass

abm = """

\033[1;97m 8888888b.        d8888 888b    888 8888888 .d8888b.  888    888 
\033[1;97m 888  "Y88b      d88888 8888b   888   888  d88P  Y88b 888    888 
\033[1;97m 888    888     d88P888 88888b  888   888  Y88b.      888    888 
\033[1;97m 888    888    d88P 888 888Y88b 888   888   "Y888b.   8888888888 
\033[1;97m 888    888   d88P  888 888 Y88b888   888      "Y88b. 888    888 
\033[1;97m 888    888  d88P   888 888  Y88888   888        "888 888    888 
\033[1;97m 888  .d88P d8888888888 888   Y8888   888  Y88b  d88P 888    888 
\033[1;97m 8888888P" d88P     888 888    Y888 8888888 "Y8888P"  888    888 
                                                                
                                                                
                                                          
\033[1;97m------------------------------------------------- 
\033[1;97m(~) Author  : Danish Khan
\033[1;97m(~) Github  : https://github.com/MUNNANBHAI/BLACK-STAR
\033[1;97m(~) Fb Ids : https://www.facebook.com/danishchaudhary.007
\033[1;97m-------------------------------------------------
"""

def main():
    os.system("clear")
    print(abm)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(abm)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install infect tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install infect extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    tech_abm = raw_input("\n[!] Select a valid option : ")
    if tech_abm =="1":
        os.system("cd data && python2 data")
    if tech_abm =="2":
        os.system("cd exts && python2 exts")
    if tech_abm =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()
