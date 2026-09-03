REM Verify Snort installation
bin\snort.exe -V
 
REM List available network interfaces
bin\snort.exe -W
 
REM Run Snort in basic sniffer mode
bin\snort.exe -v -i 5
 
REM Display packet header and payload
bin\snort.exe -vd -i 5
 
REM Display packet in hexadecimal and ASCII
bin\snort.exe -X -i 5
 
REM Packet logging mode
mkdir log
bin\snort.exe -dev -l log -i 5
 
REM Custom rule to detect ICMP ping (rules\local.rules)
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)
 
REM Start Snort IDS using the custom rule
bin\snort.exe -A console -q -i 5 -R rules\local.rules
 
REM Generate test ICMP traffic (from a second Command Prompt)
ping 8.8.8.8
