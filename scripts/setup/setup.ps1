#  implicitly git clone https://github.com/FAU-SWARM/scripts.git has already happened

param (
    [Parameter(Mandatory=$true)][string]$python
)

Invoke-Expression "$python -m virtualenv venv"

Invoke-Expression "git clone https://github.com/FAU-SWARM/api.git"
Invoke-Expression "git clone https://github.com/FAU-SWARM/database.git"
Invoke-Expression "git clone https://github.com/FAU-SWARM/iot.git"
Invoke-Expression "git clone https://github.com/FAU-SWARM/scripts.git"  # the implication being that scripts already exists somewhere
Invoke-Expression "git clone https://github.com/FAU-SWARM/website.git"

Invoke-Expression $(Resolve-Path "venv/Scripts/activate.ps1")
Invoke-Expression "pip install -r scripts/requirements-dev.txt"
Invoke-Expression "pip install -e database"
Invoke-Expression "pip install -e api"
Invoke-Expression "pip install -e iot"

Set-Location website
npm install
npm audit fix
Set-Location ../
