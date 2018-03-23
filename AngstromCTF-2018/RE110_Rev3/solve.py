
encoded_flag = "egzloxi|ixw]dkSe]dzSzccShejSi^3q"


def decode(encoded_flag):
	print "".join([chr((ord(x)+3)^0x9) for x in encoded_flag])
decode(encoded_flag)