ID = 'id'
ID_DISPLAY = 'ID'
FIELD = 'field'
FIELD_DISPLAY = 'Field'
CCD = 'ccd'
CCD_DISPLAY = 'CCD'
MARY_RUN = 'mary_run'
MARY_RUN_DISPLAY = 'Mary Run'
DATE = 'date'
DATE_DISPLAY = 'Date'
CAND_NUM = 'cand_num'
CAND_NUM_DISPLAY = 'Cand Num'
MAG = 'mag'
MAG_DISPLAY = 'mag'
EMAG = 'emag'
EMAG_DISPLAY = 'emag'
MJD = 'mjd'
MJD_DISPLAY = 'mjd'
RA = 'ra'
RA_DISPLAY = 'RA'
DEC = 'dec'
DEC_DISPLAY = 'Dec'
MARY_ID = 'maryID'
MARY_ID_DISPLAY = 'Mary ID'
SCI_PATH = 'sci_path'
SCI_PATH_DISPLAY = 'sci_path'
SUB_PATH = 'sub_path'
SUB_PATH_DISPLAY = 'sub_path'
TEMP_PATH = 'temp_path'
TEMP_PATH_DISPLAY = 'temp_path'

SEARCH_DISPLAY_HEADERS = dict()

SEARCH_DISPLAY_HEADERS.update({
    ID: ID_DISPLAY,
    FIELD: FIELD_DISPLAY,
    CCD: CCD_DISPLAY,
    MARY_RUN: MARY_RUN_DISPLAY,
    DATE: DATE_DISPLAY,
    CAND_NUM: CAND_NUM_DISPLAY,
    MAG: MAG_DISPLAY,
    EMAG: EMAG_DISPLAY,
    MJD: MJD_DISPLAY,
    RA: RA_DISPLAY,
    DEC: DEC_DISPLAY,
    MARY_ID: MARY_ID_DISPLAY,
    SCI_PATH: SCI_PATH_DISPLAY,
    SUB_PATH: SUB_PATH_DISPLAY,
    TEMP_PATH: TEMP_PATH_DISPLAY,
})

ADMIN_SEARCH_COLUMNS = [
    ID,
    FIELD,
    CCD,
    MARY_RUN,
    DATE,
    CAND_NUM,
    MAG,
    EMAG,
    MJD,
    RA,
    DEC,
    # MARY_ID,
    # SCI_PATH,
    # SUB_PATH,
    # TEMP_PATH,
]

COLLABORATOR_SEARCH_COLUMNS = [
    ID,
    FIELD,
    CCD,
    MARY_RUN,
    DATE,
    CAND_NUM,
    MAG,
    EMAG,
    MJD,
    RA,
    DEC,
    MARY_ID,
    SCI_PATH,
    SUB_PATH,
    TEMP_PATH,
]

PUBLIC_SEARCH_COLUMNS = [
    ID,
    FIELD,
    CCD,
    MARY_RUN,
    DATE,
    CAND_NUM,
    MAG,
    EMAG,
    MJD,
    RA,
    DEC,
    MARY_ID,
]
