#!/usr/bin/python
#coding=utf-8
#@+leo-ver=5-thin
#@+node:bob07.20140715160011.1575: * @file hrngpS2.py
#@@first
#@@first
#@@language python
#@@tabwidth -4

import os
import sys

import leo.core.leoBridge as leoBridge

import lib_leo03

#@+others
#@+node:bob07.20140715160011.1576: ** gnxRepeats()
def gnxRepeats(cmdrx, infoList):
    hrnGnx = cmdrx.hiddenRootNode.gnx
    gnxDict = {hrnGnx: cmdrx.hiddenRootNode.h}
    errorFlag = False
    for vnode in lib_leo03.bffvWalk(cmdrx):
        hdr = '"{0}"'.format(vnode.h)
        if vnode.gnx in gnxDict:
            errorFlag = True
            hdr = '"{0}" {1}'.format(gnxDict[vnode.gnx], hdr)
        gnxDict[vnode.gnx] = hdr
    infoList.append('Error: {0}'.format(errorFlag))
    gnxList = gnxDict.keys()
    gnxList.sort()
    for gnx in gnxList:
        infoList.append('{gnx} {hdrs}'.format(gnx=gnx, hdrs=gnxDict[gnx]))
#@-others

TestDir = 'hidden_root_tsts'

def main():
    infoList = list()
    fpn1 = sys.argv[1]
    bridge = leoBridge.controller(gui='nullGui', verbose=False,
        loadPlugins=False, readSettings=False)
    leoG = bridge.globals()
    infoList.append('After bridge create: {0}'.format(leoG.app.nodeIndices.lastIndex))
    cmdr1 = bridge.openLeoFile(fpn1)
    infoList.append('After {fpn} open: {idx}'.format(fpn=fpn1, idx=leoG.app.nodeIndices.lastIndex))
    rp = cmdr1.rootPosition()
    posx = rp.insertAfter()
    posx.h = '{cnt} - {idx}'.format(cnt=2, idx=1)
    infoList.append('After adding 1 vnode: {idx}'.format(fpn=fpn1, idx=leoG.app.nodeIndices.lastIndex))

    gnxRepeats(cmdr1, infoList)

    fpnError = os.path.join(TestDir, 'SlaveLog.txt')
    fdError = open(fpnError, 'w')
    fdError.write('\n'.join(infoList) + '\n')
    fdError.close()

if __name__ == "__main__":
    main()

#@-leo
