# Linux Networking Basics

## ping
**Command:**
```bash
ping google.com
ping -c 4 8.8.8.8
ping 192.168.1.1
```
**Purpose:**
Checks if you can reach another computer or website. Like saying "hello" to see if someone is there.

---

## ifconfig
**Command:**
```bash
ifconfig
ifconfig eth0
ifconfig -a
```
**Purpose:**
Shows your network card information - like your computer's address on the network.

---

## ip addr
**Command:**
```bash
ip addr
ip addr show
ip a
```
**Purpose:**
Modern way to see your network settings. Shows your IP address and network details.

---

## ip link
**Command:**
```bash
ip link
ip link show
ip link set eth0 up
ip link set eth0 down
```
**Purpose:**
Shows or controls your network connections. Can turn them on or off.

---

## netstat
**Command:**
```bash
netstat
netstat -tuln
netstat -r
netstat -i
```
**Purpose:**
Shows all network connections on your computer - what's connected and what's listening.

---

## ss
**Command:**
```bash
ss
ss -tuln
ss -ta
```
**Purpose:**
Faster, modern version of netstat. Shows who's talking to your computer.

---

## curl
**Command:**
```bash
curl google.com
curl -I https://example.com
curl -O https://example.com/file.zip
```
**Purpose:**
Fetches data from the internet. Like a web browser but in the terminal.

---

## wget
**Command:**
```bash
wget https://example.com/file.zip
wget -c https://example.com/bigfile.iso
```
**Purpose:**
Downloads files from the internet. Can resume interrupted downloads.

---

## hostname
**Command:**
```bash
hostname
hostname -I
hostname -f
```
**Purpose:**
Shows your computer's name on the network and its IP address.

---

## nslookup
**Command:**
```bash
nslookup google.com
nslookup 8.8.8.8
```
**Purpose:**
Looks up the IP address of a website, or finds what website an IP belongs to.

---

## dig
**Command:**
```bash
dig google.com
dig google.com +short
dig -x 8.8.8.8
```
**Purpose:**
Advanced DNS lookup - finds detailed information about websites and their servers.

---

## traceroute
**Command:**
```bash
traceroute google.com
traceroute -n 8.8.8.8
```
**Purpose:**
Shows the path your data takes to reach a website. Like GPS for internet traffic.

---

## route
**Command:**
```bash
route
route -n
ip route
ip route show
```
**Purpose:**
Shows how your computer sends data to different networks. Like a roadmap for internet traffic.

---

## arp
**Command:**
```bash
arp
arp -a
arp -n
```
**Purpose:**
Shows which IP addresses match to which physical devices on your local network.

---

## tcpdump
**Command:**
```bash
tcpdump
tcpdump -i eth0
tcpdump host 192.168.1.1
```
**Purpose:**
Captures and shows all network traffic. Like recording phone calls to see what's being said.

---

## nc (netcat)
**Command:**
```bash
nc -zv google.com 80
nc -l 1234
nc 192.168.1.100 1234
```
**Purpose:**
Swiss army knife for networking. Can test connections, transfer files, or chat between computers.

---

## telnet
**Command:**
```bash
telnet google.com 80
telnet 192.168.1.1 22
```
**Purpose:**
Tests if a port is open on another computer. Like knocking on a door to see if it opens.

---

## ssh
**Command:**
```bash
ssh user@192.168.1.100
ssh -p 2222 user@server.com
ssh user@server.com "ls -la"
```
**Purpose:**
Securely connects to another computer remotely. Like remote desktop but in terminal.

---

## scp
**Command:**
```bash
scp file.txt user@192.168.1.100:/home/user/
scp user@192.168.1.100:/home/user/file.txt .
scp -r folder/ user@server.com:/backup/
```
**Purpose:**
Securely copies files between computers over the network.

---

## rsync
**Command:**
```bash
rsync -avz folder/ user@server:/backup/
rsync -avz --progress file.zip server:/downloads/
```
**Purpose:**
Smartly syncs files between computers. Only copies what changed - saves time and bandwidth.

---

## firewall-cmd
**Command:**
```bash
firewall-cmd --state
firewall-cmd --list-all
firewall-cmd --add-port=8080/tcp
```
**Purpose:**
Manages your firewall - controls what can enter or leave your computer.

---

## ufw
**Command:**
```bash
ufw status
ufw enable
ufw allow 22
ufw deny 80
```
**Purpose:**
Simple firewall control. Allows or blocks connections to your computer.

---

## iptables
**Command:**
```bash
iptables -L
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -F
```
**Purpose:**
Advanced firewall rules. More powerful but more complex than ufw.

---

