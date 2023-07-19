import platform, subprocess

so = platform.system()

current_machine_id = subprocess.check_output('wmic path SoftwareLicensingService get OA3xOriginalProductKey').decode().split('\n')[1].strip()

with open("relkey_retag.txt", "w") as arquivo:
	print ("\nMáquina:\t\t" + platform.node(), file=arquivo)
	print ("\nPlataforma:\t" + platform.platform(), file=arquivo)
	print("\nLicença:\t" + current_machine_id, file=arquivo)
