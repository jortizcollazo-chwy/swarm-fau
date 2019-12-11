# $script_root = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
# $swarm_root = Split-Path -Parent -Path $script_root
$swarm_root = $PWD
$api_root = Resolve-Path "$swarm_root/api"
$database_root = Resolve-Path "$swarm_root/database"
$iot_root = Resolve-Path "$swarm_root/iot"
$scripts_root = Resolve-Path "$swarm_root/scripts"
$website_root = Resolve-Path "$swarm_root/website"
$venv_activate = Resolve-Path "$swarm_root/venv/Scripts/activate.ps1"


Set-Location $api_root
Invoke-Expression "git pull"

Set-Location $database_root
Invoke-Expression "git pull"

Set-Location $iot_root
Invoke-Expression "git pull"

Set-Location $scripts_root
Invoke-Expression "git pull"

Set-Location $website_root
Invoke-Expression "git pull"

Set-Location $swarm_root

Invoke-Expression $(Resolve-Path $venv_activate)

Invoke-Expression "pip install -r scripts/requirements-dev.txt"
Invoke-Expression "pip install -e database"
Invoke-Expression "pip install -e api"
Invoke-Expression "pip install -e iot"
Set-Location $website_root
npm install
npm audit fix
Set-Location $swarm_root
