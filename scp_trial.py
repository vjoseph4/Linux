import paramiko
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('xxx.xxx.x.x', 22, 'user', 'password')

with SCPClient(ssh.get_transport()) as scp:
    scp.put('filename.txt', 'destination/filename.txt')
    scp.get('source/filename.txt', 'filename.txt')


