
Privacy policies
================

**The app Enroute Flight Navigation has been designed to not send any data to
us.** We do not track our users. We do not collect data. However, note the
following.

- The app contains third-party software components, including map rendering
  software from MapBox, Inc. While we have checked that no data is collected by
  these components, there is a chance that we overlooked something.


Internet access
---------------

The app accesses internet sites that may not be under our control. These sites
may keep access logs or track their users.

- The downloads maps and data from the server `cplx.vm.uni-freiburg.de
  <cplx.vm.uni-freiburg.de>`_ at the University of Freiburg. The app will also
  connect to this server to check for updates. 

- The app downloads METAR/TAF weather data from the `Aviation Weather Center
  <https://www.aviationweather.gov>`_, a website of the United States
  government. In order to provide relevant data, the app sends your location and
  your current route to the Aviation Weather Center at regular intervals.

- The app downloads NOTAM for your location and your intended route from servers
  of the `Federal Aviation Administration <https://api.faa.gov/s/>`_ of the
  United States government.


Privileges of the Android app
-----------------------------

The Android app requires the following privileges.

- ACCESS_COARSE_LOCATION and ACCESS_FINE_LOCATION – Accessing the device’s
  location is clearly necessary for a navigation app.

- ACCESS_NETWORK_STATE and ACCESS_WIFI_STATE – Required to automatically connect
  to traffic receivers.

- CHANGE_WIFI_MULTICAST_STATE – The app receives traffic and position
  information from traffic data receivers and flight simulators via UDP network
  broadcasts. This privilege is required to receive the relevant data packages. 

- INTERNET – This privilege is required to download and update map, data and
  METAR/TAF reports.

- VIBRATE – The app vibrates your device, for instance to give haptic feedback
  for key presses.

- WAKE_LOCK – Required to maintain Wi-Fi connections to traffic data receivers
  even when the device display is off.

- WRITE_EXTERNAL_STORAGE and WRITE_EXTERNAL_STORAGE – This privilege is required
  to store the flight map library in a globally accessible directory. This
  ensures that the library persists when the app is uninstalled or reinstalled.
  It also ensures that other apps, such as file managers or file synchronization
  software, can access the data.

The Android app asks for the following optional privilege.

- POST_NOTIFICATIONS - The app uses notifications, for instance to inform the
  user about available map updates.
