Technical Notes
===============

Traffic Receiver
----------------

**Enroute Flight Navigation** expects that the traffic receiver deploys a WLAN
network via Wi-Fi and publishes traffic data via that network.  In order to
support a wide range of devices, including flight simulators, the app listens to
several network addresses simultaneously and understands a variety of protocols.

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
 

Protocol notes
^^^^^^^^^^^^^^

Support for the GDL90 protocal is problematic, and we recommend to use
FLARM/NMEA whenever possible.  We are aware of the following issues.


Altitude measurements

  According to the GDL90 Specification, the ownship geometric height is reported
  as height above WGS-84 ellipsoid.  There are however many devices on the
  market that wrongly report height above main sea level.  Different apps have
  different strategies to deal with these shortcomings.
  
  - **Enroute Flight Navigation** as well as the app Skydemon expect that
    traffic receivers comply with the GDL90 Specification.
  - Foreflight has extended the GDL90 Specification so that traffic receivers
    can indicate if they comply with the specification or not.
  - Many other apps expect wrong GDL90 implementations and interpret the
    geometric height has height above main sea level.


MODE-S traffic
  
  Most traffic receivers see traffic equipped with MODE-S transponders and can
  give an estimate for the distance to the traffic.  They are, however, unable
  to obtain the precise traffic position.  Unlike FLARM/NMEA, the GDL90
  Specification does not support traffic factors whose position is unknown.
  Different devices implement different workarounds.
  
  - Stratux devices generate a ring of eight virtual targets around the own
    position.  These targets are named "Mode S".
  - Air Avioncs devices do the same, but only with one target.
  - Other devices create a virtual target, either at the ownship position or at
    the north pole and abuse the field "Navigation Accuracy Category for
    Position" to give the approximate position to the target.

  **Enroute Flight Navigation** has special provisions for handling targets
  called "Mode S", but users should expect that this workaround is not perfect.


Platform notes
^^^^^^^^^^^^^^

When running on Android, the app acquires a Wi-Fi lock as soon as valid data is
received.  The lock is released when data no longer arrives.


ForeFlight Broadcast
^^^^^^^^^^^^^^^^^^^^

Following the standards established by the app ForeFlight, **Enroute Flight
Navigation** broadcasts a UDP message on port 63093 every 5 seconds while the
app is running in the foreground.  This message allows devices to discover
Enroute's IP address, which can be used as the target of UDP unicast messages.
This broadcast will be a JSON message, with at least these fields:

.. code-block:: JSON
		
  { 
     "App":"Enroute Flight Navigation",
     "GDL90":{ 
        "port":4000
     }
  }

The GDL90 "port" field is currently 4000, but might change in the future.
