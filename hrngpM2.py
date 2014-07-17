#!/usr/bin/python
#coding=utf-8
#@+leo-ver=5-thin
#@+node:bob07.20140715160011.1574: * @file hrngpM2.py
#@@first
#@@first
#@@language python
#@@tabwidth -4

import os
import shutil
import subprocess
import sys

import leo.core.leoBridge as leoBridge


#@+others
#@-others

TestDir = 'hidden_root_tsts'

def main():
    if os.path.exists(TestDir):
        shutil.rmtree(TestDir)
    os.makedirs(TestDir)
    cnt = 0
    infoList = list()
    bridge = leoBridge.controller(gui='nullGui', verbose=False,
        loadPlugins=False, readSettings=False)
    leoG = bridge.globals()
    infoList.append('After bridge create: {0}'.format(leoG.app.nodeIndices.lastIndex))

    fpn1 = os.path.join(TestDir, 'test{0}.leo'.format(1))
    cmdrx = bridge.openLeoFile(fpn1)
    infoList.append('After {fpn}: {idx}'.format(fpn=fpn1, idx=leoG.app.nodeIndices.lastIndex))
    rp = cmdrx.rootPosition()
    rp.h = '1 - 1'
    for idx in xrange(2, 7):
        posx = rp.insertAfter()
        posx.h = '{cnt} - {idx}'.format(cnt=1, idx=idx)
    infoList.append('After 5 vnode creates: {0}'.format(leoG.app.nodeIndices.lastIndex))

    rp = cmdrx.rootPosition()
    cmdrx.selectPosition(rp)
    cmdrx.executeMinibufferCommand('sort-siblings')

    again = True
    while again:
        again = False
        for posx in cmdrx.all_positions_iter():
            if posx.h not in ['1 - 3', '1 - 6']:
                posx.doDelete()
                again = True
                break

    infoList.append('After sorting and 3 vnode deletes: {0}'.format(leoG.app.nodeIndices.lastIndex))
    cmdrx.save()
    cmdrx.close()

    returnCode = subprocess.call(['python', 'hrngpS2.py', fpn1])
    infoList.append('subprocess return code = {0}'.format(returnCode))

    fpnError = os.path.join(TestDir, 'MasterLog.txt')
    fdError = open(fpnError, 'w')
    fdError.write('\n'.join(infoList) + '\n')
    fdError.close()

if __name__ == "__main__":
    main()

#@-leo
