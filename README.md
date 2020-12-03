# Lighthouse Core Web Vitals -> Excel
This is a script that automatically transfers Lighthouse report data to Excel. At this moment below data is transfered:
Requested URL, Fetch time, Largest Contentful Paint, Total Blocking Time, Cumulative Layout Shift. 
Note: First Input Delay metric is measurable only in RUM (real user monitoring) and therefore it was replaced by TBT.

## Prerequisites
### Python 3.x
At the moment of writing this script my version of Python was: 3.7.4

### xlwt Python library
```
pip install xlwt
```

### Lighthouse reports
All Lightouse reports should be in *reports* folder next to *main.py* script file. If you want to scan reports from different location you need to edit *reports_directory* key value in *env_data.json* file.
Note: This script is relevant to Lighthouse version 6.4.1. Script requires reports to be **JSON files**.

### Lighthouse metrics
All metrics should be listed within *metrics* key in *env_data.json* file in proper format:
```
{
  "label": "metrics-label",
  "report_key": "metrics-report-key",
  "unit": "metrics-unit"
}
```

## Execute script
From the root folder:
```
python main.py
```

## Results
Results are stored in *core_web_vitals.xls* file in the root folder.