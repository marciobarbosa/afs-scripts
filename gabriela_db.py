from subprocess import call
import time

def add_host():
	call(['/usr/afs/bin/bos', 'addhost', 'marcio', 'gabriela'])

def remove_host():
	call(['/usr/afs/bin/bos', 'removehost', 'marcio', 'nayane'])

def shutdown_processes():
	call(['/usr/afs/bin/bos', 'shutdown', 'nayane'])

def start_processes():
	call(['/usr/afs/bin/bos', 'start', 'gabriela', 'ptserver'])
	call(['/usr/afs/bin/bos', 'start', 'gabriela', 'vlserver'])

if __name__ == '__main__':
	add_host()
	remove_host()
	shutdown_processes()
	start_processes()