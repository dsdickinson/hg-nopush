"""nopush

Prohibit pushes from predefined directories.
"""
from mercurial import util
import os

# Every command must take ui and and repo as arguments.
# opts is a dict where you can find other command line flags.
#
# Other parameters are taken in order from items on the command line that
# don't start with a dash. If no default value is given in the parameter list,
# they are required.
#
# For experimenting with Mercurial in the python interpreter:
# Getting the repository of the current dir:
#    >>> from mercurial import hg, ui
#    >>> repo = hg.repository(ui.ui(), path = ".")

def nopush(ui, repo):
	# The doc string below will show up in hg help.
	"""Prohibit pushes from predefined directories."""
	pwd = os.getcwd()
	dirs = ui.configlist('nopush', 'nopush_dirs', default=None, untrusted=False)

	try:
		for dir in dirs:
			if pwd == dir:
				# Raise an Abort exception if the node has only one parent.
				raise util.Abort('Pushing from directory "%s" is not allowed.' % dir)
	except IndexError:
		# Raise an Abort exception if the node has only one parent.
		raise util.Abort('Something bad just happened')

cmdtable = {
	# "command-name": (function-call, options-list, help-string)
	'nopush': (nopush, [], "hg push")
}

testedwith = '3.3'
