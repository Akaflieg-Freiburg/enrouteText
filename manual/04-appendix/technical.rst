Technical Notes
===============

Traffic Receiver
----------------

**Enroute Flight Navigation** expects that the traffic receiver deploys a WLAN
network via Wi-Fi and publishes traffic data via that network.  In order to
support a wide range of devices, including flight simulators, the app listens to
several network addresses simultaneously.

- The app tries to establish TCP connections to port 2000 at the IP addresses
  192.168.1.1 and 192.168.10.1, where it expects to read a stream of FLARM/NMEA
  sentences.  The NMEA sentences must conform to the specification outlined in the
  document FTD-012 `Data Port Interface Control Document (ICD)
  <https://flarm.com/support/manuals-documents/>`_, Version 7.13, as published by
  `FLARM Technology Ltd <https://flarm.com/>`_.

- The app tries to establish UDP connections to ports 4000 and 49002, where it
  expects datagrams in GDL90 or XGPS format.  The datagrams must conform to the
  `GDL 90 Data Interface Specification
  <https://www.faa.gov/nextgen/programs/adsb/archival/media/gdl90_public_icd_reva.pdf>`_
  or the XGPS format specified on the `ForeFlight Web site
  <https://www.foreflight.com/support/network-gps/>`_.

When running on Android, the app acquires a WiFi lock as soon as valid data is
received.  The lock is released when data no longer arrives.
