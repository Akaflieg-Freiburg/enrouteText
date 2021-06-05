Map Data
===========

The Information displayed by the Map of Enroute Flight Navigation is provided by the following resources:

    *  openAIP
    *  open flightmaps
    *  Map Tiler
    *  Open Street Map

To get more detailed Information on these Resources you may touch the link on the lower edge of the map Display **Map Data Copyright Info**. After touching the line **Map Data Copyright Info** a sub window will open showing links to the contributor web sites:
    * https://www.openaip.net
    * https://www.openflightmaps.org
    * https://www.maptiler.com
    * https://www.openstreetmap.org

**Open AIP**

Open AIP has the goal to deliver free, current and precise data for air navigation to everyone. Open AIP is a web based and crowd-sourced platform.
The Open AIP provides the basic source aeronautical data for display in Enroute Flight Navigation.

**Open Flight Maps**

Open Flight Maps is an open-source project providing aeronautical data for a high quality VFR Map.
Open Flight Maps is providing some additional information, where available.

The detailed split of the data sources for the Enroute Flight Naviagtion map is shown below:

+--------------------------------+----------------+
| Map Feature                    |   Data Origin  |
+================================+================+
| Airfields                      |  openAIP       |
+--------------------------------+----------------+
| Airspace: Nature Preserve Areas| open flightmaps|
+--------------------------------+----------------+
| Airspace: all other            | openAIP        |
+--------------------------------+----------------+
| Navaids                        | openAIP        |
+--------------------------------+----------------+
|Procedures (Traffic Circuits, …)|open flightmaps |
+--------------------------------+----------------+
| Reporting Points               | open flightmaps|
+--------------------------------+----------------+



**Map Tiler**

Is a software application to combine multiple layers of data for maps and provide the map in a format for loading and display.
The Enroute Flight Naviagtion base maps are edited versions of maps kindly provided by Klokan Technologies through the OpenMapTiles project.

**Open Street Map**

Open Street Map (OSM) is a collaborative project to create a free editable map of the world. The geodata underlying the map is considered the primary output of the project. The creation and growth of OSM has been motivated by restrictions on use or availability of map data across much of the world, and the advent of inexpensive portable satellite navigation devices.
The Open Street Map data is used to crate the base maps.


Other
=====

The Map display is composed of two layers selected in the respective Tabs of the
'Map Library' screen:

* Aeronautical Map
* Base Map


**Aeronautical Maps**

The Aeronautical Map layers is showing the airspace data on the Map screen. If
no Base Map is installed for the area only the information coming from the
Aviation Map data is displayed.

The Aeronautical Map contains:

* Airfields
* Airspace boundaries
* Navaids
* Reporting points and routes (if available)

The display used for aerospace data is using the following basic color scheme:

* Red:
    * Line with shadow inside for Restricted Airspace
    * Shadow with dashed blue border for Aerodrome Control Zone (CTR)
    * Dashed Line for Parachute Jumping Exercise area
    * Line for Glider or Microlight Traffic pattern

* Blue:

    * Line with shadow for controlled airspace (A, B, C, D)
    * Shadow with dashed blue border for Radio Mandatory Zone (RMZ)
    * Airport, reporting point or Navaid  symbols
    * For Route or Traffic Pattern for powered aircraft

* Green:

    * Line with shadow for Natural Reserve Area (NRA)
    * Line for airspace control sector boundaries

* Black:

    * Dashed Line for Transponder Mandatory Zone (TMZ)


**Class 1 and Class 2 maps:**

* Class 1 maps are compiled from openAIP and open flightmaps data. These maps
  contain complete information about airspaces, airfields and navaids. In
  addition, the maps contain (mandatory) reporting points. Some of our tier 1
  maps also show traffic circuits and flight procedures for control zones.
* Class 2 maps are compiled from openAIP data only. They contain complete
  information about airspaces, airfields and navaids.

Details on the maps may be found at
<https://akaflieg-freiburg.github.io/enroute/maps/> The Aeronautical Map data is
selected on the “Map Library” – “Aviation Data” page accessed via the “Settings”
Menu.  To update the list of available maps the “…” option in the upper right
corner of the screen may be used.  You may install or uninstall the aviation Map
data for a county by the selection on the right hand side of the country
list. To find a country you have to scroll up and down in the list.

.. note:: To have optimum presentation of the **Enroute Flight Navigation** map
    display install the Aviation Map and the Base Map for all areas you intend
    to use **Enroute Flight Navigation**.
.. caution:: No airspace information will be provided in country when the
    Aeronautical Map is not installed for it.
.. note:: **Enroute Flight Navigation** will automatically check for updated
    Maps on the Enroute server and show a pop-up window after start if updated
    maps have been detected.  You will be asked if you want to update the map or
    delay the update.

**Base Map**

The Base Map layers is showing the geographic data on the Map screen. If no Base
Map is shown for an area it will be shown in the white background color. If no
Aviation Map is installed for the area only the information coming from the Base
Map data is displayed. The Base Map is organized in tiles. This will result in
not stopping the Base Map display abruptly at the border of an installed
country, but showing some overlap.  The Base Map will show:

* Landmass
* Water Surface (oceans, lakes and rivers)
* Forests
* Main Roads
* Railroad lines
* City names

.. note:: To have optimum presentation of the **Enroute Flight Navigation** map
    display install the Aeronautical Map and the Base Map for all areas you
    intend to use **Enroute Flight Navigation**.
.. note:: **Enroute Flight Navigation** will not show most cultural build ups
    and limits or settled area boundaries to reduce the map size.


Flight mode and ground mode
---------------------------

**Ground Mode**

Ground Mode is displayed by **Enroute Flight Navigation** whenever the sensed
speed is below the threshold and the Menu item 'Automatic Flight Detection' is
not set to 'Always in Flight Mode'.  Ground Mode does not display the Flight
Data line at the lower end of the screen and is intended for flight planning.