## nmcli
**Command:**
```bash
nmcli
nmcli device status
nmcli connection show
nmcli device wifi list
```
**Purpose:**
Manages network connections from command line. Can connect to WiFi, check status, etc.

---

## iwconfig
**Command:**
```bash
iwconfig
iwconfig wlan0
```
**Purpose:**
Shows wireless network card settings - signal strength, connected network, etc.

---

## ethtool
**Command:**
```bash
ethtool eth0
ethtool -i eth0
```
**Purpose:**
Shows detailed information about your network card - speed, driver, capabilities.

---

## mtr
**Command:**
```bash
mtr google.com
mtr -n 8.8.8.8
```
**Purpose:**
Combines ping and traceroute. Shows live network path and quality to a destination.

---

## whois
**Command:**
```bash
whois google.com
whois 8.8.8.8
```
**Purpose:**
Looks up who owns a domain name or IP address. Like a phone book for the internet.

---

## Understanding IP Addresses

**What is an IP Address?**
Like a home address, but for computers. Every device needs one to communicate.

**Types:**
```
192.168.1.100  = Private IP (only in your home/office network)
8.8.8.8        = Public IP (visible to the whole internet)
127.0.0.1      = Localhost (your own computer)
```

**Common Private IP Ranges:**
```
192.168.0.0 - 192.168.255.255  (Home routers love this)
10.0.0.0 - 10.255.255.255      (Big companies use this)
172.16.0.0 - 172.31.255.255    (Medium networks)
```

---

## Understanding Ports

**What is a Port?**
Like apartment numbers in a building. The IP is the building address, the port is the specific door.

**Common Ports:**
```
22   = SSH (secure remote login)
80   = HTTP (websites)
443  = HTTPS (secure websites)
21   = FTP (file transfer)
25   = SMTP (sending email)
3306 = MySQL (database)
8080 = Alternative web server
```

---

## Understanding DNS

**What is DNS?**
Like a phone book - converts website names (google.com) to IP addresses (142.250.185.46).

**Common DNS Servers:**
```
8.8.8.8       = Google DNS
1.1.1.1       = Cloudflare DNS
8.8.4.4       = Google DNS (backup)
```

---

## Network Testing Quick Guide

**Check if you're online:**
```bash
ping 8.8.8.8
```

**Check if a website is up:**
```bash
ping google.com
```

**See your IP address:**
```bash
ip addr show
# or
hostname -I
```

**Check who's connected to your computer:**
```bash
ss -tuln
```

**Download a file:**
```bash
wget https://example.com/file.zip
```

**Test if a port is open:**
```bash
telnet example.com 80
# or
nc -zv example.com 80
```

**Trace route to website:**
```bash
traceroute google.com
```

---

## Common Networking Tasks

**Connect to WiFi:**
```bash
nmcli device wifi list
nmcli device wifi connect "NetworkName" password "YourPassword"
```

**Check network speed:**
```bash
ethtool eth0 | grep Speed
```

**Find your router IP:**
```bash
ip route | grep default
```

**See all devices on your network:**
```bash
arp -a
```

**Check internet speed (after installing speedtest-cli):**
```bash
speedtest-cli
```

---

## Troubleshooting Tips

**Can't connect to internet?**
1. Check cable/WiFi: `ip link`
2. Check IP address: `ip addr`
3. Ping router: `ping 192.168.1.1`
4. Ping internet: `ping 8.8.8.8`
5. Check DNS: `nslookup google.com`

**Slow internet?**
1. Check latency: `ping -c 10 google.com`
2. Trace route: `mtr google.com`
3. Check bandwidth: `speedtest-cli`

**Can't access a website?**
1. Ping it: `ping website.com`
2. Check DNS: `nslookup website.com`
3. Try IP directly: `curl http://IP-ADDRESS`

---

## Security Tips

**Always use SSH instead of Telnet** (SSH is encrypted, Telnet is not)

**Check open ports regularly:**
```bash
ss -tuln
netstat -tuln
```

**Enable firewall:**
```bash
ufw enable
ufw allow 22  # Allow SSH
```

**Monitor network traffic:**
```bash
tcpdump -i any port 80
```

---

## Quick Reference

**See network info:** `ip addr` or `ifconfig`

**Test connectivity:** `ping google.com`

**Download files:** `wget URL` or `curl -O URL`

**Remote login:** `ssh user@server`

**Copy files:** `scp file user@server:/path/`

**Check ports:** `ss -tuln` or `netstat -tuln`

**DNS lookup:** `nslookup domain.com` or `dig domain.com`

**Trace route:** `traceroute google.com` or `mtr google.com`