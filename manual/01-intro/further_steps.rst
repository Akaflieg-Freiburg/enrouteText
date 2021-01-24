Further Steps
=============

When using Enroute Flight Navigation on a frequent basis you may want to get into some more detail on the features and configure the app.

Menu
----
Functions not directly accessible on the moving map display and more options are accessed via the menu symbol in the upper left edge of the moving map display.

When touching the Menu area in the left upper corner of the screen the menu will open and give the following options:

* Route --- see Flight Routes described below
* Nearby Waypoints  --- will show the closest 20 aerodromes, navaids or reporting points
* Weather   --- will open the weather display
* Set Altimeter --- allows to enter current altitude to have altitude with an offset
* Settings --- see below
* Information
    * Satellite Status
    * Manual
    * About Enroute Flight Navigation
    * Participate
    * Donate
* Bug Report
* Exit

Only some reference to Menu items is given in this section. More details may be found in the 'Reference' section of  the manual.


Settings
-------------
The settings Menu will allow to customize Enroute Flight Navigation and give access to program status.
The settings Menu gives the following options:

* **Hide Airspace above FL 100** --- allows to select display of airspace above FL100 displayed.
* **Automatic flight detection** --- allows to select the display of flight mode on the ground
* **Flight Routes** --- will show a window with the previously stored routes
* **Maps** --- will show a window with the available and previously installed Aviation and Base Maps
* **Use metric units** --- allows to select display in metric units
* **Use English** --- allows to select English Language for display

.. note::

    The items to be selected by the on-off slider will enable the related function. The current status of the selected item is shown below the item.

.. note::

      If you do not select “Hide Airspace above FL 100” the FIS frequencies for the Airspace C above FL100 will be displayed. In general this frequencies are also applicable below FL 100.

.. note::

      When Automatic flight detection is not selected the display will always be in flight mode.

.. note::

      If “Use English” is not selected the standard language selected for your device will be used if available.

Flight routes
-------------
Enroute Flight Navigation provides direct planning of one Route. A Route will remain present until it is cleared.
Route planning is entered via the Menu point Route. The Menu is entered via the Menu Symbol in the upper left corner of the map area. Then the Route Symbol has to be touched to go to the Route area.

A Route may be planned in the following ways:

* “Direct” in the waypoint window will provide a Route between current position and desired waypoint
* “to Route” in the waypoint window will add the waypoint to the last position of the Route.
* “Add Waypoint” in the Route window will open a selection window for a waypoint and add the selected waypoint to the route.

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
The following options are available from the Route Menu:

* Open a previously stored route from the library
* Save the current route to the library
* View the route library
* Import a Route from an external source
* Send the Route in JSON or GPX format
* Open the Route in another APP using the JSON or GPX format
* Clear Route
* Reverse Route

The previously created and stored routes will be kept in a data base within Enroute Flight Navigation. Routes consist of the data for the selected way points. The Route data may be exported for use in other applications.

**Route – Aircraft and Wind**

The Aircraft and Wind sub-page of the Route page allows to enter aircraft performance and wind data required for navigational calculations.
The Aircraft Data will be used to determine the distance of the flight and the true course.
The Wind data will will be used to calculate the true heading and duration of the flight. The duration of the flight will determine the fuel used.
Enroute Flight Navigation only offers a very superficial flight planning and cannot replace a full flight planning, but is only intended to provide quick reference.

Warning
Always perform a full flight preparation in accordance with the flight manual of the aircraft used. The use of Enroute Flight Navigation as primary flight planning may cause accidents leading to loss of lives. 

The Aircraft and Wind sub-page of the Route page offers the following input fields:

* Aircraft
    * Cruise Speed: Average Speed for Route
    * Descent Speed: Allows to enter a different speed for the descent phase (Currently not used)
    * Fuel Consumption: Average Fuel consumption per hour
* Wind
    * Direction in degrees
    * Speed in knots

Only one speed, fuel consumption and wind may be entered for the whole route.



