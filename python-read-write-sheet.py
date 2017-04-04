# Install smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet

# TODO: Set your API access token here, or leave as None and set as environment variable "SMARTSHEET_ACCESS_TOKEN"
access_token = None

# TODO: Update this with the ID of your sheet to update
sheet_id = 3948180799809412

# The API identifies columns by Id, but it's more convenient to refer to column names. Store a map here
column_map = {}

# Helper function to find cell in a row
def get_cell_by_column_name(row, column_ame):
    column_id = column_map[column_ame]
    return row.get_column(column_id)


# TODO: Replace the body of this function with your code
# This *example* looks for rows with a "Status" column marked "Complete" and sets the "Remaining" column to zero
#
# Return a new Row with updated cell values, else None to leave unchanged
def evaluate_row_and_build_updates(source_row):
    # Find the cell and value we want to evaluate
    status_cell = get_cell_by_column_name(source_row, "Status")
    status_value = status_cell.display_value
    if (status_value == "Complete"):
        remaining_cell = get_cell_by_column_name(source_row, "Remaining")
        if (remaining_cell.display_value != "0"):                           # Skip if already 0
            print("Need to update row #" + str(source_row.row_number))

            # Build new cell value
            newCell = ss.models.Cell()
            newCell.column_id = column_map["Remaining"]
            newCell.value = "0"
            # Set strict to false to allow the API to parse the string "0" as a number
            newCell.strict = False

            # Build the row to update
            newRow = ss.models.Row()
            newRow.id = source_row.id
            newRow.cells.append(newCell)

            return newRow

    return None



print("Starting ...")

# Initialize client
ss = smartsheet.Smartsheet(access_token)
# Make sure we don't miss any error
ss.errors_as_exceptions(True)

# Load entire sheet
sheet = ss.Sheets.get_sheet(sheet_id)

print ("Loaded " + str(len(sheet.rows)) + " rows from sheet: " + sheet.name)

# Build column map for later reference - translates column names to column id
for column in sheet.columns:
    column_map[column.title] = column.id

# Accumulate rows needing update here
rowsToUpdate = []

for row in sheet.rows:
    rowToUpdate = evaluate_row_and_build_updates(row)
    if (rowToUpdate != None):
        rowsToUpdate.append(rowToUpdate)

# Finally, write updated cells back to Smartsheet
print("Writing " + str(len(rowsToUpdate)) + " rows back to sheet id " + str(sheet.id))
result = ss.Sheets.update_rows(sheet_id, rowsToUpdate)
print ("Done")




