from subprocess import call
import time

def add_host():
	call(['/usr/afs/bin/bos', 'addhost', 'marcio', 'nayane'])

def remove_host():
	call(['/usr/afs/bin/bos', 'removehost', 'marcio', 'gabriela'])

def shutdown_processes():
	call(['/usr/afs/bin/bos', 'shutdown', 'gabriela'])

def start_processes():
	call(['/usr/afs/bin/bos', 'start', 'nayane', 'ptserver'])
	call(['/usr/afs/bin/bos', 'start', 'nayane', 'vlserver'])

if __name__ == '__main__':
	add_host()
	remove_host()
	shutdown_processes()
	start_processes()