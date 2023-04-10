# python-read-write-sheet
A Python sample application that loads a sheet, updates selected cells, and saves the results

This is a minimal Smartsheet sample that demonstrates how to
* Import an XLSX file
* Load a sheet
* Loop through the rows
* Check for rows that meet a criteria
* Update cell values
* Write the results back to the original sheet


This sample scans a sheet for rows where the value of the "Status" column is "Complete" and sets the "Remaining"
column to zero.
This is implemented in the `evaluate_row_and_build_updates()` method which you should modify to meet your needs.


## Setup
Install the smartsheet Python SDK from [pypi](https://pypi.python.org/pypi/smartsheet-python-sdk)

- `pip install smartsheet-python-sdk --upgrade`

## Configure

- Set the system environment variable `SMARTSHEET_ACCESS_TOKEN` to the value of your token, obtained from the Smartsheet Account button, under Personal settings

## Build and run the application.
- `python python-read-write-sheet.py`

The rows marked "Complete" will have the "Remaining" value set to 0. (Note that you will have to refresh in the desktop application to see the changes.)

A log file named `rwsheet.log` will accumulate information about API calls.

## See also
- http://smartsheet-platform.github.io/api-docs/
- https://github.com/smartsheet-platform/smartsheet-python-sdk
- https://www.smartsheet.com/
