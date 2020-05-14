import os



def generate_wordlist(cms,path):
    wordlist=[]
    for root,subfolder,files in os.walk(path):
        for folder in subfolder:
            wordlist.append(folder)
        for file in files:
            wordlist.append(file)

    wordlist=list(set(sorted(wordlist)))
    print "result ready..do u want to save!! Y/N "
    confirm=raw_input(" Y/N ")
    if(confirm.lower()=="y"):
        fh=open(cms+".txt","a")
        for item in wordlist:
            fh.write(item+"\n")
        fh.close()
    else:
        print wordlist



def main():
    #time.sleep(20)
    print '''
                 / ____|  \/  |/ ____| \ \        / /          | | (_)   | |  
 | |    | \  / | (___    \ \  /\  / /__  _ __ __| | |_ ___| |_ 
 | |    | |\/| |\___ \    \ \/  \/ / _ \| '__/ _` | | / __| __|
 | |____| |  | |____) |    \  /\  / (_) | | | (_| | | \__ \ |_ 
  \_____|_|  |_|_____/      \/  \/ \___/|_|  \__,_|_|_|___/\__|
  
            Tools can be used to generate wordlist CMS wise and which can be used in Dirbuster
            '''
    print "Enter the Cms Name \n"
    cms=raw_input()
    print "Enter the path of CMS repo \n"
    path=raw_input()
    generate_wordlist(cms,path)

if __name__ == "__main__":

    main()
