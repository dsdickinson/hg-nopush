# README #

Mercurial extension to prohibit pushes from predefined directories.

### Synopsis ###

The nopush extension lets an admin prevent users from performing an 'hg push' in predefined local repository directories. Occasionally, it may be necessary to have repo directories setup whose only function is to receive updates from the mercurial server. For instance, a staging website could be setup and run from a local repo to test the on going integrity of the code there. When pulls are automatically performed on the repo, commits may also be necessary. These commits conjest the history and typically are undesired to be pushed back up to the central repository. This extension prevents that from happening. 

* Version 1.0

* [Mercurial wiki - NoPushExtension](https://mercurial.selenic.com/wiki/NoPushExtension)

### Setup ###

Below is an example configuration file (hgrc). It is recommended that these settings be placed in the server's global hgrc file (/etc/mercurial/hgrc) to prevent pushes from all users on the server.

~~~~
[extensions]
nopush = /home/<user>/hg/hg-nopush/nopush.py

[nopush]
nopush_dirs = /home/<user>/hg/repo1, /home/<user>/hg/repo2

[hooks]
pre-push = hg nopush
~~~~

### Contact ###

Steve Dickinson

Email: [dsdickinson-atat-gmail.com](dsdickinson-atat-gmail.com)

Web: [www.codeuniversity.com](http://www.codeuniversity.com)