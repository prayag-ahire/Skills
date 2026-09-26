Set-Location -Path $PSScriptRoot\..
python build_app.py
python build.py
Write-Output 'Both builds completed successfully.'
