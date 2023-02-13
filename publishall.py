#!/usr/bin/env python

"""Allows you to publish on all your repositories.

Requirements:
    mercurial

Use:
    hg pusha
    You can also use hg pushall

Installation:
    Add the following entry to the [extensions] part of your .hg/hgrc config:
        publishall = /path/to/publishall.py

License:
    MIT (see LICENSE).

For more information, please read the README.markdown file.
"""

testedwith = '6.3.2'

from mercurial import commands, registrar

cmdtable = {}
command = registrar.command(cmdtable)

@command(b'pushall',
         [(b'', b'new-branch', None, b'pushes with new branch(es)',)],
         b"Push to all your repositories.")

def pushall(ui, repo, **opts):
    """The Publishall core function. Makes your life easier."""
    repos = ui.configitems(b'paths')
    if not repos:
        ui.warn(b"No paths defined in your hgrc. Pushall aborted.\n")
    ui.status(b"%s paths found\n" % len(repos))
    for path in repos:
        ui.status(b"* pushing to %s\n" % path[0])
        try:
            commands.push(ui, repo, path[1], **opts)
        except Exception as e:
            print(e)
    return 0

@command(b'pusha',
         [(b'', b'new-branch', None, b'pushes with new branch(es)',)],
         b"Push to all your repositories.")
def pusha(ui, repo, **opts):
    return pushall(ui, repo, **opts)
