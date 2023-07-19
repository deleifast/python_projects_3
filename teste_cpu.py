import wmi, shutil

c = wmi.WMI ()

total, used, free = shutil.disk_usage("/")

cpuArr = c.Win32_Processor()

with open('cpu.txt','w') as arquivo:
	
	for cpu in cpuArr :
		print('cpu:', cpu.loadPercentage, cpu.numberOfCores, cpu.name, cpu.maxClockSpeed/1000, file=arquivo)
	#print('OS is: {0}'.format(c.Win32_OperatingSystem()[0].Caption))
	#print('Disk freespace {0} - total {1}'.format(c.Win32_LogicalDisk()[0].Freespace,c.Win3#2_LogicalDisk()[0].Size))
	print('Total Memória: {0}'.format(c.Win32_ComputerSystem()[0].TotalPhysicalMemory), file=arquivo)
	print("Total do disco: %d GiB" % (total // (2**30)), "Usado: %d GiB" % (used // (2**30)), "Livre: %d GiB" % (free // (2**30)), file=arquivo)
#wql = "SELECT IPAddress FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = 'True'"
#print('Local IP address: {0}'.format(''.join(c.query(wql)[0].IPAddress)))

