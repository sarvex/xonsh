import os

def pwd(args, stdin, stdout, stderr, controller):
    e = __xonsh_env__['PWD']
    if '--help' in args:
        print(HELP_STR, file=stdout)
        return 0
    if '-P' in args:
        e = os.path.realpath(e)
    print(e, file=stdout)
    return 0


HELP_STR = """This version of pwd was written in Python for the xonsh project: http://xon.sh
Based on pwd from GNU coreutils: http://www.gnu.org/software/coreutils/

Usage: pwd [OPTION]...
Print the full filename of the current working directory.

  -L, --logical    use PWD from environment, even if it contains symlinks
  -P, --physical   avoid all symlinks
      --help       display this help and exit"""
