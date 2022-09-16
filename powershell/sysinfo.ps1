$IP = (get-netipaddress).IPAddress[2]
$hostname = hostname
$version = $HOST.Version.Major
$day = Get-Date -Format "dddd, MMMM dd yyy"

$BODY = "This machine's IP is $IP." + " " + "User is $env:USERNAME." + " " + "Hostname is $hostname." + " " + "PowerShell Version $version." + " " + "Today's Date is $day."

$BODY | Out-File C:\it3038c-scripts\Lab3output.txt
