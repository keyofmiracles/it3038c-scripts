mkdir $env:HOMEPATH\ALLPDFS

$items = Get-ChildItem -Recurse -Filter "*.txt*" 

$answer = Read-Host -Prompt "Make copies? Enter 'Yes' or 'No'"

if ($answer -eq 'Yes') {

$items.fullname | ForEach-Object {

Copy-Item -Path $_ -Destination $env:HOMEPATH\ALLPDFS

}

    $ans2 = Read-Host -Prompt "Delete Old files? Enter 'Yes' or 'No'"
    if ($ans2 -eq 'Yes') {

        $items.FullName | ForEach-Object {
            Remove-Item -Path $_ -Force -Recurse
        }
    }


}

if ($answer -eq 'No') {

    Write "OK. Aborting."
}


