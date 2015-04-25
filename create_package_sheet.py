import xlsxwriter

def gen_sheet(vendor_data, worksheet):
    '''
    Create the package worksheet.
    '''
    print "Generating Sheet: Package"
    row_index = 2
    for vendor, market_tuple_array in vendor_data.items():
        for market_tuple in market_tuple_array:
            #print "Vendor: ", vendor
            #print "Market Tuple: ", str(market_tuple)
            worksheet.write('B' + str(row_index), vendor+ '_' + market_tuple[0])
            worksheet.write('C' + str(row_index), vendor)
            worksheet.write('D' + str(row_index), 'CPM')
            row_index += 1

    return worksheet
