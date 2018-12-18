[int]$date = get-date -Uformat %s #file name - int date
$dateTitle = Get-Date -Format g #date as a header in txt file
$exportlocation = New-Item -type file -path "d:\$date.txt" #export location
while ($true) { #while powershell script open
     Add-content $exportlocation (%{"====={0}=====" -f $dateTitle}) #add line to txt
     $cpu = Get-WmiObject win32_processor | Measure-Object -Property LoadPercentage -Average | Select Average #get avg cpu usage
     $cputxt = Get-WmiObject win32_processor | %{"CPU Usage:{0}%" -f $cpu.Average}
     Add-content $exportlocation $cputxt #add cpu usage to txt
     $ram = Get-WmiObject win32_OperatingSystem |%{"Total Physical Memory: {0}KB`nFree Physical Memory : {1}KB`nTotal Virtual Memory : {2}KB`nFree Virtual Memory  : {3}KB" -f $_.totalvisiblememorysize, $_.freephysicalmemory, $_.totalvirtualmemorysize, $_.freevirtualmemory}
     $ram = Get-WmiObject win32_OperatingSystem
     $ramTotal = %{"Total physical memory: {0} KB " -f $ram.totalvisiblememorysize} 
     $ramFree = %{"Free memory: {0} KB" -f $ram.freephysicalmemory}
     $ramUsage = %{"Memory Usage: {0}%" -f ($ram.freephysicalmemory/$ram.totalvisiblememorysize)}
     Add-content $exportlocation $ramTotal
     Add-content $exportlocation $ramFree
     Add-content $exportlocation $ramUsage
     $processesCPU = Get-Process | Select-Object -Property Name, CPU | Sort-Object -Property CPU -Descending | Select-Object -First 10 #get top 10 processes by CPU usage
     $processesRAM = Get-Process | Select-Object -Property Name, WS | Sort-Object -Property WS -Descending | Select-Object -First 10 #get top 10 processes by RAM usage (WS)
     Add-content $exportlocation ""
     Add-content $exportlocation "TOP 10 CPU Usage:"
     Add-content $exportlocation $processesCPU
     Add-content $exportlocation ""
     Add-content $exportlocation "TOP 10 RAM Usage:"
     Add-content $exportlocation $processesRAM
     Add-content $exportlocation ""
     start-sleep -s 60 #wait timer 
}

