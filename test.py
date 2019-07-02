# Paramiko used for SSH capabilities
import pprint
import select
import datetime
import paramiko


def main():
    pp = pprint.PrettyPrinter()
    client = paramiko.SSHClient()
    output=""
    hostname = ""
    connected = False
    client.load_system_host_keys()
    try:
        client.connect(hostname, username='ubuntu')
        print(f'Successful connection at ',datetime.datetime.now())
        stdin, stdout, stderr = client.exec_command('ls -l')
        connected = True
        stdout = stdout.readlines()
        for line in stdout:
            output=output+line
        if output!="":
            print(output)
        client.close()
    except (paramiko.ssh_exception.BadHostKeyException, paramiko.ssh_exception.AuthenticationException, 
            paramiko.ssh_exception.SSHException, paramiko.ssh_exception.socket.error) as e:
        print(e)
        

# Try connecting, record time of attempt
# If fails, record that it fails and output that it fails
# If trial is successful, record and output that it succeeded
# Read from a configuration file (yml?)
#   Read what time intervals to test
#   Also read each of the services to test 

main()
