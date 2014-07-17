GNXrepeats
==========

Files needed to demonstrate that leoBridge can use one GNX for several different vnodes.

Bug Demonstration
-----------------

This git repository contains three .py files that demonstrate the bug.

Put all three .py files in one directory.  Execute hrngpM2.py.  This creates a sub-directory hidden_root_tsts containing several files, among which is SlaveLog.txt.  Here is a a SlaveLog.txt from a run that shows the bug:

```
After bridge create: 0
After hidden_root_tsts/test1.leo open: 6
After adding 1 vnode: 7
Error: True
bob07.20140717152454.4 "<hidden root VNode>" "1 - 3"
bob07.20140717152454.7 ""2 - 1"" "1 - 6"
---- End SlaveLog.txt ---
```

This indicates that "Hidden Root Node" for the Slave session has the same GNX as the node with headline "1 - 3" created by the Master session; and the node with headline "2 - 1" created by the Slave session has the same GNX as the node with headline "1 - 6" created by the Master session.

Build 7e04b48a7477 runs this test much faster than build 2b9f8da59fc7.  Using 2b9f8da59fc7 I had to run the test four times before it showed the bug.  Your experience will vary based on the speed of your system.
