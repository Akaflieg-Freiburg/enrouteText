Getting started
===============

Installing the App
------------------

**Enroute Flight Navigation** is available as an Android App in the Google Play
Store.  To install the App **Enroute Flight Navigation** you may use the
following steps:

* Open Google Play Store
* Select "Apps"
* Search for **Enroute Flight Navigation**
* Touch the Symbol
* Select Install


Installing maps
---------------

To use **Enroute Flight Navigation** you have to install Maps covering the area
of flight.  For installing Maps the following steps have to be followed:

* Open the Menu by touching the area in the upper right side of the screen
* Open the menu item 'Settings'
* touch the item 'Maps' in the *Libraries* section
* Select the desired Maps by clicking the download Symbol

The Map display is composed of two layers selected in the respective Tabs of the 'Map Library' screen:
* Aeronautical Map
* Base Map

.. caution::
    Make sure Aeronautical and Base Map are installed for desired area of flight to avoid flight into areas without map display.

**Aeronautical Maps**

The Aeronautical Map layers is showing the airspace data on the Map screen. If no Base Map is installed for the area only the information coming from the Aviation Map data is displayed.

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

The Base Map layers is showing the geographic data on the Map screen. If no Base Map is shown for an area it will be shown in the white background color. If no Aviation Map is installed for the area only the information coming from the Base Map data is displayed. The Base Map is organized in tiles. This will result in not stopping the Base Map display abruptly at the border of an installed country, but showing some overlap.
The Base Map will show:

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

.. figure:: ./fig_GroundMode.png
    :align: center

*Legend*:

1. Own Position (No valid GPS position)
2. North Indicator, also area to switch between track up and north up
3. Zoom area to increase map scale (+) and reduce map scale (-)
4. Map Scale reference indicator
5. Menu area

There are two basic ways to plan a flight route:

* Menu - Route:

    * Enter Waypoints
    * Edit existing Route
    * Enter Wind data
    * Enter Aircraft data

* Double touch Maps and open Waypoints
    * Direct will make a route from present position to Waypoint
    * '+' to Route will add the Waypoint to the current Route

A Route will remain in **Enroute Flight Navigation** until overwritten or
removed. Routes may be saved or shared.

**Flight Mode**

When **Enroute Flight Navigation** senses a speed above the threshold it will
automatically switch to flight mode.  For the displays given in flight mode
refer to Figure 3: Flight Mode (Track Up) In flight mode the following
additional items will be displayed:
* The own position will be changes from a dot to an arrow
* A segmented flight path for the next 5 minutes will be indicated
* A flight data line will indicate the following GPS data:
* Altitude in feet (or meters if metric units selected)
* Ground Speed in knots (or km/h if metric units selected)
* Track in reference to true north
* Universal Coordinated Time (UTC)

.. figure:: ./fig_FlightModeTu.png
    :align: center

*Legend*:

1. Own Position
2. Flight Path Vector (5 Minutes)
3. North Indicator, also area to switch between track up and north up
4. Center on Position area
5. Zoom area
6. Menu area


The **Enroute Flight Navigation** map display is automatically centered to
display the own position to have about 80 % of the display area in direction of
flight.  The map display may be shifted by touching the display and moving it to
the desired position. After shifting the “Center on Position” Symbol will be
displayed. After touching he “Center on Position” Symbol the map will be
centered to give maximum map area in direction of flight again.

**Track Up and North Up Mode**

The **Enroute Flight Navigation** map display may be switched between a Track Up
display and a North Up display by touching the gray window in the upper right
area.  Touching the display orientation area toggles between North up and Track
Up.


.. figure:: ./fig_FlightModeTu.png
    :align: center

*Legend*:

1. Own Position
2. Flight Path Vector (5 Minutes)
3. North Indicator, also area to switch between track up and north up
4. Zoom area
5. Scale
6. Menu area

The North Up mode provides a map display always showing the map north up.  The
**Enroute Flight Navigation** map display in North Up mode will center the
display to provide about 80% area in direction of flight.  In case the map
display has been manually rotated the area besides the direction arrow will show
the map orientation in degrees.

Your first flight
-----------------

Now you are ready for the first use of **Enroute Flight Navigation**. General
operation is very intuitive. The primary purpose of **Enroute Flight
Navigation** of displaying a moving aeronautical map is directly available after
starting the app.  Before using the moving map function you have to make sure
the GPS of your mobile device is operating properly. The own position indicator
will be gray if GPS position is not available and will be displayed in blue
color if GPS position is available. The own position will be indicated as round
shape when no motion is sensed and displayed as arrow with flight path marker
when moving.

.. warning::
    Make sure the GPS position is correct and valid to avoid loss of situational awareness. Loss of situational awareness is a common cause of severe accidents in aviation.

To show a planned route on the moving map display you may:

1. Use 'Direct'
    * Double Touch the desired Waypoint
    * Select 'Direct'
2. Plan a route
    * Double Touch the desired Waypoint
    * Select (+) 'to Route'

The planned route will be displayed as light green line on the map display. More detailed information on route planning will be given in the dedicated section.

**Airspace awareness**

Information related to any selected point on the Map will be displayed when double touching a point.


The displayed Information for arbitrary points will include:

* Distance to point
* True bearing to point
* Airspace classification including related frequencies and transponder code

The displayed Information for reporting points or Navaids will include:

* Distance to point
* True bearing to point
* Designation, controlling agency and radio frequencies
* Airspace classification including related radio frequencies and transponder code

The displayed Information for airfields will include:

* Distance to point
* True bearing to point
* Meteorological information summary if available
* Designation, controlling agency and radio frequencies and Navaids
* Airfield data for Runways and field elevation
* Airspace classification including related radio frequencies and transponder code


More information on the features and operation will be given in the 'Further
Steps' part of the **Enroute Flight Navigation** manual.

The following topics are described in more detail **Enroute Flight Navigation**
'Reference' section of the manual:

* Display of Airspace
* Display of Aeronautical Data
* Weather Data
* Settings


