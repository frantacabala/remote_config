RCONF 

- automaticky konfiguracni system zalozeny na centralnim serveru, ktery rozesila konfiguraci

- nejprve je nutno vygenerovat konfiguracni soubory pro vsechny dostupne pocitace v siti s prepinacem -g 
	- tyto konfigurace se ukladaji do predem zvolene slozky webovskeho serveru, ktery musi byt nakonfigurovan na centralim serveru, ktery rozesila konfigurace
	- definice pocitace je podle jeho MAC adresy, diky ktere rozpozna, kterou si ma stahnout pomoci wget
- je mozno pouze oskenovat sit pomoci prepinace -s , ktery nam pouze najde klienty v sity a jejich IP a ulozi si je do konfigurace
	- pokud vzniknou nejake komplikace typu - manualni zmena IP adresy na klientskem pocitaci, je nutno zavolat predem prepinac -r, ktery vymaze tabulku s prirazenim MAC-IP.
		- Pokud tak nebude ucineno bude server se pokouset pripojovat na starou IP adresu a konfigurace selze
- configuracni klientsky skript je ulozen do /usr/bin/rconf_client, log je ulozen do /var/log/rconf_client.log
- pokud jsou konfiguracni soubory vygenerovany, je mozne prejit k dalsi casti a to je rozeslani scriptu na vsechny dostupne pocitace
	- toto v podstate provede zarazeni klientskeho pocitace do automatizovane spravy
	- scripty nejsou pouze odeslany na klientske pocitace, avsak jsou i nasledne po zkopirovani spusteny na danem klientovi a ten si spusti uvodni konfiguraci, ktera zahrnuje nakonfigurovani sitoveho rozhrani eth0(IP,MASKA,DNS,GW,HOSTNAME), ale take nastaveni firewallu
- po vygenerovani konfiguracnich souboru a firewallu je mozno provadet zmeny dle libosti a v zavislosti na definovanych promennych, avsak neni zarucena funcnost v pripade zadani nespravnych promennych. 
	- oprava je mozna opet pomoci prepinace -g, ale ztrati se tim cela manualne nastavena konfigurace a je vse obnoveno automaticky



- v programu jsou pouzite externi knihovny, ktere byly naistalovane pomoci interniho balickovaciho systemu apt-get
	-	je zde jeden zdrojovy kod knihovny - scp.py, ktery je vytvoren 3. stranou 
 	
pro spravnou funkcnost je nutno mit naistalovane nasledujich knihovny:
- ./lib/scp.py - pridavny modul do knihovny paramiko, ktery se stara o zabezpecene kopirovani souboru pomoci scp
- # apt-get install python-nmap
- # apt-get install python-paramiko
- # apt-get install python-scapy
- # apt-get install tcpdump
- # apt-get install python-netifaces
