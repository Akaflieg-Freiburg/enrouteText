
================
Route Planning
================

Waypoints
---------

Waypoints are the central element of aeronautical navigation. A waypoint is selected by touching the moving map at the location of the waypoint display. When a waypoint is selected a pop up window will show detailed information of the waypoint. Waypoints may also be directly added to a route by list selection or search.
A waypoint may be directly added from the waypoint pop-up window to the end of the current route by touching the "+" selection at the lower end.
The selection of "--> Direct" will overwrite the current route by a route from current location to the selected point. Overwriting the current route has to be confirmed if a route is present.

The following types of Waypoints are available:

    * Aerodromes
    * Reporting points
    * Navaids
    * Arbitrary points on the map.

For Aerodromes the full set of information will be displayed:

    * Aerodrome symbol indicating type of airport
    * Aerodrome designation
    * Distance and Bearing to Aerodrome
    * Meteorological information if available
    * Aerodrome communication information
    * Runway direction and length
    * Field elevation
    * Airspace data

For Reporting Points the following information will be displayed:

    * Reporting Point designation
    * Distance and bearing to Reporting Point
    * Reporting Point communication information
    * Airspace data

For Navaids the following information will be displayed:

    * Navaid symbol, designation and type
    * Distance and bearing to Navaid
    * Navaid ID, frequency and elevation
    * Airspace data

For Arbitrary Points the following information will be displayed:

    * Point designation if manually entered
    * Distance and bearing to Point
    * Airspace data



Flight Routes
-------------
Enroute Flight Navigation provides direct planning of one flight Route. A Route will remain present until it is cleared.
Route planning is entered via the Menu point Route. The Menu is entered via the Menu symbol in the upper left corner of the map area. Then the Route symbol has to be touched to go to the Route area.

A Route may be planned in the following ways:
    * “Add Waypoint” in the Route window will open a selection window for a waypoint and add the selected waypoint to the route.
    * “+” symbol in the waypoint details pop-up window will add the waypoint to the last position of the Route.
    * “Direct” in the waypoint details pop-up window will provide a Route between current position and desired waypoint
    
.. note::
          The designation of a Waypoint may be changed after touching the pencil symbol in waypoint line of the Route screen. 

The Route Display will show the following information:

* Symbol of the waypoint
* Designation of the waypoint
* Route Point Menu
* Navigation Data
    * Distance between way points
    * Time calculated between way points using the cruise speed set in the “Aircraft and Wind” page
    * True Course between way points
    * True Heading between way points

.. note::

          A Route may also be imported from a GPX file from another PC. After sending the GPX file as Email attachment Enroute Flight Navigation will offer to open the GPX file.

The Route Point Menu provides the option to:

* Move a waypoint up in the Route
* Move a waypoint down in the Route
* Remove a waypoint from the Route

The Route Menu is entered by touching the Route Menu Symbol on the Route page.
For Arbitrary Points the standard designation "Waypoint" may be changed by touching the pencil symbol and entering a designation.

The following options are available from the Route Menu:

* Open a previously stored route from the library
* Save the current route to the library
* View the route library
* Share the Route in JSON or GPX format
* Open the Route in another APP using the JSON or GPX format
* Clear Route
* Reverse Route

The previously created and stored routes will be kept in a data base within Enroute Flight Navigation. Routes consist of the data for the selected way points. The Route data may be exported for use in other applications.

The Route display has 3 Sub windows:
    * Route
    * Wind
    * ACFT

At the lower end of the route window the calculated data of the total route will be displayed:
    * Total Distance
    * Total flight time
    * Fuel consumed

.. warning::
          Make sure wind and aircraft speed are correct. Failure to  enter correct data will result in wrong route time and fuel consumed calculation. The route time and fuel consumed are calculated using the aircraft speed and wind entered at previously. 
 
Route – Aircraft and Wind
-------------------------

The Aircraft and Wind sub-pages of the Route page allows to enter aircraft performance and wind data required for navigational calculations.
The aircraft data will be used to determine the distance of the flight and the true course.
The Wind data will will be used to calculate the true heading and duration of the flight. The duration of the flight will determine the fuel used.
Enroute Flight Navigation only offers a very superficial flight planning and cannot replace a full flight planning, but is only intended to provide quick reference.

.. note::
          Aircraft and wind data will be automatically kept in memory. For any calculation the aircraft and wind data entered at last occasion will be used.

.. warning::

         Always perform a full flight preparation in accordance with the flight manual of the aircraft used. The use of Enroute Flight Navigation as primary flight planning may cause accidents leading to loss of lives. 

The Wind sub-page of the Route page offers the following input fields:
    * Direction in degrees
    * Speed in knots

Only one speed, fuel consumption and wind may be entered for the whole route.

The Aircraft sub-page of the Route page offers the following input fields:

* Aircraft
    * Cruise Speed: Average Speed for Route
    * Descent Speed: Allows to enter a different speed for the descent phase (Currently not used)
    * Fuel Consumption: Average Fuel consumption per hour
