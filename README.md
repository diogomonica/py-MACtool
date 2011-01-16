# MAC Address Generator & Changer for Linux and OS X

This application generates and changes the interface MAC Address. There is the possibility of generating a completely random MAC Address:
	
	husk:py-MacTool hip$ sudo python MACtool.py en0
	[*] Generated MAC address: 00:4a:5d:44:70:0f for device en0
	[*] Done
	
But you can also choose a Manufacturer from which the MAC Address should be generated:

	husk:py-MacTool hip$ sudo python MACtool.py -m Apple en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[*] Generated MAC address: 00:26:08:0f:09:1a for device en0
	[*] Done
	husk:py-MacTool hip$ sudo python MACtool.py -m Intel en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[*] Generated MAC address: 00:02:b3:4f:6c:0c for device en0
	[*] Done
	husk:py-MacTool hip$ sudo python MACtool.py -m FAKE en0
	[+] Found Manufacturer List: manufacturer_list.txt
	[-] Manufacturer: FAKE not found.
	
Finally, you can also choose your own MAC Address, or just the prefix (in this example we are setting the DE:AD:BE:EF prefix). The application will generate the remainder of the MAC Address randomly.
	
	husk:py-MacTool hip$ sudo python MACtool.py -p de:ad:be:ef en0
	[*] Generated MAC address: de:ad:be:ef:55:0e for device en0
	[*] Done

This Application was tested on Ubuntu 10.10 and OS X 10.6+, and uses the latest manufacturer list from Wireshark: http://anonsvn.wireshark.org/wireshark/trunk/manuf. You can also use just getMAN.py as a wrapper to the manufacturer list:

	husk:py-MacTool hip$ python getMAN.py Apple
	[+] Found Manufacturer List: manufacturer_list.txt
	['00:10:FA', '00:1C:B3', '00:1E:C2', '00:1F:5B', '00:1F:F3', '00:21:E9', '00:22:41', '00:23:12', '00:23:32', '00:23:6C', '00:23:DF', '00:24:36', '00:25:00', '00:25:4B', '00:25:BC', '00:26:08', '00:26:4A', '00:26:B0', '00:26:BB', '04:1E:64', '10:93:E9', '10:9A:DD', '18:E7:F4', '24:AB:81', '34:15:9E', '40:A6:D9', '40:D3:2D', '44:2A:60', '58:1F:AA', '58:55:CA', '58:B0:35', '5C:59:48', '60:33:4B', '60:FB:42', '64:B9:E8', '70:CD:60', '78:CA:39', '7C:6D:62', '7C:C5:37', '88:C6:63', '8C:7B:9D', '90:27:E4', '90:84:0D', 'B8:FF:61', 'C4:2C:03', 'C8:BC:C8', 'CC:08:E0', 'D4:9A:20', 'D8:30:62', 'D8:A2:5E', 'DC:2B:61', 'E0:F8:47', 'E8:06:88', 'F0:B4:79', 'F8:1E:DF']
	
	