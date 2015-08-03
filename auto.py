from subprocess import call
import time

def remove_all():
	call(['/etc/init.d/afs', 'stop'])
	call(['pkill', 'bosserver'])
	call(['rm', '-r', '/usr/vice/etc'])
	call(['rm', '-r', '/usr/afs'])
	call(['rm', '-r', '/usr/afsws'])
	call(['rm', '/etc/init.d/afs'])
	call(['rm', '-r', '/etc/sysconfig'])

def create_directories():
	call(['mkdir', '-p', '/usr/vice/etc'])
	call(['mkdir', '-p', '/usr/afs'])
	call(['mkdir', '-p', '/usr/afsws'])

def copy_files():
	path = '/home/marcio/openafs/amd64_linux26/dest/'
	call(['cp', '-rp', path + 'root.client/usr/vice/etc/.', '/usr/vice/etc'])
	call(['cp', '-p', path + 'root.client/usr/vice/etc/afs.rc', '/etc/init.d/afs'])
	call(['chmod', '755', '/etc/init.d/afs'])
	call(['mkdir', '-p', '/etc/sysconfig'])
	call(['cp', path + 'root.client/usr/vice/etc/afs.conf', '/etc/sysconfig/afs'])
	call(['cp', '-rp', path + 'root.server/usr/afs/.', '/usr/afs'])
	call(['cp', '-rp', path + 'bin/', path + 'etc/', path + 'include/', path + 'lib/', '/usr/afsws'])

def copy_lib():
	call(['cp', '-r', '/home/marcio/openafs/amd64_linux26/dest/lib/.', '/lib'])

def run_bos_noauth():
	call(['/usr/afs/bin/bosserver', '-noauth'])

def set_cell_name():
	call(['/usr/afs/bin/bos', 'setcellname', 'marcio.marcio.edu', 'marcio.edu', '-noauth'])

def create_db_processes():
	call(['/usr/afs/bin/bos', 'create', 'marcio.marcio.edu', 'ptserver', 'simple', '/usr/afs/bin/ptserver', '-noauth'])
	call(['/usr/afs/bin/bos', 'create', 'marcio.marcio.edu', 'vlserver', 'simple', '/usr/afs/bin/vlserver', '-noauth'])

def add_user():
	call(['/usr/afs/bin/bos', 'adduser', 'marcio.marcio.edu', 'admin', '-noauth'])
	call(['/usr/afs/bin/asetkey', 'add', '2', '/etc/afs.keytab', 'afs/marcio.edu'])

def pt_create_user():
	time.sleep(5)
	call(['/usr/afs/bin/pts', 'createuser', '-name', 'admin', '-noauth'])
	call(['/usr/afs/bin/pts', 'adduser', 'admin', 'system:administrators', '-noauth'])
	call(['/usr/afs/bin/bos', 'restart', 'marcio.marcio.edu', '-all', '-noauth'])

def create_processes():
	call(['/usr/afs/bin/bos', 'create', 'marcio.marcio.edu', 'fs', 'fs', '/usr/afs/bin/fileserver',
		'/usr/afs/bin/volserver', '/usr/afs/bin/salvager', '-noauth'])

def restore_volumes():
	time.sleep(5)
	call(['/usr/afs/bin/vos', 'syncvldb', 'marcio.marcio.edu', '-verbose', '-noauth'])
	call(['/usr/afs/bin/vos', 'syncserv', 'marcio.marcio.edu', '-verbose', '-noauth'])

def remove_links():
	call(['rm', '/usr/vice/etc/ThisCell'])
	call(['cp', '/usr/afs/etc/ThisCell', '/usr/vice/etc/ThisCell'])
	call(['rm', '/usr/vice/etc/CellServDB'])
	call(['cp', '/usr/afs/etc/CellServDB', '/usr/vice/etc/CellServDB'])

def create_cache():
	fd = open("/usr/vice/etc/cacheinfo", "w")
	call(['mkdir', '/usr/vice/cache'])
	fd.write("/afs:/usr/vice/cache:50000")
	fd.close()

def reboot():
	call(['pkill', 'bosserver'])
	call(['/etc/init.d/afs', 'restart'])
	call(['/usr/afs/bin/bosserver', '-noauth'])

def insert_ip_addr():
	fd =  open("/usr/afs/etc/CellServDB", "a")
	fd_cli = open("/usr/vice/etc/CellServDB", "a")
	fd.write("192.168.25.23\t #nayane\n")
	fd.write("192.168.25.25\t #gabriela\n")
	fd_cli.write("192.168.25.23\t #nayane\n")
	fd_cli.write("192.168.25.25\t #gabriela\n")
	fd.close()
	fd_cli.close()

def get_tokens():
	call(['/home/marcio/openafs/amd64_linux26/dest/bin/aklog'])

def setup_remote_fileserver():
	call(['ssh', 'root@192.168.25.23', '/etc/init.d/afs', 'stop'])
	call(['ssh', 'root@192.168.25.23', 'pkill', 'bosserver'])
	call(['scp', '-r', '/usr/afs/etc/.', 'root@192.168.25.23:/usr/afs/etc'])
	call(['ssh', 'root@192.168.25.23', '/etc/init.d/afs', 'start'])
	call(['ssh', 'root@192.168.25.23', '/usr/afs/bin/bosserver'])
	call(['ssh', 'root@192.168.25.25', '/etc/init.d/afs', 'stop'])
	call(['ssh', 'root@192.168.25.25', 'pkill', 'bosserver'])
	call(['scp', '-r', '/usr/afs/etc/.', 'root@192.168.25.25:/usr/afs/etc'])
	call(['ssh', 'root@192.168.25.25', '/etc/init.d/afs', 'start'])
	call(['ssh', 'root@192.168.25.25', '/usr/afs/bin/bosserver'])

def restart_processes():
	call(['/usr/afs/bin/bos', 'restart', 'marcio.marcio.edu', 'fs'])
	call(['/usr/afs/bin/bos', 'restart', 'marcio.marcio.edu', 'ptserver', 'vlserver'])
	call(['/usr/afs/bin/bos', 'restart', 'nayane.marcio.edu', 'fs'])
	call(['/usr/afs/bin/bos', 'restart', 'nayane.marcio.edu', 'ptserver', 'vlserver'])
	call(['/usr/afs/bin/bos', 'restart', 'gabriela.marcio.edu', 'fs'])
	call(['/usr/afs/bin/bos', 'restart', 'gabriela.marcio.edu', 'ptserver', 'vlserver'])

if __name__ == '__main__':
	remove_all()
	create_directories()
	copy_files()
	copy_lib()
	run_bos_noauth()
	set_cell_name()
	create_db_processes()
	add_user()
	pt_create_user()
	create_processes()
	restore_volumes()
	remove_links()
	create_cache()
	reboot()
	insert_ip_addr()
	setup_remote_fileserver()
	reboot()
	get_tokens()
	restart_processes()