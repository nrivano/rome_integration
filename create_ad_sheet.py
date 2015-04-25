import xlsxwriter

def gen_sheet(vendor_data, worksheet):
    '''
    Create the package worksheet.
    '''
    print "Generating Sheet: Package"
    markets = set()
    for market_tuple_array in vendor_data.values():
        for market_tuple in market_tuple_array:
            markets.add(market_tuple[0])

    row_index = 2
    for market in markets:
        #print "Vendor: ", vendor
        #print "Market Tuple: ", str(market_tuple)
        worksheet.write('B' + str(row_index), market)
        worksheet.write('D' + str(row_index), 'LiveNation URL')
        row_index += 1

    return worksheet
