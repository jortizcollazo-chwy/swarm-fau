:: implicitly git clone https://github.com/FAU-SWARM/scripts.git has already happened
@ECHO OFF

SET python="notset"

:argparse
IF NOT "%1"=="" (
    IF "%1"=="--python" (
        SET python=%2
        SHIFT
    )
    SHIFT
    GOTO :argparse
)

IF "%python%"=="notset" (
    GOTO :error
) ELSE (
    GOTO :execute
)

:error
echo "Please provide python exe path"
exit 1

:execute
%python% -m virtualenv venv
git clone https://github.com/FAU-SWARM/api.git
git clone https://github.com/FAU-SWARM/database.git
git clone https://github.com/FAU-SWARM/iot.git
git clone https://github.com/FAU-SWARM/scripts.git  :: # the implication being that scripts already exists somewhere
git clone https://github.com/FAU-SWARM/website.git

venv/Scripts/activate
pip install -r scripts/requirements-dev.txt
pip install -e database
pip install -e api
pip install -e iot
cd website
npm install
cd ../