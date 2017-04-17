from JumpScale import j

try:
    import xonsh
except BaseException:
    j.sal.process.executeInteractive("pip3 install colored-traceback")
    j.sal.process.executeInteractive("pip3 install xonsh")
    j.sal.process.executeInteractive("pip3 install pudb")
    j.sal.process.executeInteractive("pip3 install tmuxp")
    import xonsh


#from pudb import set_trace; set_trace()


class Xonsh:

    def __init__(self):
        self.__jslocation__ = "j.tools.xonsh"
        self.executor = j.tools.executorLocal
        self._cuisine = self.executor.cuisine

    def configAll(self):
        self.config()
        self.configTmux(True)

    def config(self):
        C = """
        from JumpScale import j
        $XONSH_SHOW_TRACEBACK = True
        $XONSH_STORE_STDOUT = True
        $XONSH_LOGIN = True

        #from pprint import pprint as print

        import colored_traceback
        colored_traceback.add_hook(always=True)
        import sys


        from tools.xonsh.XonshAliases import *

        aliases['jsgo'] = xonsh_go
        aliases['jsedit'] = xonsh_edit
        aliases['jsupdate'] = xonsh_update


        """
        self._cuisine.core.file_write("$HOMEDIR/.xonshrc", C)

    def configTmux(self, restart=True):
        self._cuisine.tmux.configure(restart, True)
