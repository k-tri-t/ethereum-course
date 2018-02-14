import subprocess
import io

proc = subprocess.Popen([
    'geth',
    '--networkid', '16',
    '--port', '30303',
    '--maxpeers', '0',
    '--nodiscover',
    '--etherbase', '0xb8ce60975590f7aebca746fc6086777bf6ca5acc',
    '--mine',
], stderr=subprocess.PIPE, bufsize=-1)

print('process id = %d' % proc.pid)

with io.open(proc.stderr.fileno(), closefd=False) as stream:
	[print(line.rstrip('\n')) for line in stream]

proc.wait()
if proc.returncode != 0:
	print('open error')
	sys.exit(1)

# end of run.py
