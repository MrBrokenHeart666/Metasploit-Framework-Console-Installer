import os
print("=====================??=====================")
os.system("figlet Metasploit")
print("=====================??=====================")
print("[ Metasploit Framework Console Installer ]")
print("=====================??=====================")
print("""
1). Install Metasploit Framework Console [ Android 7.0 ]
2). Install Metasploit Framework Console [ Android 5.0 ]
3). About This Tools
4). Quit
""")
print("=====================??=====================")
code = raw_input("Please Choose : ")
if code == "1":
	print("Are You Sure??")
	pilihan = raw_input("[ Y/N ] ")
    	if pilihan == "y":
		print("Youre Going To Install Metasploit Framework Console")
	 	os.system("apt update && apt upgrade && pkg install unstable-repo && pkg install metasploit")
	 	print("Now You Can Run Metasploit Framework Console By Typing msfconsole")
elif code == "2":
	print("Are You Sure??")
	aku = raw_input("[ Y/N ] ")
	if aku == "y":
		print("Youre Going To Install Metasploit Framework Console")
		os.system("apt update && apt upgrade -y && apt install git curl wget nano -y && curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz && gunzip metasploit_5.0.65-1_all.deb.gz && dpkg -i metasploit_5.0.65-1_all.deb && apt install -f && apt --fix-broken install")
		print("Now You Can Run Metasploit Framework Console By Typing msfconsole")
elif code == "3":
	print("This Tools Is Created By MR.BR0K3NH34RT and u0_a117")
	print("""
	What is Metasploit?

	Metasploit is a widely used penetration testing tool that
	makes hacking way easier than it used to be. It has become
	an indispensable tool for both red team and blue team
	""")
	print("""
	Metasploit definition :

	Metasploit is a penetration testing framework that makes hacking simple.
	It's an essential tool for many attackers and defenders.
	Point Metasploit at your target, pick an exploit,
	what payload to drop, and hit Enter.
	It's not quite as simple as that, of course, so let's begin at the beginning.
	Back in ye olden days of yore,
	pentesting involved a lot of repetitive labor that Metasploit now automates.
	Information gathering? Gaining access? Maintaining persistence?
	Evading detection? Metasploit is a hacker's Swiss army chainsaw
	(sorry, Perl!), and if you work in information security,
	you're probably already using it.
	Better still,
	the core Metasploit Framework is both free and libre software and
	comes pre-installed in Kali Linux. (It's BSD-licensed, in case you're curious.
	The framework offers only a command-line interface,
	 but those wanting GUI-based click-and-drag hacking
	 plus some other cool features
	 can drop a bundle for per-seat licenses to Metasploit Pro.
	Let's take a closer look at how Metasploit works, and its history
	""")
	print("""
	History of Metasploit :

	HD Moore began working on Metasploit in the early oughts,
	and released 1.0, written in Perl, in 2003. The project has grown
	dramatically since then, from the original 11 exploits the project
	came with to more than 1,500 now, plus around 500 payloads, with a switch to
	Ruby under the hood along the way.
	Security outfit Rapid7 acquired both Metasploit and Moore in 2009.
	(Moore left the project in 2016.) Metasploit has since become the de facto
	framework for exploit development, despite competition from Canvas and Core
	Impact. Today it is common for zero day reports to include a
	Metasploit module as proof of concept
	""")
	print("""
	How to use Metasploit :

	During the information gathering phase of a pentest, Metasploit integrates
	seamlessly with Nmap, SNMP scanning and Windows patch enumeration, among others. 
	There's even a bridge to Nessus, Tenable's vulnerability scanner.
	Pretty much every reconnaissance tool you can think of integrates with Metasploit,
	making it possible to find the chink in the armor you're looking for.

	Once you've identified a weakness, hunt through Metasploit's
	large and extensible database for the exploit that will crack open that chink
	and get you in. For instance, NSA's EternalBlue exploit, released by the Shadow
	Brokers in 2017, has been packaged for Metasploit and is a reliable go-to when
	dealing with unpatched legacy Windows systems.

	Like fine wine and cheese, pair the exploit with a payload to suit the task at
	hand. Since what most folks are wanting is a shell,
	a suitable payload when attacking Windows systems is the ever-popular
	Meterpreter, an in-memory-only interactive shell.
	Linux boxes get their own shellcode, depending on the exploit used.
	Once on a target machine, Metasploit's quiver contains a full
	suite of post-exploitation tools, including privilege escalation,
	pass the hash, packet sniffing, screen capture, keyloggers,
	and pivoting tools. You can also set up a persistent backdoor
	in case the machine in question gets rebooted.

	More and more features are being added to Metasploit every year,
	include a fuzzer to identify potential security flaws in binaries,
	as well as a long list of auxiliary modules too long to list here.

	This is only a high-level view of what Metasploit can do.
	The framework is modular and easily extensible and enjoys an active community.
	If it doesn't do exactly what you want it to do, you can almost certainly
	tweak it to suit.
	""")
else:
	print("Bye Dude!!:)")
	print("Thanx For Using My Tools")
	print("")


