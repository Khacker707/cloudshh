import os
import random, string
password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

cmd1 = 'wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
os.system(cmd1)
cmd2 = 'unzip -qq -n ngrok-stable-linux-amd64.zip'
os.system(cmd2)
cmd3 = 'apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null'
os.system(cmd3)
cmd4 = 'echo root:$password | chpasswd'
os.system(cmd4)
cmd5 = 'mkdir -p /var/run/sshd'
os.system(cmd5)
cmd6 = 'echo "PermitRootLogin yes" >> /etc/ssh/sshd_config'
os.system(cmd6)
cmd7 = 'echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config'
os.system(cmd7)
cmd8 = 'echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc'
os.system(cmd8)
cmd9 = 'echo "export LD_LIBRARY_PATH" >> /root/.bashrc'
os.system(cmd9)
get_ipython().system_raw('/usr/sbin/sshd -D &')
print("Copy authtoken from https://dashboard.ngrok.com/auth")
import getpass
authtoken = getpass.getpass()
get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')
print("Root password: {}".format(password))

