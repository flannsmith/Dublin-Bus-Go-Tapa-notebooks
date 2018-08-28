#A set of tools for analyzing dublin bus data

## An implementation of a time dependant graph on the Dublin Bus network. 

Includes:
* route_tools -> functions for splitting dublin bus data
* scripts -> more functions for splitting bus data, and processing gtfs data
* resources -> Plenty of pickles and dictionaries, derived from gtfs data
* stop_tools -> the stop_getter (distance and shape retrieval) and stop_finder (find closest stops to given coordinates) classes, as well as some functions for retrieving and preprocessing data
* classes -> contains stop objects, route selector objects, and also contains the time_tabler classes (generate bus departure times,and store and retrieve timetables in an accessible format).
* network -> contains the network class that acts as a container for stops, as well as running routefinding algorithms and retrieving information about the dublin bus network.


The principal files used in our app are:
* final_notebooks - The notebooks from which our report is derived. The comparisons of models on individual routes are in the "chained model comparisons" and "whole route model comparisons", and "chained_models_without_upper_quantile" folders.
* notebooks - Many other notebooks created over the course of the project. Not intended for presentation.
* dbanalysis/network/simple_network4.py - The final implementation of the network object.
* dbanalysis/classes/neural_stop.py - The final implementation of the stop object
* dbanalysis/classes/time_tabler_refac2.py - The final implementation of both the stop time table object, and the departure times time table object.
* dbanalysis/classes/route_selector.py - The final implementation of the route selection object
* dbanalysis/stop_tools.py - The final implementation of both the stop finder, and stop getter objects, as well as the functions used for retrieving stop-link data.  
* dbanalysis/models/build_neural_models.py The script used to actually build all of the stop link models. Also contains the BRM.py model class that was used as a holder for whole route models.
* dbanalysis/route_tools.py Contains the get_munged_route_data function that was used to split route files into individual stop link files.
* dbanalysis/scripts Contains many scripts that were used throughout the process.
* dbanalysis/resources - Contains the models

## Running the tests

To run our suite of tests move into the directory "/dbanalysis/tests" and run:
```
python test.py
```
```
```

You will have to open an ssh tunnel to our database in order to connect and properly run the tests.
