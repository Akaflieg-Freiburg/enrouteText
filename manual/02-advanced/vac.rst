Import visual approach charts
=============================


.. warning:: This section describes a new feature currently in the beta 
  test phase. At present, the functionality is only available to a small group
  of testers.


**Enroute Flight Navigation** is can import visual approach charts and display
them on the moving map.  The figure :ref:`vac` shows how this will typically
look.

.. _vac:
.. figure:: ./VAC.png
   :scale: 30 %
   :align: center
   :alt: Moving map display with approach chart

   Moving map display with embedded approach chart

**Enroute Flight Navigation** accepts visual approach charts in one of the
following formats.

* Geo-referenced image files in GeoTIFF format.
* TripKits that contain collections of approach charts for a specific area or
  flight route. The latest beta version of the `AIP Browser DE
  <https://mpmediasoft.de/products/AIPBrowserDE/help/AIPBrowserDE.html>`_ can
  produce TripKits for Germany.

.. note:: GeoTIFF is a complex format that supports many use cases, ranging 
  from astronomy to high-precision land survey. **Enroute Flight Navigation**
  only supports a subset of the GeoTIFF standard. If you encounter a GeoTIFF 
  file that **Enroute Flight Navigation** does not recognize, please 
  `open an issue report 
  <https://github.com/Akaflieg-Freiburg/enroute/issues/new/choose>`_.
  We will be glad to help!


Obtain approach chart files
---------------------------

* Michael Paus' free software `AIP Browser DE
  <https://mpmediasoft.de/products/AIPBrowserDE/help/AIPBrowserDE.html>`_ can
  generate GeoTIFF images and TripKits for all German airfields. The data comes
  from Germany's official `AIP <https://aip.dfs.de/basicAIP>`_, as provided by
  `DFS Deutsche Flugsicherung GmbH <https://www.dfs.de/homepage>`_.

* For testing purposes, we provide `a few TripKits and Approach Charts
  <https://v2202001110709105590.ultrasrv.de/nextcloud/index.php/s/jFqd9ykgLgmDpSf>`_
  for download on our servers. These files will be removed once the testing
  phase ends.

Please get in touch with us if you are aware of other data sources. We will be
glad to list them here.


Import approach chart files
---------------------------
 
Import on Android devices
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using an Android device, you must transfer the approach chart file or
TripKit file to the device and open it there. There are many ways to transfer
files, but most users will likely do one of the following.

- Download the file on the Android device with a web browser. The browser will
  then offer to open the file in **Enroute Flight Navigation**.

- Upload the file to a cloud storage service, such as "Google Drive", "Microsoft
  OneDrive", "Apple iCloud" or a "NextCloud" instance. Connect your device to
  the service and use a file management program on your device to open the file.

.. note:: TripKits are ZIP files with specialized content. Trying to open a 
  TripKit file, some file management utilities will automatically unpack the ZIP 
  file rather than offering to open it in **Enroute Flight Navigation**.  Along 
  similar lines, GeoTIFF files are image files with specialized metadata and some
  file management utilities will launch an image viewing application rather than
  offering to open a GeoTIFF file in **Enroute Flight Navigation**.
  
  If you encounter problems opening a TripKit or GeoTIFF file, look for an icon
  or menu item labeled "Open with…".  Some utilities open an appropriate context 
  menu after a tap-and-hold gesture.

Import on the Linux desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you run **Enroute Flight Navigation** on a Linux Desktop machine, drag and
drop the file into the app's main window.


Manage your approach chart collection
-------------------------------------

On the moving map screen, open the main menu and go to "Library/Maps and Data".
The page "Map and Data Library" will then open. The page has a "VAC" tab listing
the approach charts. Use the context menus to uninstall charts and retrieve
basic information.


Use approach charts
-------------------

Once approach charts are installed, open the main menu and go to "Approach
Charts". The page "Visual Approach Charts" will then open. The page lists all
approach charts installed in your device, sorted by distance to the current
position. Tap on a chart to open "Approach Chart" page, which shows a slightly
simplified moving map with the approach chart superimposed on top of the usual
map layer. As usual, tap on the left arrow symbol in the page title to close the
page and return to the standard moving map display.

.. note:: The menu entry "Approach Charts" is only visible if approach
  charts are installed on your device. If you cannot find the menu entry, 
  install some approach charts first.
