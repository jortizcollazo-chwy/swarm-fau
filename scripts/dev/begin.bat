
echo dev-api && start cmd /k "%~dp0/../../venv/Scripts/activate && python %~dp0/../../api/main.py --dev --debug"
echo dev-website && start cmd /k "%~dp0/../../venv/Scripts/activate && cd %~dp0/../../website && npm run start"
