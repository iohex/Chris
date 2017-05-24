import requests
import random
from lib.output import *
import optparse
import sys


__program__ = 'chris'
__version__='1.0'
__author__='iohehe'

def _info():
    print('program: '+__program__)
    print('version: '+__version__)
    print('author: '+__author__)

def _banner():
    banner = r'''
    _________________________
______________        ____
  ____ _          _
 / ___| |__  _ __(_)___
| |   | '_ \| '__| / __|        ____
| |___| | | | |  | \__ \
 \____|_| |_|_|  |_|___/   __
    ___________
        __________________________
                _______________________
    '''
    output.printHeader(banner)

# global setting
user_agent_dic = 'data/user-agent.list'
thread_count = 1
timeout = 10
allow_redirects = True
proxies = {'http':'http:127.0.0.1:666'}

# Create request header
def random_header():
    header = dict()
    with open(user_agent_dic) as agent_file:
        agent_list = agent_file.readlines()
    random_agent = random.choice(agent_list).replace('\n','')
    header.update(requests.utils.default_headers())
    header['User-Agent'] = random_agent
    return header


def _request(method,url,session=None,**kwargs):
    headers = random_header()
    kwargs['headers'] = headers
    if session:
        return session.request(method,url,proxies=proxies,**kwargs)
    else:
        return requests.request(method,url,proxies=proxies,**kwargs)


def _get(url,session=None):
    return _request('get',url)

def _post(url,session=None):
    return _request('post',url)


def detect_web(url):
    if not url.endswith("index.php"):
        url = url+"/index.php"
    output.printInfo('[INFO] detecting server info of '+url)
    with requests.Session() as session:
        r = _get(url,session=session)
        print r.text


def fuzz_start(url):
    if not url.startswith('http://'):
        url = 'http://%s'%(url)
    detect_web(url)

def main():
    _banner()

    parser  = optparse.OptionParser("ex: python chris.py url -t 10  -p'dict.txt'")
    parser.add_option('-d','--dic',dest='password',help='the password list')
    parser.add_option('-t','--thread',dest='thread',default=10,help='the thread number')
    parser.add_option('-i','--info',dest='info',help='the information of the program')
    parser.add_option('-f','--file',dest='web_file',default='php',help='the method of the request')
    (options,args)= parser.parse_args()
    if len(sys.argv)>1:
        fuzz_start(sys.argv[1])
    else:
        parser.print_help()
        sys.exit(0)

if __name__ =='__main__':
    output = CLIOutput()
    main()