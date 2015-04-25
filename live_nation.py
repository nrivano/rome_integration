from enum import Enum

WORKBOOK_NAME = 'LiveNationTemplates.xlsx'
ROME_FILE = 'rome_sheet.csv'
DIMENSION_FILE = 'dimensions.csv'
STRATEGIES_FILE = 'strategies.csv'
HEADERS = ['Vendor', '', 'Offer #', 'Market', '', 'Event Name', '', '', 'Event Date', \
    'AdPlan #', 'Ad Plan Name', '', 'Marketer ', 'Rate', '', '', 'Tracking']
ROME_TO_ATLAS_VENDOR_DICT = {
    'DataXu': 'DataXu Inc.',
    'Tubemogul': 'TubeMogul',
}

class WorksheetNames (Enum):
    PACKAGE = 'Package Import'
    PLACEMENT = 'Placement Import'
    AD = 'Ad Import'
    TRACKING_PIXEL = 'Tracking Pixel Import'
    ASSIGNMENT = 'Assignment Import'

class WorksheetHeaders (Enum):
    PACKAGE = [
        'Package ID',
        'Package Name',
        'Publisher Name',
        'Cost Type',
        'Action Name',
        'Is Capped',
        'Start Date',
        'End Date',
        'Time Zone',
        'Rate',
        'Quantity',
        'Total Cost',
        'Custom Parameter Key',
        'Custom Parameter Value',
        'Import Action',
    ]
    PLACEMENT = [
        'Placement ID',
        'Publisher Name',
        'Site Name',
        'Placement Name',
        'Width',
        'Height',
        'Placement Type',
        'Tracking Partner Name',
        'Cost Package Name',
        'Alternate Placement ID',
        'Start Date',
        'End Date',
        'Time Zone',
        'COPPA Placement',
        'Custom Parameter Key',
        'Custom Parameter Value',
        'Additional Code',
        'Import Action',
    ]
    AD = [
        'Ad ID',
        'Ad Name',
        'Creative Concept Name',
        'Click-Through Name',
        'Start Date',
        'End Date',
        'Time Zone',
        'Custom Parameter Key',
        'Custom Parameter Value',
        'Import Action',
    ]
    TRACKING_PIXEL = []
    ASSIGNMENT = []
