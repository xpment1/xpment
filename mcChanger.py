
import os

import subprocess
from subprocess import call 


sudoPassword='F!retornado9'

def macChanger():
    
    command2 = 'ifconfig wlp2s0 down'
    command3 = 'macchanger -r wlp2s0'
    command4 = 'ifconfig wlp2s0 up'

    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command2))
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command3))
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command4))

    


macChanger()




def customChanger():
    
    cmd1='ifconfig wlp2s0 down'
    cmd2='ifconfig wlp2s0 hw ether 70:BB:E9:69:1F:BE'
    cmd3='ifconfig wlp2s0 up'
    
    #works with shell command
    call('echo {} | sudo -S {}'.format(sudoPassword, cmd1), shell=True)
    call('echo {} | sudo -S {}'.format(sudoPassword, cmd2), shell=True)
    call('echo {} | sudo -S {}'.format(sudoPassword, cmd3), shell=True)


customChanger()
