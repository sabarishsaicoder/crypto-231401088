import subprocess
 
def run(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout.strip()
    except Exception:
        return "Unable to execute command"
 
print("Linux Privilege Escalation Checker")
print("-" * 40)
 
print("\n1. Current User")
print(run("whoami"))
print(run("id"))
 
print("\n2. Sudo Permissions")
sudo = run("sudo -n -l 2>/dev/null")
print(sudo if sudo else "No passwordless sudo permission found.")
 
print("\n3. SUID Files")
suid = run("find /usr/bin /usr/sbin /bin /sbin -perm -4000 -type f 2>/dev/null")
print(suid if suid else "No SUID files found.")
 
print("\n4. World-Writable Files")
writable = run("find /etc /usr /opt -type f -perm -0002 2>/dev/null | head -20")
print(writable if writable else "No world-writable files found.")
 
print("\n5. Sensitive File Permissions")
print(run("ls -l /etc/passwd /etc/shadow 2>/dev/null"))
 
print("\n6. Writable Cron Files")
cron = run("find /etc/cron* -type f -writable 2>/dev/null")
print(cron if cron else "No writable cron files found.")
 
print("\nScan Completed Successfully.")
