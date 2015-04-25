import sys
import live_nation
import csv

def gen_vendor_dict():
    '''
    Load the CSV file from Rome into a vendor to market_tuple
    where market_tuple is a tuple of market and tracking URL
    from Rome.
    '''
    vendor_dict = {}
    with open(live_nation.ROME_FILE) as csvfile:
        reader = csv.reader(csvfile)

        row_index = 0
        for row in reader:
            if row_index == 0:
                assert (row == live_nation.HEADERS), "Headers do not match."
                row_index += 1
                continue
            if (row[0] != '' and row_index != 0):
                vendor = row[0]
                vendor_dict[vendor] = []
            map_markets_to_vendor(vendor_dict, row, vendor)

    csvfile.close()

    # filter out the empty vendors and map to Atlas naming conventions
    filtered_vendor_dict = dict((k, v) for k, v in vendor_dict.iteritems() if v)
    atlas_filtered_vendor_dict = \
        map_rome_to_atlas_vendor_names(filtered_vendor_dict)

    return atlas_filtered_vendor_dict

def gen_file_dict(filename):
    '''
    Load the CSV file for dimensions into a vendor to
    dimensions dictionary.
    '''
    file_dict = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)

        headers = next(reader)
        for index in range(0, len(headers)):
            file_dict[headers[index]] = []

        for row in reader:
            for index in range(0, len(row)):
                if (row[index] != ''):
                    file_dict[headers[index]].append(row[index])

    csvfile.close()
    filtered_file_dict = dict((k, v) for k, v in file_dict.iteritems() if v)
    return filtered_file_dict

def map_markets_to_vendor(vendor_dict, current_row, vendor):
    '''
    Takes a file that is being read and creates an entry for
    a vendor with an array of markets. This is where I'll hold all
    the custom rules for filtering out rows that LiveNation deems
    unnecessary.
    '''
    # Load vendor name and current market/URL tuple of current_row
    # Do some checks for no Google or Facebook  media other than PAP
    if (not (
        vendor == 'Google' or
        vendor == 'Twitter' or
        (vendor == 'Facebook' and ('_PAP_' not in current_row[16])) or
        '_O_' in current_row[16]
        )
    ):
        market_tuple = (current_row[3], current_row[16])
        vendor_dict[vendor].append(market_tuple)

def map_rome_to_atlas_vendor_names(vendor_dict):
    '''
    Rome has different naming conventions than Atlas.
    We need to hold a map of these differences and update
    the vendor_dict to the Atlas name so we can import it.
    '''
    for key in vendor_dict.keys():
        if key in live_nation.ROME_TO_ATLAS_VENDOR_DICT.keys():
            vendor_dict[live_nation.ROME_TO_ATLAS_VENDOR_DICT[key]] = \
                vendor_dict.pop(key)

    return vendor_dict


