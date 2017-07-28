import requests
import random
from lib.output import *

output = CLIOutput()
user_agent_dic = 'data/user-agent.list'

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
        return session.request(method,url,**kwargs)
    else:
        return requests.request(method,url,**kwargs)


def get(url,session=None):
    url = format_web(url)
    return _request('get',url)

def post(url,session=None):
    format_web(url)
    return _request('post',url)

def format_web(url):
    if not url.startswith("http://"):
        url = "http://"+url
        return url
    output.printInfo('[INFO] detecting server info of '+url)
