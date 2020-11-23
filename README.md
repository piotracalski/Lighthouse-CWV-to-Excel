# Lighthouse TTI -> Excel
This is a script that automatically transfers Lighthouse report data to Excel. At this moment below data is transfered:
Report name, Time of execution, Time to interactive

## Prerequisites
### Python 3.x
At the moment of writing this script my version of Python was: 3.7.4

### xlwt Python library
`pip install xlwt`

### Lighthouse reports
All Lightouse reports should be in *reports* folder next to *main.py* script file. If you want to scan reports from different location you need to change *directory* parameter in line 51 of *main.py* file.
Note: Lighthouse naming convention is relevant to version 6.4.1

## Execute script
From the root folder:
`python main.py`