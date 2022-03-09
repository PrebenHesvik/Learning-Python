Set-PoshPrompt -Theme paradox
Enable-PoshTooltips

$env:POSH_SESSION_DEFAULT_USER = [System.Environment]::UserName


# menu complete using TAB instead of CTRL+SPACE
Set-PSReadlineKeyHandler -Chord Tab -Function MenuComplete
# up&down arrow for history search
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward

# paths
#$projects = 'C:\Users\Preben\Documents\Programming\03-projects'
#$learning = 'C:\Users\Preben\Documents\Programming\04-learning'

Import-Module posh-git
# Chocolatey profile
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"