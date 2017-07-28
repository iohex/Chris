import optparse
import sys
import code
from lib.output import *

__program__ = 'chris'
__version__='1.0'
__author__='iohehe'

def _info():
    print('program: '+__program__)
    print('version: '+__version__)
    print('author: '+__author__)

# global setting
output = CLIOutput()
thread_count = 1
timeout = 10
allow_redirects = True
proxies = {'http':'http:127.0.0.1:666'}

def _banner():
    banner = r'''
    _________________________
______________        ____
_________ .__          .__        
\_   ___ \|  |_________|__| ______
/    \  \/|  |  \_  __ \  |/  ___/
\     \___|   Y  \  | \/  |\___ \ 
 \______  /___|  /__|  |__/____  >
        \/     \/              \/   __
    ___________
        __________________________
                _______________________
    '''
    output.printHeader(banner)



def fuzz_start(url):
    if not url.startswith('http://'):
        url = 'http://%s'%(url)
    detect_web(url)

def interact():
    from method import *
    the_banner = _banner()
    code.interact(banner=the_banner, local=locals())


if __name__ =='__main__':
    interact()
