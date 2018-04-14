import os,shlex
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_open_url.ini')

option_int = 100
option_bool = True

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

class Command:
    
    def __init__(self):

        global option_int
        global option_bool
        option_int = int(ini_read(fn_config, 'op', 'option_int', str(option_int)))
        option_bool = str_to_bool(ini_read(fn_config, 'op', 'option_bool', bool_to_str(option_bool)))

    def config(self):

        ini_write(fn_config, 'op', 'option_int', str(option_int))
        ini_write(fn_config, 'op', 'option_bool', bool_to_str(option_bool))
        file_open(fn_config)

    def call_browser(self, browser, site):
        ss=shlex.split(browser+' '+site)
        os.spawnv(os.P_NOWAIT+os.P_OVERLAY,ss[0],ss)

    def url_chrome(self):
        self.call_browser('chrome.exe','www.foo.com')

    def url_chrome_pvt(self):
        self.call_browser('chrome.exe --incognito','www.foo.com')

    def url_firefox(self):
        pass
        
    def url_firefox_pvt(self):
        pass
        
    def url_opera(self):
        pass
        
    def url_opera_pvt(self):
        pass
