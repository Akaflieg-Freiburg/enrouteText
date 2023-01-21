
Platform notes
===============

Android
-------

Network security problems
^^^^^^^^^^^^^^^^^^^^^^^^^

Like most other programs, **Enroute Flight Navigation** uses `Transport Layer
Security (TLS) <https://en.wikipedia.org/wiki/Transport_Layer_Security>`_ for
secure communication with servers on the internet.  The technology relies on
`digital certificates
<https://en.wikipedia.org/wiki/Transport_Layer_Security#Digital_certificates>`_
that are built into the Android operating system and can only be updated by the
device manufacturer through system security updates. Regretfully, manufacturers
of Android devices are often not interested in after-sales support and provide
updates only for a very short period of time, if at all.

If a device does not receive regular system updates, the certificates will
expire after a while, and secure network connections are no longer possible. `As
covered in the media
<https://techcrunch.com/2021/09/21/lets-encrypt-root-expiry>`_, many users of
systems running Android 7.1 (or below) started to experience problems on 30.
September 2021, when an important certificate expired.

When certificates expire, some apps will stop working.  Other app authors prefer
to hide the complexity of secure communication from their users and write apps
that will silently revert to insecure communication.  These apps appear to run
as normal, but leave communication (and eventually the system) open to tampering
and manipulation.

The author of **Enroute Flight Navigation** believes that pilots should be able
to make an informed decision about the security of their systems.  **Enroute
Flight Navigation** will tell the user of any network security errors.  Users
can then decide to do one of the following.

- Replace the device by a more recent model, preferably from one of the few
  manufacturers who offer long-time support for their products.
- Accept the risk of insecure communication and ignore network security errors
  in the future.

.. note:: The author, who is concerned about short-lived digital
    products, uses a `Fairphone <https://www.fairphone.com>`_ personally.
    Fairphones are long-lasting, can be repaired easily and receive many years
    of security updates.  Other brands might have similar offers.


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
starting **Enroute Flight Navigation** via the Unix command line.  The following
command line options are supported.

============== =====================
Option         Description
============== =====================
-h, --help     Displays help on commandline options.
--help-all     Displays help including Qt specific options.
-v, --version  Displays version information.
--sg           Run simulator and generate screenshots for Google Play
--sm           Run simulator and generate screenshots for the manual
============== =====================

