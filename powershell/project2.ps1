$server = New-Object System.Net.HttpListener
$server.Prefixes.Add("http://localhost:8080/")

$Context = $listener.GetContext()

$URL = $Context.Request.Url.LocalPath
$Content = Get-Content -Encoding Byte -Path "MyPowerShellSite:$URL"
$Context.Response.ContentType = [System.Web.MimeMapping]::GetMimeMapping("MyPowerShellSite:$URL")
$Context.Response.OutputStream.Write($Content, 0, $Content.Length)
$Context.Response.Close()

$server.Start()
