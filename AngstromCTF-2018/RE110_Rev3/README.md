# REV3

**Category:** Reverse Engineering
**Points:** 110
**Description:**

> Let's try Rev 3! For this executable, you will need to figure out what input makes the program return "Correct". You don't need the shell server for this one, but the binary can be found at /problems/rev3/ on the shell server.

## Write-up

```python
def decode(encoded_flag):
	print "".join([chr((ord(x)+3)^0x9) for x in encoded_flag])


encoded_flag = "egzloxi|ixw]dkSe]dzSzccShejSi^3q"
decode(encoded_flag)
```


