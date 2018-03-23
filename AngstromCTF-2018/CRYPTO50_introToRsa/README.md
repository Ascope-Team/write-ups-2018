# Intro To RSA

**Category:** Cryptography
**Points:** 50
**Description:**

> One common method of public key encryption is the RSA algorithm. Given p, q, e, and c, see if you can recover the message and find the flag!

## Write-up

```python
from pwn import *

# p = process('./guessPublic64')
p = remote('shell.angstromctf.com', 1235)

p.recvuntil("max):")
p.sendline("0x%3$x-0x%9$x")

p.recvuntil("sum?")
data = p.recvuntil("guess:")
numbers = data.split("'s guess")[0].strip().split('-')

p.sendline(str(int(numbers[0],16)+int(numbers[1],16)))

print p.recvall()
```


