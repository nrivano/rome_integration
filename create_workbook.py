import create_ad_sheet
import create_package_sheet
import create_placement_sheet
import live_nation
import load_files
import sys
import xlsxwriter

def create_excel_sheet(workbook_name):
    '''
    Takes an array of names and creates a workbook
    with a sheet for each name in array.
    '''
    print "Generating Workbook:", workbook_name
    workbook = xlsxwriter.Workbook(workbook_name)
    for sheet_name in live_nation.WorksheetNames:
        print "Adding sheet:", sheet_name.value
        workbook.add_worksheet(sheet_name.value)

    return workbook

def create_import_headers(workbook):
    '''
    Create the headersfor each sheet in the workbook passed.
    '''
    print "Generating Headers"
    for worksheet in workbook.worksheets():
        if worksheet.get_name() == live_nation.WorksheetNames.PLACEMENT.value:
            print "Generating Headers: Placment"
            worksheet.write_row('A1', live_nation.WorksheetHeaders.PLACEMENT.value)
        elif worksheet.get_name() == live_nation.WorksheetNames.PACKAGE.value:
            print "Generating Headers: Package"
            worksheet.write_row('A1', live_nation.WorksheetHeaders.PACKAGE.value)
        elif worksheet.get_name() == live_nation.WorksheetNames.AD.value:
            print "Generating Headers: Ad"
            worksheet.write_row('A1', live_nation.WorksheetHeaders.AD.value)
        elif worksheet.get_name() == live_nation.WorksheetNames.TRACKING_PIXEL.value:
            print "Generating Headers: Tracking Pixel"
        elif worksheet.get_name() == live_nation.WorksheetNames.ASSIGNMENT.value:
            print "Generating Headers: Assignment"
        else:
            print "No Available Sheets"

def main():
    '''
    Load all the files, create the templates, and load the data in.
    '''
    try:
      # open file stream
      workbook = create_excel_sheet(live_nation.WORKBOOK_NAME)
      missing_cell_format = workbook.add_format()
      missing_cell_format.set_bg_color('yellow')
    except:
      print "There was an error creating a workbook."
      sys.exit()

    # load all the files
    vendor_data = load_files.gen_vendor_dict()
    dimension_data = load_files.gen_file_dict(live_nation.DIMENSION_FILE)
    strategies_data = load_files.gen_file_dict(live_nation.STRATEGIES_FILE)

    # add in the headers to the worksheets
    create_import_headers(workbook)

    # add in the data for each worksheet
    print "Generating Sheets"
    for worksheet in workbook.worksheets():
        if worksheet.get_name() == live_nation.WorksheetNames.PACKAGE.value:
            package_sheet = \
                create_package_sheet.gen_sheet(
                    vendor_data,
                    worksheet
                )
        if worksheet.get_name() == live_nation.WorksheetNames.PLACEMENT.value:
            create_placement_sheet.gen_sheet(
                vendor_data,
                dimension_data,
                strategies_data,
                worksheet,
                missing_cell_format
            )
        if worksheet.get_name() == live_nation.WorksheetNames.AD.value:
            create_ad_sheet.gen_sheet(
                vendor_data,
                worksheet
            )

    package_sheet.activate()

    workbook.close()


main()
