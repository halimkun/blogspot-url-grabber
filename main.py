from colorama import init, Fore, Back, Style
import feedparser as feed
import validators

'''
Created with <3 by 
@halimkun https://github.com/halimkun
'''

def gabu(u):
    print(Fore.GREEN + "Getting all urls from blogger...\n")
    fd = feed.parse(u)
    
    for entry in fd.entries:
        print(Fore.WHITE + entry.link)

    print(Fore.GREEN + "\nDone!")
    print(Fore.LIGHTBLUE_EX + "Jumlah : " + str(len(fd.entries)) + "\n")
    # Warning 
    if len(fd.entries) == 0:
        print(Fore.RED + "Perhatian : ")
        print(Fore.RED + "- Url yang anda masukkan tidak mengandung artikel")
        print(Fore.RED + "- Atau url yang anda masukkan salah")
        print(Fore.YELLOW + "Tools ini hanya bekerja untuk blogspot / blogger, bukan untuk wordpress atau yang lainnya \n")


def piu(r) :
    if r.endswith("/"):
        nu = r + "feeds/posts/default"
    else :
        nu = r + "/feeds/posts/default"
    return nu

def ciu(l):
    if not validators.url(l):
        print(Fore.RED+Style.BRIGHT+"Url Tidak Valid ! \n")
        return False
    else :
        return True

print(Fore.YELLOW + Style.BRIGHT + """ Welcome to
╔══╗────────────╔╦╦═╦╗─╔══╗────╔╗╔╗────╔╗
║╔╗╠╗╔═╦═╦═╦═╦╦╗║║║╬║║─║╔═╬╦╦═╗║╚╣╚╦═╦╦╣║
║╔╗║╚╣╬║╬║╬║╩╣╔╝║║║╗╣╚╗║╚╗║╔╣╬╚╣╬║╬║╩╣╔╣║
╚══╩═╩═╬╗╠╗╠═╩╝─╚═╩╩╩═╝╚══╩╝╚══╩═╩═╩═╩╝╠╣
───────╚═╩═╝───────────────────────────╚╝ code by: @halimkun""")
print(Fore.YELLOW + Style.NORMAL + "Cara Penggunaan --------------------")
print(Fore.GREEN + Style.BRIGHT + " ✓ https://www.haliminfo.com/") 
print(Fore.GREEN + " ✓ http://www.haliminfo.com")

q = str(input(Fore.YELLOW + Style.BRIGHT + "\nMasukkan URL Blogger : "))

if ciu(q):
    gabu(piu(q))
