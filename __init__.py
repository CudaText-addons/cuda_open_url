import os
import shlex
import webbrowser
from subprocess import Popen
from cudatext import *

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_open_url.ini')

opt_chrome = 'chrome'
opt_chrome_pvt = 'chrome --incognito'
opt_firefox = 'firefox'
opt_firefox_pvt = 'firefox -private-window'
opt_opera = 'opera'
opt_opera_pvt = 'opera -newprivatetab'
opt_ie = 'iexplore.exe'
opt_ie_pvt = 'iexplore.exe -private'
opt_tool1 = ''
opt_tool2 = ''
opt_handle_click = True
opt_action_on_click = -1

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
        global opt_handle_click
        global opt_action_on_click
        global opt_tool1
        global opt_tool2

        opt_chrome      = ini_read(fn_config, 'op', 'chrome', opt_chrome)
        opt_chrome_pvt  = ini_read(fn_config, 'op', 'chrome_pvt', opt_chrome_pvt)
        opt_firefox     = ini_read(fn_config, 'op', 'firefox', opt_firefox)
        opt_firefox_pvt = ini_read(fn_config, 'op', 'firefox_pvt', opt_firefox_pvt)
        opt_opera       = ini_read(fn_config, 'op', 'opera', opt_opera)
        opt_opera_pvt   = ini_read(fn_config, 'op', 'opera_pvt', opt_opera_pvt)

        opt_tool1   = ini_read(fn_config, 'op', 'tool_1', '')
        opt_tool2   = ini_read(fn_config, 'op', 'tool_2', '')

        opt_handle_click = str_to_bool(ini_read(fn_config, 'op', 'handle_click', bool_to_str(opt_handle_click)))
        opt_action_on_click = int(ini_read(fn_config, 'op', 'action_on_click', '-1'))


    def config(self):

        ini_write(fn_config, 'op', 'chrome', opt_chrome)
        ini_write(fn_config, 'op', 'chrome_pvt', opt_chrome_pvt)
        ini_write(fn_config, 'op', 'firefox', opt_firefox)
        ini_write(fn_config, 'op', 'firefox_pvt', opt_firefox_pvt)
        ini_write(fn_config, 'op', 'opera', opt_opera)
        ini_write(fn_config, 'op', 'opera_pvt', opt_opera_pvt)

        ini_write(fn_config, 'op', 'tool_1', opt_tool1)
        ini_write(fn_config, 'op', 'tool_2', opt_tool2)

        ini_write(fn_config, 'op', 'handle_click', bool_to_str(opt_handle_click))
        ini_write(fn_config, 'op', 'action_on_click', str(opt_action_on_click))

        file_open(fn_config)


    def on_click_dbl(self, ed_self, state):

        if not opt_handle_click: return

        url = self.get_url()
        if not url: return

        items = [
            'Open in default browser',
            'Open in Chrome',
            'Open in Chrome, private mode',
            'Open in Firefox',
            'Open in Firefox, private mode',
            'Open in Opera',
            'Open in Opera, private mode',
            'Open in IE',
            'Open in IE, private mode',
            ]

        if opt_action_on_click >= 0:
            res = opt_action_on_click
        else:
            res = dlg_menu(MENU_LIST, items, caption='Open URL')
        if res is None:
            return False

        if res==0: webbrowser.open_new_tab(url)
        elif res==1: self.run(opt_chrome, url)
        elif res==2: self.run(opt_chrome_pvt, url)
        elif res==3: self.run(opt_firefox, url)
        elif res==4: self.run(opt_firefox_pvt, url)
        elif res==5: self.run(opt_opera, url)
        elif res==6: self.run(opt_opera_pvt, url)
        elif res==7: self.run(opt_ie, url)
        elif res==8: self.run(opt_ie_pvt, url)

        return False #disable std click handling


    def get_url(self):

        x, y, x1, y1 = ed.get_carets()[0]
        return ed.get_prop(PROP_LINK_AT_POS, (x, y))


    def run(self, browser, url):

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
            msg_status('Running: "'+browser+'"')
        except:
            msg_status('Error running: "'+browser+'"')


    def url_default(self):
        webbrowser.open_new_tab(self.get_url())

    def url_chrome(self):
        self.run(opt_chrome, self.get_url())

    def url_chrome_pvt(self):
        self.run(opt_chrome_pvt, self.get_url())

    def url_firefox(self):
        self.run(opt_firefox, self.get_url())

    def url_firefox_pvt(self):
        self.run(opt_firefox_pvt, self.get_url())

    def url_opera(self):
        self.run(opt_opera, self.get_url())

    def url_opera_pvt(self):
        self.run(opt_opera_pvt, self.get_url())

    def url_ie(self):
        self.run(opt_ie, self.get_url())

    def url_ie_pvt(self):
        self.run(opt_ie_pvt, self.get_url())

    def url_tool1(self):
        self.run(opt_tool1, self.get_url())

    def url_tool2(self):
        self.run(opt_tool2, self.get_url())
