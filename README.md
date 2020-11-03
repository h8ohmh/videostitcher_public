# videostitcher_public V0.2

**Important: 
Videostitcher is NOT finished now. Use it at your own Risk!!!**

**Version:**
0.2 of 1-Sept-2020

**Operational:** 
Videostitcher is supposed to be used for stitching **large amounts of corrupted videofiles** in timely correct order together after a datacrash and data recovery of disks/storage devices, recovered by (linux) testdisk and photorec on a fast desktop PC or server

**Usage:**
Currently it is still not very usable by a simple commandline, because of the almost completely different usage of underlying ffmpeg, mplayer and avifix binaries. It creates currently in this version a json-file containing all data of each video file and a batch (bash) file containing the concatenation command(lines) The finished videostiter will either create the resulting files by self (by python task-switcher module) or generate a batch file containing all commands 
**YOU HAVE TO KNOW PYTHON2/3 VERY WELL and to use sometimes some online translator to understand some german comments**

**Depends:**
Python2/3, pymediainfo, pandas, ffmpeg, mplayer and avifix!!!

**Remarks:**
Due to afore mentioned problems with the not uniform and not very easy (*really said: completely weird and messy*) commandlines and videoformats/standards of ffmpeg, mplayer, avifix etc., it is still 
a Trial and Error to get correct result. **Everyone is encouraged to make it better in usage etc.**




