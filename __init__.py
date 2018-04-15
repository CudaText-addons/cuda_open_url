import os
import shlex
from subprocess import Popen
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_open_url.ini')

opt_chrome = 'chrome'
opt_chrome_pvt = 'chrome --incognito'
opt_firefox = 'firefox'
opt_firefox_pvt = 'firefox -private-window'
opt_opera = 'opera'
opt_opera_pvt = 'opera -newprivatetab'

def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'

class Command:

    def __init__(self):

        global opt_chrome
        global opt_chrome_pvt
        global opt_firefox
        global opt_firefox_pvt
        global opt_opera
        global opt_opera_pvt

        opt_chrome      = ini_read(fn_config, 'op', 'chrome', opt_chrome)
        opt_chrome_pvt  = ini_read(fn_config, 'op', 'chrome_pvt', opt_chrome_pvt)
        opt_firefox     = ini_read(fn_config, 'op', 'firefox', opt_firefox)
        opt_firefox_pvt = ini_read(fn_config, 'op', 'firefox_pvt', opt_firefox_pvt)
        opt_opera       = ini_read(fn_config, 'op', 'opera', opt_opera)
        opt_opera_pvt   = ini_read(fn_config, 'op', 'opera_pvt', opt_opera_pvt)

    def config(self):

        ini_write(fn_config, 'op', 'chrome', opt_chrome)
        ini_write(fn_config, 'op', 'chrome_pvt', opt_chrome_pvt)
        ini_write(fn_config, 'op', 'firefox', opt_firefox)
        ini_write(fn_config, 'op', 'firefox_pvt', opt_firefox_pvt)
        ini_write(fn_config, 'op', 'opera', opt_opera)
        ini_write(fn_config, 'op', 'opera_pvt', opt_opera_pvt)

        file_open(fn_config)

    def call_browser(self, browser):

        x, y, x1, y1 = ed.get_carets()[0]
        url = ed.get_prop(PROP_LINK_AT_POS, (x, y))
        if not url:
            msg_status('Cannot find URL under caret')
            return

        v = shlex.split(browser+' '+url)

        #os.spawnv(os.P_NOWAIT, v[0], v) ##don't run Firefox on Linux
        '''
        https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family
        os.spawnvp(os.P_NOWAIT, path, args)
        ==>
        Popen([path] + args[1:])
        '''

        try:
            Popen(v)
            msg_status('Running browser: '+browser)
        except:
            msg_status('Error running browser: '+browser)


    def url_chrome(self):         self.call_browser(opt_chrome)
    def url_chrome_pvt(self):     self.call_browser(opt_chrome_pvt)
    def url_firefox(self):        self.call_browser(opt_firefox)
    def url_firefox_pvt(self):    self.call_browser(opt_firefox_pvt)
    def url_opera(self):          self.call_browser(opt_opera)
    def url_opera_pvt(self):      self.call_browser(opt_opera_pvt)
