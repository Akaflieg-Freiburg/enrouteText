Connecting your traffic receiver
================================

In order to display nearby traffic on the moving map, **Enroute Flight
Navigation** can connect to your aircraft's traffic receiver (typically a FLARM
device).

The app author has tested the **Enroute Flight Navigation** with the following
traffic receivers.

- `AT-1 AIR Traffic <http://www.air-avionics.com/?page_id=253>`_ by `Air
  Avionics <http://www.air-avionics.com/>`_ with software version 5.

Users reported success with the following traffic receivers.

- `Stratux devices <http://stratux.me/>`_
- `TTGO T-Beam devices <https://www.amazon.de/TTGO-T-Beam-915Mhz-Wireless-Bluetooth/dp/B07SFVQ3Z8>`_


Before you connect
------------------

Before you try to connect this app to your traffic receiver, make sure that the
following conditions are met.

- Your traffic receiver has an integrated Wi-Fi interface that acts as a
  wireless access point. Bluetooth devices are currently not supported.
- You know the network name (=SSID) of the WLAN network deployed by your traffic
  receiver. If the network is encrypted, you also need to know the WLAN
  password.
- If you use a Stratux or T-Beam device, set the device IP address to
  192.168.1.1.  Most FLARM devices use this address default and  no
  configuration is required.
- Some devices require an additional password in order to access traffic
  data. This is currently **not** supported. Set up your device so that no
  additional password is required.

  
Connecting to the traffic receiver
----------------------------------

It takes a two steps to connect **Enroute Flight Navigation** to the traffic
receiver for the first time. Once things are set up properly, your device should
automatically detect the traffic receiver's WLAN network, enter the network and
connect to the traffic data stream whenever you go flying.

Step 1: Enter the traffic receiver's WLAN network

- Make sure that the traffic receiver has power and is switched on. In a typical
  aircraft installation, the traffic receiver is connected to the 'Avionics'
  switch and will automatically switch on. You may need to wait a minute before
  the WLAN comes online and is visible to your device.
- Enter the WLAN network deployed by your traffic receiver. This is usually done
  in the "WLAN Settings" of your device. Enter the WLAN password if
  required. Some devices will issue a warning that the WLAN is not connected to
  the internet. In this case, you might need to confirm that you wish to enter
  the WLAN network.

Most operating systems will offer to remember the connection, so that your
device will automatically connect to this WLAN in the future. We recommend to
use this option.

Step 2: Connect to the traffic data stream

Open the main menu and navigate to the "Information" menu.

- If the entry "Traffic Receiver" is highlighted in green, then **Enroute Flight
  Navigation** has already found the traffic receiver in the network and has
  connected to it. Congratulations, you are done!
- If the entry "Traffic Receiver" is not highlighted in green, then select the
  entry. The "Traffic Receiver Status" page will open. The page explains the
  connection status in detail, and explains how to establish a connection
  manually.

Troubleshooting
---------------

**The app cannot connect to the traffic data stream.**

- Check that your device is connected to the WLAN network deployed by your
  traffic receiver.

  
**The connection breaks down after a few seconds.**

Most traffic receivers cannot serve more than one client and abort connections
at random if more than one device tries to access.

- Make sure that there no second device connected to the traffic receiver's WLAN
  network. The other device might well be in your friend's pocket!
- Make sure that there is no other app trying to connected to the traffic
  receiver's data stream.
- Many traffic receivers offer "configuration panels" that can be accessed via a
  web browser. Close all web browsers.
