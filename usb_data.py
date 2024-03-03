import usb.core
import struct
from http.server import HTTPServer, BaseHTTPRequestHandler

def main():
	dev = usb.core.find(idVendor = 0x1a86, idProduct = 0x7523)
	ep = dev[0].interfaces()[0].endpoints()[0]
	i = dev[0].interfaces()[0].bInterfaceNumber
	dev.reset()

	if dev.is_kernel_driver_active(i):
		dev.detach_kernel_driver(i)

	dev.set_configuration()
	eaddr = ep.bEndpointAddress

	names = {"volt1": 0, "volt2": 0, "curr1": 0, "curr2": 0, "temp1": 0, "temp2": 0}

	while True:
		#Read and decode 256 bytes
		r = dev.read(eaddr, 256)
		decoded_data = struct.pack('B'*len(r),*r).decode('utf-8')

		open_p = True
		name = ""
		curr_name = ""
		val = ""

		with open('usb_data.txt', 'w') as file:
			file.write(str(names["volt1"]) + "\n")
			file.write(str(names["volt2"]) + "\n")
			file.write(str(names["curr1"]) + "\n")
			file.write(str(names["curr2"]) + "\n")
			file.write(str(names["temp1"]) + "\n")
			file.write(str(names["temp2"]) + "\n")

		#Parse and tokenize the decoded value
		for i in range(len(r)):
			#Start getting string for name and finish getting float for value
			if decoded_data[i] == "(":
				open_p = True

				try:
					if curr_name in names:
						names[curr_name] = float(val)
				except ValueError as e:
					pass

				val = ""
				continue

			#Start getting float for value and finish getting string for name
			elif decoded_data[i] == ")":
				open_p = False

				if name in names:
					pass

				curr_name = name
				name = ""
				continue

			#Get the strings for name and value
			if open_p == True:
				name += decoded_data[i]
			elif open_p == False:
				val += decoded_data[i]

if __name__ == "__main__":
	main()
