import xlsxwriter
from urlparse import urlparse

def gen_sheet(
    vendor_data,
    dimension_data,
    strategies_data,
    worksheet,
    missing_cell_format
    ):
    '''
    Create the placement worksheet.
    '''
    print "Generating Sheet: Placement"

    print vendor_data.keys()
    print dimension_data.keys()
    assert(set(vendor_data.keys()) == set(dimension_data.keys())), \
        "Dimension data does not match Vendor data"

    row_index = 2
    for vendor, market_tuple_array in vendor_data.items():
        for market_tuple in market_tuple_array:
            for dimension in dimension_data[vendor]:
                if (vendor in strategies_data.keys()):
                    for strategy in strategies_data[vendor]:
                        # URL Object
                        url_obj = urlparse(market_tuple[1])
                        # Publisher Name
                        worksheet.write('B' + str(row_index), vendor)
                        # Site Name
                        worksheet.write('C' + str(row_index), vendor)
                        # Placement Name
                        worksheet.write('D' + str(row_index), \
                            vendor+ '_' + market_tuple[0] + '_' + strategy + '_' + dimension)
                        # Width
                        worksheet.write('E' + str(row_index), \
                            int(dimension.split('_')[-1].split('x')[0]))
                        # Height
                        worksheet.write('F' + str(row_index), \
                            int(dimension.split('_')[-1].split('x')[1]))
                        # Placement Type
                        if (dimension.split('_')[-1] == '1x1'):
                            worksheet.write('G' + str(row_index), 'tracking')
                            is_display = False
                        else:
                            worksheet.write('G' + str(row_index), 'display')
                            is_display = True
                        # Cost Package
                        worksheet.write('I' + str(row_index), vendor+ '_' + market_tuple[0])
                        # Start Date, highlight if display
                        if (is_display):
                            worksheet.write('K' + str(row_index), '', missing_cell_format)
                        # End Date, highlight if display
                        if (is_display):
                            worksheet.write('L' + str(row_index), '', missing_cell_format)
                        # Custom Parameter Key 1
                        worksheet.write('O' + str(row_index), 'OMNITURE')
                        # Custom Parameter Value 1
                        if (market_tuple[1][:26] == 'http://www.livenation.com/'):
                            worksheet.write('P' + str(row_index), market_tuple[1][26:])
                        else:
                            worksheet.write('P' + str(row_index), '', missing_cell_format)
                        # Custom Parameter Key 2
                        worksheet.write('Q' + str(row_index), 'DOMAIN')
                        # Custom Parameter Value 2
                        if (url_obj.netloc == ''):
                            worksheet.write('R' + str(row_index), url_obj.netloc, missing_cell_format)
                        else:
                            worksheet.write('R' + str(row_index), url_obj.netloc)
                        row_index += 1

                else:
                    # URL Object
                    url_obj = urlparse(market_tuple[1])
                    # Publisher Name
                    worksheet.write('B' + str(row_index), vendor)
                    # Site Name
                    worksheet.write('C' + str(row_index), vendor)
                    # Placement Name
                    worksheet.write('D' + str(row_index), \
                        vendor+ '_' + market_tuple[0] + '_' + dimension)
                    # Width
                    worksheet.write('E' + str(row_index), \
                        int(dimension.split('_')[-1].split('x')[0]))
                    # Height
                    worksheet.write('F' + str(row_index), \
                        int(dimension.split('_')[-1].split('x')[1]))
                    # Placement Type
                    if (dimension.split('_')[-1] == '1x1'):
                        worksheet.write('G' + str(row_index), 'tracking')
                        is_display = False
                    else:
                        worksheet.write('G' + str(row_index), 'display')
                        is_display = True
                    # Cost Package
                    worksheet.write('I' + str(row_index), vendor+ '_' + market_tuple[0])
                    # Start Date, highlight if display
                    if (is_display):
                        worksheet.write('K' + str(row_index), '', missing_cell_format)
                    # End Date, highlight if display
                    if (is_display):
                        worksheet.write('L' + str(row_index), '', missing_cell_format)
                    # Custom Parameter Key
                    worksheet.write('O' + str(row_index), 'OMNITURE')
                    # Custom Parameter Value
                    if (market_tuple[1] != ''):
                        worksheet.write('P' + str(row_index), \
                            url_obj.path + url_obj.params + url_obj.query)
                    else:
                        worksheet.write('P' + str(row_index), '', missing_cell_format)
                    # Custom Parameter Key 2
                    worksheet.write('Q' + str(row_index), 'DOMAIN')
                    # Custom Parameter Value 2
                    if (url_obj.netloc == ''):
                        worksheet.write('R' + str(row_index), url_obj.netloc, missing_cell_format)
                    else:
                        worksheet.write('R' + str(row_index), url_obj.netloc)
                    row_index += 1

    return worksheet
