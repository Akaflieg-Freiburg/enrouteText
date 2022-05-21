Use your own maps
=================

**Enroute Flight Navigation** comes with a set of base maps that cover large
parts of the world and are updated frequently. Still, there might be situations
where a user would like to use their own base maps. 

- Where available, some users might prefer to use official ICAO charts of their
  countries.
- Some users might prefer raster maps that follow a different style.
- Some users might prefer to install high-detail vector maps for particular
  regions of interest.

Starting with the beta version 2.16.90, **Enroute Flight Navigation** is able to
import MBTILES file containing raster or vector data.  Vector data must follow
the standard `OpenMapTiles <https://github.com/openmaptiles/openmaptiles>`_
schema.  Vector maps are rendered in the same style that **Enroute Flight
Navigation** uses for its own maps.  It is possible to install vector maps along
with the maps provided by **Enroute Flight Navigation**, in order to provide
higher detail for particular regions of interest.


Import Maps
-----------

Import Maps on Android devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using an Android device, you need to transfer the MBTILES file to the
device, and open it there.  There are many ways to transfer files, but most
users will likely do one of the following.

- Download the MBTILES file on the Android device with a web browser. The
  browser will then offer to open the file in **Enroute Flight Navigation**.

- Download the MBTILES file to a desktop computer, connect the device to the
  desktop computer via USB and then copy the file to the device. Afterwards, the
  file can be opened by a file management app on the Android device.


Import Maps on Linux Desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are running **Enroute Flight Navigation** on a Linux Desktop machine, use
the file manager to drag-and-drop the file into the main window of the app.


.. note::  MBTILES files are often extremely large. It is possible that your
  device becomes unresponsive for a few seconds while copying the file.  Also, 
  note that **Enroute Flight Navigation** will copy the file to its internal 
  data directory.  In order to save space, we recommend deleting the MBTILES file 
  once it has been imported.


Map data sources
----------------

We are aware of a few websites that offer vector or raster maps that can be used
with **Enroute Flight Navigation**.  Please let us know if you know of other map
data sources!

- The website `maptiler data <https://data.maptiler.com/downloads/planet/>`_
  provides excellent vector maps that can be installed alongside the base maps
  provided by **Enroute Flight Navigation**, in order to provide high-detail
  maps for specific regions of interest.

- The website `open flightmaps
  <https://www.openflightmaps.org/https://www.openflightmaps.org>`_ provides
  excellent aviation maps in raster format for a variety of European countries,
  as well as South Africa and Namibia.


GeoTIFF sources
^^^^^^^^^^^^^^^

We are aware of websites that offer raster maps in GeoTIFF format. At present,
**Enroute Flight Navigation** cannot handle GeoTIFF file, but there are web
services and command line tools that 

- Official ICAO maps for Denmark are available `here
  <https://aim.naviair.dk/en/charts/>`_

- Official ICAO maps for Switzerland are available `here
  <https://www.swisstopo.admin.ch/en/geodata/aero/icao.html>`_

- The commercial web service `MyGeodata
  <https://mygeodata.cloud/converter/geotiff-to-mbtiles>`_ converts GeoTIFF to
  MBTILES.

- The command line tool `gdal2mbtiles
  <https://github.com/ecometrica/gdal2mbtiles>`_ is able to convert GeoTIFF to
  MBTILES.