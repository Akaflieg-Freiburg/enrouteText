Use your own maps
=================

**Enroute Flight Navigation** comes with a set of base maps that cover large
parts of the world and are updated frequently. Still, there might be situations
where a user would like to use their own base maps. 

- Where available, some users might prefer to use official ICAO charts of their
  countries.
- Some users might prefer raster maps following a different style.
- Some users might prefer to install high-detail vector maps for particular
  regions of interest.

**Enroute Flight Navigation** is able to import MBTILES file containing raster
or vector data.  Vector data must follow the standard `OpenMapTiles
<https://github.com/openmaptiles/openmaptiles>`_ schema.  Vector maps are
rendered in the same style that **Enroute Flight Navigation** uses for its own
maps.  It is possible to install vector maps along with the maps provided by
**Enroute Flight Navigation**, in order to provide higher detail for particular
regions of interest.

.. note:: If you import vector maps, then make sure that the maps contain all 
   the data that you require.  For instance, the vector maps provided by 
   `maptiler data <https://data.maptiler.com/downloads/planet/>`_ do not show 
   cable cars or gondolas. If you install maptiler maps along with the maps 
   provided by **Enroute Flight Navigation**, you may find that cable cars are 
   not shown, depending on how far you zoom into the map.
   

Sources
-------

- The website `maptiler data <https://data.maptiler.com/downloads/planet/>`_
  provides excellent vector maps that can be installed alongside the base maps
  provided by **Enroute Flight Navigation**, in order to provide high-detail
  maps for specific regions of interest.

- The website `open flightmaps
  <https://www.openflightmaps.org/https://www.openflightmaps.org>`_ provides
  excellent raster maps for a variety of European countries, as well as South 
  Africa and Namibia.

There are several sources for raster map in `GeoTIFF
<https://en.wikipedia.org/wiki/GeoTIFF>`_ format. 

- `ICAO Map Denmark <https://aim.naviair.dk/en/charts>`_
- `ICAO Map Switzerland <https://www.swisstopo.admin.ch/en/geodata/aero/icao.html>`_