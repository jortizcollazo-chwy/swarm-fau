#  Write-Output $PSScriptRoot

$swarm_root = $PWD
$api_root = Resolve-Path "$swarm_root/api"
$database_root = Resolve-Path "$swarm_root/database"
$scripts_root = Resolve-Path "$swarm_root/scripts"
$website_root = Resolve-Path "$swarm_root/website"
$venv_activate = Resolve-Path "$swarm_root/venv/Scripts/activate.ps1"

Write-Output $website_root $api_root $venv_activate


Write-Output dev-api ; Start-Process powershell -ArgumentList "-noexit", "& $venv_activate ; python $(Resolve-Path "$api_root/main.py") --dev --debug"
Write-Output dev-website ; Start-Process powershell -ArgumentList "-noexit", "& $venv_activate ; cd $website_root ; npm run start"
