Collection
==========

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




**Flight Data**

 


**Flight Mode**

As soon as you are flying, the moving maps switches to *flight mode*.  The
figure :ref:`movingMapFlightMode` shows how the display will look while you are
in the air.

.. note:: Flight detection might fail in slow-flying aircraft, such as balloons
   or paragliders.  The settings allow to force the flight mode to "on".

.. _movingMapFlightMode:
.. figure:: ./fig_FlightModeTu.png
   :scale: 50 %
   :align: center
   :alt: Moving map display in flight mode

   Moving map display in flight mode

1. Own Position.  The blue arrow shape indicates that the satellite navigation
   system knows your position and your direction of movement.
2. Flight Path Vector, showing the projected track for the next five Minutes.
3. North Indicator.  This button can also be used to switch between the display
   modes *track up* and *north up*.
4. Autopan button.  Click this button to switch to *autopan mode* where the map
   is automatically centered about your current position.  Pan the map manually
   to stop the *autopan mode*.
5. Zoom buttons.
6. Menu button.

The bottom of the display shows a little panel with the following information.

* Altitude
* Ground Speed
* True Track
* Universal Coordinated Time (UTC)

.. warning:: The display shows the altitude reported by the satellite navigation
   system, with geoid corrections applied.  Depending on temperature and air
   density, the value will generally differ from the value shown by your
   barometric altimeter, even if the altimeter is set to QNH.  **The altitude
   reading must not be used for navigation in airspace classes C and D.**


Your first flight
-----------------

Now you are ready for the first use of **Enroute Flight Navigation**. General
operation is very intuitive. The primary purpose of **Enroute Flight
Navigation** of displaying a moving aeronautical map is directly available after
starting the app.  Before using the moving map function you have to make sure
the GPS of your mobile device is operating properly. The own position indicator
will be gray if GPS position is not available and will be displayed in blue
color if GPS position is available. The own position will be indicated as round
shape when no motion is sensed and displayed as an arrow with flight path marker
when moving.

.. warning:: Make sure the GPS position is correct and valid to avoid loss of
    situational awareness. Loss of situational awareness is a common cause of
    severe accidents in aviation.

To show a planned route on the moving map display you may:

1. Use 'Direct'
    * Double Touch the desired Waypoint
    * Select 'Direct'
2. Plan a route
    * Double Touch the desired Waypoint
    * Select (+) 'to Route'

The planned route will be displayed as a light green line on the map
display. More detailed information on route planning will be given in the
dedicated section.

**Airspace awareness**

Information related to any selected point on the Map will be displayed when
double touching a point.


The displayed Information for arbitrary points will include:

* Distance to point
* True bearing to point
* Airspace classification including related frequencies and transponder code

The displayed Information for reporting points or Navaids will include:

* Distance to point
* True bearing to point
* Designation, controlling agency and radio frequencies
* Airspace classification including related radio frequencies and transponder
  code

The displayed Information for airfields will include:

* Distance to point
* True bearing to point
* Meteorological information summary if available
* Designation, controlling agency and radio frequencies and Navaids
* Airfield data for Runways and field elevation
* Airspace classification including related radio frequencies and transponder
  code

More information on the features and operation will be given in the 'Further
Steps' part of the **Enroute Flight Navigation** manual.

The following topics are described in more detail **Enroute Flight Navigation**
'Reference' section of the manual:

* Display of Airspace
* Display of Aeronautical Data
* Weather Data
* Settings


