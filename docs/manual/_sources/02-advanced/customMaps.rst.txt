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

**Enroute Flight Navigation** is able to import MBTILES file containing raster
or vector data.  Vector data must follow the standard `OpenMapTiles
<https://github.com/openmaptiles/openmaptiles>`_ schema.  Vector maps are
rendered in the same style that **Enroute Flight Navigation** uses for its own
maps.  It is possible to install vector maps along with the maps provided by
**Enroute Flight Navigation**, in order to provide higher detail for particular
regions of interest.


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


MBTILES Map Data Sources
------------------------

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


Raster Maps in GeoTIFF format
-----------------------------

We are aware of websites that offer raster maps in GeoTIFF format. At present,
**Enroute Flight Navigation** cannot handle GeoTIFF files, but there are tools
that convert GeoTIFF to MBTILES.

- Official ICAO maps for Denmark are available from the danish `AIM Naviair
  <https://aim.naviair.dk/en/charts/>`_

- Official ICAO maps for Spain are available from the Spanish `Insignia Servicio
  de Información Aeronáutica
  <https://aip.enaire.es/AIP/CartasInsigniaImpresas-es.html>`_

- Official ICAO maps for Switzerland are available from the Swiss `Federal
  Office of Topography swisstopo
  <https://www.swisstopo.admin.ch/en/geodata/aero/icao.html>`_

- Official VFR raster charts are available from the `United States Federal
  Aviation Administration
  <https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/vfr/>`_

Users have successfully used the free tool `QGIS <https://qgis.org/en/site>`_ to
convert GeoTIFF files to MBTILES, which can then be used with **Enroute Flight
Navigation**. 

.. _QGIS-img:
.. figure:: QGIS-MainWindow.png
   :scale: 40 %
   :align: center

   QGIS Main Window

Since QGIS is a powerful tool that is not always easy to use, one user has
kindly provided the following short tutorial.

- Install QGIS on your desktop computer. On Fedora Linux, we found that the
  packages provided by the default software repository were outdated and lacked
  the necessary functionality.  We followed the installations instructions on
  the `QGIS website <https://qgis.org/en/site/forusers/download.html>`_ to
  install a current and full-featured version of the program.

- Open QGIS. Create a new project and open the GeoTIFF file in QGIS by
  dragging-and-dropping the GeoTIFF file into the QGIS window. The content of
  the GeoTIFF file should become visible.

- Choose the menu item "Project/Properties…" to open the dialog window "Project
  Properties". There, set the coordinate reference system to EPSG:3857. To
  locate the reference system, use the text field "Filter" and search for
  EPSG:3857.

- Use the menu items under "View/Panels/…" to ensure that the panels "Layer" and
  "Layer Styling" are visible. Select the layer of your GeoTIFF file and in the
  "Layer" panel.  Then, go to the "Layer Styling" panel and set "Resampling" to
  "Bilinear" for better image render quality.

- Use the menu items under "View/Panels/…" to ensure that the panel "Processing
  Toolbox" is visible. Inside the "Processing Toolbox", double-click on "Raster
  Tools→Generate XYZ Tiles (MBTILES)".  The dialog "Generate XYZ Tiles
  (MBTILES)" will open. Fill the necessary parameters, as seen in the image
  below. We found the function "Draw on Map Canvas" useful to specify the map
  extent. Pay attention to the maximum zoom level, as the time and file size
  increase significantly after zoom level 12. Depending on the size of your
  GeoTIFF and on the number of zoom levels you use, it may take a while to
  generate the MBTILES file.


.. _QGIS-Gen-img:
.. figure:: QGIS-GenerateMBTILES.png
   :scale: 40 %
   :align: center

   QGIS Generate Tiles Dialog
