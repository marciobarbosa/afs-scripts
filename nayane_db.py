from subprocess import call
import time

def remove_hosts():
	call(['/usr/afs/bin/bos', 'removehost', 'marcio', 'marcio'])
	call(['/usr/afs/bin/bos', 'removehost', 'marcio', 'gabriela'])
	call(['/usr/afs/bin/bos', 'removehost', 'nayane', 'marcio'])
	call(['/usr/afs/bin/bos', 'removehost', 'nayane', 'gabriela'])
	call(['/usr/afs/bin/bos', 'removehost', 'gabriela', 'marcio'])
	call(['/usr/afs/bin/bos', 'removehost', 'gabriela', 'nayane'])

def shutdown_processes():
	call(['/usr/afs/bin/bos', 'shutdown', 'marcio', 'ptserver'])
	call(['/usr/afs/bin/bos', 'shutdown', 'marcio', 'vlserver'])
	call(['/usr/afs/bin/bos', 'shutdown', 'nayane', 'fs'])
	call(['/usr/afs/bin/bos', 'shutdown', 'gabriela'])

def restart_processes():
	call(['/usr/afs/bin/bos', 'restart', 'marcio', 'fs'])
	call(['/usr/afs/bin/bos', 'restart', 'nayane', 'ptserver'])
	call(['/usr/afs/bin/bos', 'restart', 'nayane', 'vlserver'])

if __name__ == '__main__':
	remove_hosts()
	shutdown_processes()
	restart_processes()