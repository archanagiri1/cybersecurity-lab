# Linux File Permissions

## chmod
**Command:**
```bash
chmod 755 file.txt
chmod 644 file.txt
chmod +x script.sh
chmod -x script.sh
```
**Purpose:**
Changes file permissions using numeric or symbolic notation.

---

## chmod (Numeric)
**Command:**
```bash
chmod 777 file.txt
chmod 755 folder/
chmod 644 document.txt
chmod 600 private.txt
```
**Purpose:**
Sets permissions using numbers: 7=rwx, 6=rw-, 5=r-x, 4=r--, 0=---

---

## chmod (Symbolic)
**Command:**
```bash
chmod u+x file.sh
chmod g-w file.txt
chmod o+r file.txt
chmod a+x script.sh
```
**Purpose:**
Sets permissions using symbols: u=user, g=group, o=others, a=all

---

## chmod (Recursive)
**Command:**
```bash
chmod -R 755 folder/
chmod -R u+x directory/
```
**Purpose:**
Changes permissions recursively for all files and subdirectories.

---

## chown
**Command:**
```bash
chown user file.txt
chown user:group file.txt
chown -R user:group folder/
```
**Purpose:**
Changes file owner and group.

---

## chgrp
**Command:**
```bash
chgrp groupname file.txt
chgrp -R groupname folder/
```
**Purpose:**
Changes the group ownership of a file or directory.

---

## ls -l
**Command:**
```bash
ls -l
ls -la
```
**Purpose:**
Displays file permissions, owner, group, size, and modification date.

---

## umask
**Command:**
```bash
umask
umask 022
umask 077
```
**Purpose:**
Sets default permissions for newly created files and directories.

---

## stat
**Command:**
```bash
stat file.txt
stat -c '%a' file.txt
```
**Purpose:**
Displays detailed file information including permissions.

---

## getfacl
**Command:**
```bash
getfacl file.txt
getfacl folder/
```
**Purpose:**
Displays Access Control Lists (ACL) for a file or directory.

---

## setfacl
**Command:**
```bash
setfacl -m u:username:rwx file.txt
setfacl -x u:username file.txt
setfacl -b file.txt
```
**Purpose:**
Sets or modifies Access Control Lists (ACL).

---

## Permission Numbers

**Numeric Permission Values:**
```
7 = rwx (read, write, execute)
6 = rw- (read, write)
5 = r-x (read, execute)
4 = r-- (read only)
3 = -wx (write, execute)
2 = -w- (write only)
1 = --x (execute only)
0 = --- (no permissions)
```

**Common Permission Combinations:**
```
755 = rwxr-xr-x (owner: full, group/others: read+execute)
644 = rw-r--r-- (owner: read+write, group/others: read only)
777 = rwxrwxrwx (everyone: full permissions)
700 = rwx------ (owner: full, group/others: none)
600 = rw------- (owner: read+write, group/others: none)
```

---

## Symbolic Notation

**Users:**
```
u = user (owner)
g = group
o = others
a = all (user, group, and others)
```

**Operators:**
```
+ = add permission
- = remove permission
= = set exact permission
```

**Permissions:**
```
r = read (4)
w = write (2)
x = execute (1)
```

---

## Special Permissions

**SUID (Set User ID):**
```bash
chmod u+s file
chmod 4755 file
```
**Purpose:**
File executes with the permissions of the file owner.

---

**SGID (Set Group ID):**
```bash
chmod g+s file
chmod 2755 file
```
**Purpose:**
File executes with the permissions of the group owner.

---

**Sticky Bit:**
```bash
chmod +t directory
chmod 1755 directory
```
**Purpose:**
Only the owner can delete files in the directory (common for /tmp).

---

## Examples

**Make a script executable:**
```bash
chmod +x script.sh
chmod 755 script.sh
```

**Secure a private file:**
```bash
chmod 600 private_key.txt
```

**Set folder permissions:**
```bash
chmod 755 public_folder/
chmod 700 private_folder/
```

**Change owner:**
```bash
chown john:developers project.txt
```

**Recursive ownership change:**
```bash
chown -R www-data:www-data /var/www/html/
```

---

## File Types in ls -l

**First character indicates file type:**
```
- = regular file
d = directory
l = symbolic link
c = character device
b = block device
p = named pipe
s = socket
```

**Example output:**
```
-rw-r--r--  1 user group 1234 Jan 30 10:00 file.txt
drwxr-xr-x  2 user group 4096 Jan 30 09:00 folder/
lrwxrwxrwx  1 user group   10 Jan 30 08:00 link -> file.txt
```
