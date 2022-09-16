function getIP{
    (Get-NetIPAddress).Ipv4address | Select-string "192*"
    }
