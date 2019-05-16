## ETL Architecture Project Questionnaire

### Project Data Points
1. Across all reservation partners for January & February, how many completed reservations occurred? 28


2. Which studio has the highest rate of reservation abandonement (did not cancel but did not check-in)?
hive-athletics	3
crossfit-control-jacksonville-beach	3
orlando-yoga	3

3. Which fitness area (i.e., tag) has the highest number of completed reservations for February
yoga	10
strength	10

4. How many members completed at least 1 reservation and had no more than 1 canceled reservation in January?
	25

### Project Discussion
1. Describe what custom logic you chose to implement in your ETL solution and why?
The main custom logic was the cleaning of the data.  It is customized to the data issues seen in the supplied files.  Also the loading of the data to help take advantage of the database checks was able to take advantage of that when loading the dimension type tables vs the fact type tables.

2. What forecasting opportunities do you see with a dataset like this and why? Could see trends in what studios could be increasing or decreasing reservations over time.  To be able to reward better studios or help struggling studios.   Also which may have higher cancellation rates then others to find problem areas.  Also some sort of recommendations for members to help find classes they may like but are not attending.  

3. What other data would you propose we gather to make reporting/forecasting more robust and why?  Need more member info.  Specially to show if members from certain employers could be utilizing the benefits.  Could be used to help getting higher utilization rates.

4. What was difficult and how might you have approached that obstacle differently next time? Just how some of the data related and how much needs to be complete to be effective.  Need more of an all-around understanding on what the data represents.
