import logging
# import pickle
import pandas as pd
import numpy as np

# import re
import os.path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper Functions

# def get_name():
#     print(__name__)


def convert_index_to_dict(string_list):
    dct = dict()
    for s in string_list:
        res = s[s.find("(")+1:s.find(")")]
        a = int(res)
        t = s[:s.find(" (")]
        dct[a] = str(t)
    return dct


# ### Converting to Age Group into bagging
#
# see this page:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html

age_list_bagging = {
    'unknown'  : 0,
    '0 to 4'   : 1,
    '5 to 9'   : 2,
    '10 to 14' : 3,
    '15 to 19' : 4,
    '20 to 24' : 5,
    '25 to 29' : 6,
    '30 to 34' : 7,
    '35 to 39' : 8,
    '40 to 44' : 9,
    '45 to 49' : 10,
    '50 to 54' : 11,
    '55 to 59' : 12,
    '60 to 64' : 13,
    '65 to 69' : 14,
    '70 to 74' : 15,
    '75 to 79' : 16,
    '80 to 84' : 17,
    '85 to 89' : 18,
    '90 to 94' : 19,
    'Over 95'  : 20
}


class KSIData:
    '''
        Killed or Seriously Injured Dataset
    '''
    def __init__(self):
        self.df = None
        self.hood_dict = None
        self.age_list_bagging = age_list_bagging
        self.age_list_index = {value: key for (key, value) in age_list_bagging.items()}
        logger.info('loading csv data...')
        self.load_ksi_data()
        self.clean_ksi_data()
        logger.info('finish loading data')

    def load_ksi_data(self):
        mypath = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(mypath, '../data/pedestrian/Pedestrians.csv')
        self.df = pd.read_csv(path)

    def clean_ksi_data(self):
        # FIXING DATE
        self.df['MY_DATE'] = pd.to_datetime(
            self.df['DATE'],
            errors='coerce',
            format='%Y/%m/%d'
        ).dt.date

        # FIXING HOUR
        self.df['MY_HOUR'] = self.df['HOUR'].map('{:02d}'.format)

        # FIXING MINUTE
        self.df['MY_MIN'] = self.df['TIME'] - (self.df['HOUR'] * 100)

        # THERE ARE ABOUT 130 ROWS WITH MINUTE PROBLEM, AFTER THE ABOVE
        # CONVERSION
        # we will just change minute data to "0"
        # wrong
        mask = self.df['MY_MIN'] < 0
        self.df.loc[mask, 'MY_MIN'] = 0

        self.df['DATE_TIME'] = pd.to_datetime(self.df['MY_DATE'].apply(lambda x: x.strftime('%Y-%m-%d')) + ' ' + self.df['MY_HOUR'].astype(str) + ':' + self.df['MY_MIN'].astype(str))
        # self.df['DATE_TIME']

        self.df['DATE'] = pd.to_datetime(self.df['DATE'], errors='coerce', format='%Y/%m/%d')

        self.df = self.df.drop(['MY_DATE', 'MY_HOUR', 'MY_MIN'], axis=1)
        self.df.set_index('DATE_TIME', inplace=True)
        self.df.sort_index()

        # location_class_list = ['ROAD_CLASS', 'LOCCOORD', 'ACCLOC', 'TRAFFCTL']
        # road_conditions_list = ['VISIBILITY', 'LIGHT', 'RDSFCOND']
        # accident_class_list = ['ACCLASS', 'IMPACTYPE']

        # IMPACTYPE has no significant value, we will remove it.
        # accident_class_list.remove('IMPACTYPE')

        # involvement_class_list = ['INVTYPE', 'INVAGE', 'INJURY', 'FATAL_NO']

        # vehicle_related_list = ['INITDIR', 'VEHTYPE', 'MANOEUVER', 'DRIVACT', 'DRIVCOND']

        # pedestrian_related_list = ['PEDTYPE', 'PEDACT', 'PEDCOND']

        # cyclist_related_list = ['CYCLISTYPE', 'CYCACT', 'CYCCOND']

        # parties_involved_list = ['CYCLIST', 'AUTOMOBILE', 'MOTORCYCLE', 'TRUCK', 'TRSN_CITY_VEH', 'EMERG_VEH', 'PASSENGER']

        # driving_behaviors_list = ['SPEEDING', 'AG_DRIV', 'REDLIGHT', 'ALCOHOL', 'DISABILITY']

        # police_control_list = ['WardNum', 'Division', 'Hood_ID', 'Neighbourhood']

        columns_to_delete1 = ['X', 'Y', 'ObjectId']
        self.df = self.df.drop(columns_to_delete1, axis=1)
        columns_to_delete2 = ['IMPACTYPE']
        self.df = self.df.drop(columns_to_delete2, axis=1)

        def convert_to_bool_type(columns):
            for i in columns:
                # df['CYCLIST'] = np.where(df['CYCLIST'] == 'Yes', True, False)
                self.df[i] = np.where(self.df[i] == 'Yes', True, False)

        columns_obj_to_boolean = ['PEDESTRIAN', 'CYCLIST', 'AUTOMOBILE', 'MOTORCYCLE', 'TRUCK', 'TRSN_CITY_VEH', 'EMERG_VEH', 'PASSENGER', 'SPEEDING', 'AG_DRIV', 'REDLIGHT', 'ALCOHOL', 'DISABILITY']
        convert_to_bool_type(columns_obj_to_boolean)

        self.df['ACCLASS'] = np.where(self.df['ACCLASS'] == 'Fatal', True, False)


        # how to convert cat to num
        # https://stackoverflow.com/questions/38088652/pandas-convert-categories-to-numbers

        columns_obj_to_cat1 = ['District', 'WardNum']
        columns_obj_to_cat2 = ['ROAD_CLASS', 'LOCCOORD', 'ACCLOC', 'TRAFFCTL']
        columns_obj_to_cat3 = ['VISIBILITY', 'LIGHT', 'RDSFCOND']
        columns_obj_to_cat4 = ['INVTYPE', 'INJURY']
        columns_obj_to_cat5 = ['INITDIR', 'VEHTYPE', 'MANOEUVER', 'DRIVACT', 'DRIVCOND']
        columns_obj_to_cat6 = ['PEDTYPE', 'PEDACT', 'PEDCOND', 'CYCLISTYPE', 'CYCACT', 'CYCCOND']

        li_cat_cols = [columns_obj_to_cat1, columns_obj_to_cat2, columns_obj_to_cat3, columns_obj_to_cat4, columns_obj_to_cat5, columns_obj_to_cat6]

        for i in li_cat_cols:
            for j in i:
                name_mod = j + '_cc'
                self.df[j] = pd.Categorical(self.df[j])
                self.df[name_mod] = self.df[j].cat.codes
                # df[name_mod] = df[j].astype('category').cat.codes

        self.df['INVAGE_cc'] = self.df['INVAGE'].map(age_list_bagging)

        self.df['ACCNUM'] = pd.Categorical(self.df['ACCNUM'])
        self.df['YEAR'] = pd.Categorical(self.df['YEAR'])
        self.df['HOUR'] = pd.Categorical(self.df['HOUR'])

        # listing all those categories definitions
        # for i in li_cat_cols:
        #     for j in i:
        #         a = dict( enumerate(df[j].cat.categories ) )
        #         print("\nDictionary for Column: ", j)
        #         print(a)

        # ## Intersection Name
        # Merging Street 1 and Street 2 so it make sense

        # Problem:
        # when combining 2 columns in to 1 i.e. (df['STREET'] = df['STREET1'] + ' & ' + df['STREET2']), you get different results.
        #
        # DUNDAS ST W & BLOOR ST W  -> 5 cases and
        # BLOOR ST W & DUNDAS ST W  -> 5 (another 5 )
        #
        # where this should be consider 10 cases in total. We have to remap those Street into one entity.
        #
        # This code does not work
        # df['STREET'] = df['STREET1'] + ' & ' + df['STREET2']
        # cases_per_intersection = df.groupby(df['STREET'])['ACCNUM'].nunique().sort_values(ascending=False)
        # cases_per_intersection
        #
        # see this as an example:
        #
        # https://stackoverflow.com/questions/60313006/mapping-of-multiple-columns-categorical-values-in-pandas

        self.df['STREET1_MOD'] = self.df['STREET1'].str.upper()
        self.df['STREET2_MOD'] = self.df['STREET2'].str.upper()
        stacked = self.df[['STREET1_MOD', 'STREET2_MOD']].stack()

        codes, uniques = pd.factorize(stacked, sort=True)
        # print('codes: ', codes)
        # print('uniques:', uniques)

        self.df['STREET1_MOD'] = pd.Categorical(self.df['STREET1_MOD'], categories=uniques)
        self.df['STREET2_MOD'] = pd.Categorical(self.df['STREET2_MOD'], categories=uniques)
        self.df['STREET1_cc'] = self.df['STREET1_MOD'].cat.codes
        self.df['STREET2_cc'] = self.df['STREET2_MOD'].cat.codes
        self.df['STREET12'] = self.df['STREET1'] + ' & ' + self.df['STREET2']

        # So, now we have unique numbers for the street's identifiers, we can combine their codes by union them together. Since AB = BA (commutative), we will multiple the two integers together.
        self.df['STREET_U'] = self.df['STREET1_cc'].astype(int) * self.df['STREET2_cc'].astype(int)

        hood_series = self.df['Neighbourhood'].unique()
        hood_series[hood_series == 'Mimico (includes Humber Bay Shores) (17)'] = 'Mimico includes Humber Bay Shores (17)'
        hood_list = hood_series.tolist()
        self.hood_dict = convert_index_to_dict(hood_list)

    def get_hood_dict(self, id):
        # hood_dict[97]
        return self.hood_dict[id]

    def get_intersection_name(self, val):
        filter = self.df['STREET_U'] == val
        a = self.df[filter]
        st = a.iloc[0]['STREET12']
        return str(st)
        # this is how you use to map STREET_U code back to intersection name
        # ```
        # df['INTERSECTION_NAME'] = df.STREET_U.apply(lambda x: get_intersection_name(x))
        # ```
        # ## Neighbourhood Dictionary
        # #### Obtain a dictionary type for neighbourhood name
        # where you get key, value pair for neighbourhood {id: name}

    def get_total_cases(self):
        return self.df['ACCNUM'].nunique()
