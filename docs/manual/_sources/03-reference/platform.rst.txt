
Platform notes
===============

Android
-------

Screen backlighting
^^^^^^^^^^^^^^^^^^^

**Enroute Flight Navigation** overrides the system settings of your device and
ensures that the screen backlighting is always on.  To save battery power, the
screen can be switched off manually with the hardware "power button" of your
device.


Screen locking
^^^^^^^^^^^^^^

**Enroute Flight Navigation** stays on top of the lock screen of your device.
It will therefore be shown immediately as soon as the screen is switched on.
You can therefore use **Enroute Flight Navigation** without unlocking your
device.


Wi-Fi locking
^^^^^^^^^^^^^

When running on Android, **Enroute Flight Navigation** acquires a Wi-Fi lock as
soon as the app receives heartbeat messages from one of the channels where it
listens for traffic receivers.  The lock is released when the messages no longer
arrive.



Linux desktop
-------------

File import by drag-and-drop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to import files by dragging and dropping then anywhere in the
main window of **Enroute Flight Navigation**.  The following file types are
accepted.

=============== ======= =============
Content         Format  File name 
=============== ======= =============
FLARM Test Data Text    \*.txt
Flight Route    GeoJSON \*.geojson 
Flight Route    GPX     \*.gpx
=============== ======= =============


Command line
^^^^^^^^^^^^

Rather than importing file by drag-and-drop, file names can also be given when
starting **Enroute Flight Navigation** via the Unix command line.  The followin
command line options are supported.

============== =====================
Option         Description
============== =====================
-h, --help     Displays help on commandline options.
--help-all     Displays help including Qt specific options.
-v, --version  Displays version information.
-s             Run simulator and generate screenshots for manual
============== =====================

