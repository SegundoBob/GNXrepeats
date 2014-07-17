#!/usr/bin/python
#coding=utf-8
#@+leo-ver=5-thin
#@+node:bob06.20140218132129.1633: * @file lib_leo03.py
#@@first
#@@first
#@@language python
#@@tabwidth -4

#@+<< Copyright >>
#@+node:bob06.20140218132129.1634: ** << Copyright >>
"""
lib_leo03.py - Uniform Node Locator Functions
Copyright (C) 2013 Robert F. Hossley.  All Rights Reserved.

lib_leo03.py is Open Software and is distributed under the terms of the MIT
License. The gist of the license is that lib_leo01.py is absolutely free, even
for commercial use (including resale). There is no GNU-like "copyleft"
restriction. The Open Source Initiative board has voted to certify the
MIT license as Open Source. This license is compatible with the GPL.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Robert F. Hossley
not be used in advertising or publicity pertaining to distribution of
the software without specific, written prior permission.

DISCLAIMER OF WARRANTIES

Robert F. Hossley SPECIFICALLY DISCLAIMS ALL WARRANTIES, EXPRESSED
OR IMPLIED, WITH RESPECT TO THIS COMPUTER SOFTWARE, INCLUDING BUT NOT
LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE. IN NO EVENT SHALL REAM BE LIABLE FOR ANY LOSS OF
PROFIT OR ANY COMMERCIAL DAMAGE, INCLUDING BUT NOT LIMITED TO SPECIAL,
INCIDENTAL, CONSEQUENTIAL OR OTHER DAMAGES.

"""

#@-<< Copyright >>
#@+<< documentation >>
#@+node:bob06.20140218132129.1635: ** << documentation >>
"""
Leo-Outline walking functions

"""
#@-<< documentation >>
#@+<< version >>
#@+node:bob06.20140314140323.1635: ** << version >>
__version__ = '0.1.0'
#@-<< version >>
#@+<< imports >>
#@+node:bob06.20140218132129.1636: ** << imports >>
#@-<< imports >>

#@+others
#@+node:bob06.20140218132129.1664: ** bffpWalk() - Breadth First Full Position Walk
def bffpWalk(cmdr):
    """ Breadth First Full Position Walk
    Generator returning every Tree Position in Breadth First Order.
    
    Arguments:
        cmdr:  Commander for the tree to be walked.
    
    Returns:
        posx:  Next position in the tree.

    Exceptions:
        StopIteration:  All positions have been returned.

    """

    fifo = [(root.copy(), None) for root in cmdr.rootPosition().self_and_siblings_iter()]
    while True:
        if fifo:
            parent, index = fifo[0]
            if index is None:
                yield parent
                del fifo[0]
                fifo.append((parent, 0))
            else:
                nxtPos = parent.getNthChild(index)
                if nxtPos:
                    yield nxtPos
                    fifo[0] = (parent, index + 1)
                    fifo.append((nxtPos, 0))
                else:
                    del fifo[0]
        else:
            break
#@+node:bob06.20140218132129.1666: ** dffpWalk() - Depth First Full Position Walk
def dffpWalk(cmdr):
    """ Depth First Full Position Walk
    Generator returning every Tree Position in Depth First Order.
    
    Arguments:
        cmdr:  Commander for the tree to be walked.
    
    Returns:
        posx:  Next position in the tree.

    Exceptions:
        StopIteration:  All positions have been returned.

    """

    lifo = [(root.copy(), None) for root in cmdr.rootPosition().self_and_siblings_iter()]
    lifo.reverse()
    while True:
        if lifo:
            parent, index = lifo[-1]
            if index is None:
                yield parent
                lifo[-1] = (parent, 0)
            else:
                nxtPos = parent.getNthChild(index)
                if nxtPos:
                    yield nxtPos
                    lifo[-1] = (parent, index + 1)
                    lifo.append((nxtPos, 0))
                else:
                    lifo.pop()
        else:
            break
#@+node:bob06.20140323152354.1635: ** bffvWalk() - Breadth First Full Vnode Walk
def bffvWalk(cmdr):
    """ Breadth First Full Vnode Walk
    Generator returning every Vnode in Breadth First Order.
    
    Arguments:
        cmdr:  Commander for the tree to be walked.
    
    Returns:
        vnodex:  Next vnode in the tree.

    Exceptions:
        StopIteration:  All positions have been returned.
    
    """

    cmdr.clearAllVisited()
    fifo = [(vnodex, None) for vnodex in cmdr.hiddenRootNode.children]
    while True:
        if fifo:
            parent, index = fifo[0]
            if index is None:
                if not parent.isVisited():
                    parent.setVisited()
                    yield parent
                del fifo[0]
                fifo.append((parent, 0))
            else:
                if index < len(parent.children):
                    nxtVnode = parent.children[index]
                    if not nxtVnode.isVisited():
                        nxtVnode.setVisited()
                        yield nxtVnode
                    fifo[0] = (parent, index + 1)
                    fifo.append((nxtVnode, 0))
                else:
                    del fifo[0]
        else:
            break
#@+node:bob06.20140323152354.1637: ** dffvWalk() - Depth First Full Vnode Walk
def dffvWalk(cmdr):
    """ Depth First Full Vnode Walk
    Generator returning every Vnode in Depth First Order.
    
    Arguments:
        cmdr:  Commander for the tree to be walked.
    
    Returns:
        vnodex:  Next vnode in the tree.

    Exceptions:
        StopIteration:  All positions have been returned.

    """

    cmdr.clearAllVisited()
    lifo = [(vnodex, None) for vnodex in cmdr.hiddenRootNode.children]
    lifo.reverse()
    while True:
        if lifo:
            parent, index = lifo[-1]
            if index is None:
                if not parent.isVisited():
                    parent.setVisited()
                    yield parent
                lifo[-1] = (parent, 0)
            else:
                if index < len(parent.children):
                    nxtVnode = parent.children[index]
                    if not nxtVnode.isVisited():
                        nxtVnode.setVisited()
                        yield nxtVnode
                    lifo[-1] = (parent, index + 1)
                    lifo.append((nxtVnode, 0))
                else:
                    lifo.pop()
        else:
            break
#@-others

if __name__ == "__main__":
    main()
#@-leo
