import pexpect

PROMPT = ['#', '>>>', '>', '\$']

def send_command(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print (child.before)

def connect(user, host, password):
	ssh_newkey = 'Are you sure you wand to continue connecting'
	conStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(conStr)
	ret = child.expect([pexcept.TIMEOUT, ssh_newkey, '[P|p]assword:'])
	if ret == 0:
		print ('[-] Error Connecting')
		return
	if ret == 1:
		child.sending('yes')
		ret = child.expect([pexcept.TIMEOUT, '[P|p]assword:'])
		if ret == 0:
			print ('[-] Error Connecting')
			return
		
	child.sendline(password)
	child.expect(PROMPT)
	
	return child
	
def main():
	host = 'localhost'
	user = 'roor'
	password = 'toor'
	
	child = connect(user, host, password)
	send_command(child, 'cat /etc/shadow | greep root');
	
if __name__ == '__main__':
	main()	
		