# Linux Basic Commands

## ls
**Command:**
```bash
ls
ls -l
ls -a
ls -la
```
**Purpose:**
Lists directory contents. -l shows details, -a shows hidden files.

---

## cd
**Command:**
```bash
cd folder
cd ..
cd ~
cd /
```
**Purpose:**
Changes the current directory.

---

## pwd
**Command:**
```bash
pwd
```
**Purpose:**
Displays the current working directory.

---

## clear
**Command:**
```bash
clear
```
**Purpose:**
Clears the terminal screen.

---

## mkdir
**Command:**
```bash
mkdir test_folder
```
**Purpose:**
Creates a new directory.

---

## rmdir
**Command:**
```bash
rmdir test_folder
```
**Purpose:**
Deletes an empty directory.

---

## touch
**Command:**
```bash
touch file.txt
```
**Purpose:**
Creates an empty file.

---

## cat
**Command:**
```bash
cat file.txt
```
**Purpose:**
Displays the content of a file.

---

## echo
**Command:**
```bash
echo "hello linux"
```
**Purpose:**
Prints text to the terminal.

---

## man
**Command:**
```bash
man ls
```
**Purpose:**
Shows the manual/help for a command.

---

## whoami
**Command:**
```bash
whoami
```
**Purpose:**
Displays the current user.

---

## uname
**Command:**
```bash
uname -a
```
**Purpose:**
Shows system information.

---

## history
**Command:**
```bash
history
```
**Purpose:**
Shows previously used commands.

---

## exit
**Command:**
```bash
exit
```
**Purpose:**
Closes the terminal session.

---

## cp
**Command:**
```bash
cp source.txt destination.txt
cp -r folder1 folder2
```
**Purpose:**
Copies files or directories.

---

## mv
**Command:**
```bash
mv old_name.txt new_name.txt
mv file.txt /path/to/folder/
```
**Purpose:**
Moves or renames files and directories.

---

## rm
**Command:**
```bash
rm file.txt
rm -r folder_name
```
**Purpose:**
Removes files or directories.

---

## grep
**Command:**
```bash
grep "search_term" file.txt
grep -r "term" folder/
```
**Purpose:**
Searches for text patterns in files.

---

## chmod
**Command:**
```bash
chmod 755 file.sh
chmod +x script.sh
```
**Purpose:**
Changes file permissions.

---

## sudo
**Command:**
```bash
sudo command
sudo apt update
```
**Purpose:**
Executes commands with superuser privileges.

---

## df
**Command:**
```bash
df
df -h
```
**Purpose:**
Shows disk space usage.

---

## du
**Command:**
```bash
du -sh folder_name
```
**Purpose:**
Shows directory size.

---

## find
**Command:**
```bash
find . -name "file.txt"
find /path -type f
```
**Purpose:**
Searches for files and directories.

---

## ps
**Command:**
```bash
ps
ps aux
```
**Purpose:**
Shows running processes.

---

## kill
**Command:**
```bash
kill PID
kill -9 PID
```
**Purpose:**
Terminates processes.

---

## tar
**Command:**
```bash
tar -czvf archive.tar.gz folder/
tar -xzvf archive.tar.gz
```
**Purpose:**
Creates or extracts compressed archives.

---

## wget
**Command:**
```bash
wget https://example.com/file.zip
```
**Purpose:**
Downloads files from the internet.

---

## curl
**Command:**
```bash
curl https://example.com
curl -O https://example.com/file.zip
```
**Purpose:**
Transfers data from or to a server.

---

## ping
**Command:**
```bash
ping google.com
ping -c 4 8.8.8.8
```
**Purpose:**
Tests network connectivity.

---

## top
**Command:**
```bash
top
```
**Purpose:**
Displays real-time system processes and resource usage.

---

## htop
**Command:**
```bash
htop
```
**Purpose:**
Interactive process viewer (enhanced version of top).