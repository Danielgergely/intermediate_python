Get-childItem venv -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force
python -m venv venv
venv\scripts\activate
python -m pip install --upgrade pip setuptools