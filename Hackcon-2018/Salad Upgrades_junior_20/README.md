# Salad Upgrades
**Category**: Junior
**Points**: 20

# Write-up
```python
crypted_flag= "l4bv{gv1i_1l_m0q4s10p}g0jl"
flag = ""

for i in range(len(crypted_flag)):
	if ord(crypted_flag[i]) >= ord('a') and ord(crypted_flag[i])<=ord('z'):

		decalage = i+8
		new = ord(crypted_flag[i])-decalage
		if new < ord('a'):
			new += 26
		flag += chr(new)
	else:
		flag += crypted_flag[i]
print flag
```