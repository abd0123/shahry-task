from datetime import datetime

from utils.enums import Gender

CODE_TO_GOVERNERATE = {
    '01': 'Cairo',
    '02': 'Alexandria',
    '03': 'Port Said',
    '04': 'Suez',
    '11': 'Damietta',
    '12': 'Dakahlia',
    '13': 'Ash Sharqia',
    '14': 'Kaliobeya',
    '15': 'Kafr El Sheikh',
    '16': 'Gharbia',
    '17': 'Monufia',
    '18': 'El Beheira',
    '19': 'Ismailia',
    '21': 'Giza',
    '22': 'Beni Suef',
    '23': 'Fayoum',
    '24': 'El Menia',
    '25': 'Assiut',
    '26': 'Sohag',
    '27': 'Qena',
    '28': 'Aswan',
    '29': 'Luxor',
    '31': 'Red Sea',
    '32': 'New Valley',
    '33': 'Matrouh',
    '34': 'North Sinai',
    '35': 'South Sinai',
    '88': 'Foreign Country',
}

def extract_birth_date(nid: str):
    """extracts the birth date from the national id number with the follwoing consideration:
        1- first digit is the century 2 -> (1901 - 1999)
        2- second and third digits are the year of birth
        3- fourth and fifth digits are the month of birth
        4- sixth and seventh digits are the day of birth

    Args:
        nid (str): national id number

    Returns:
        _type_: 
    Raises:
        ValueError: if birth date is not valid
    """
    century = int(nid[0])
    year_digits = int(nid[1:3])
    year = 1700 + (century * 100) + year_digits
    month = int(nid[3:5])
    day = int(nid[5:7])
    # datetime handles validation on month and day 1..12 1..31 also leap years
    date = datetime(year, month, day)
    birth_date = date.strftime("%Y-%m-%d")
    if(datetime.now() < date):
        raise ValueError(f"Birth date is not valid: {birth_date} is in the future")
    return birth_date


def extract_birth_governerate(nid: str):
    """extracts the birth governerate from the national id number
        1- eighth and ninth digits are the birth governerate code

    Args:
        nid (str): national id number
    
    Returns:
        _type_: str
    Raises:
        ValueError: if governerate code is not valid
    """
    birth_governerate_code = nid[7:9]
    
    if (birth_governerate_code in CODE_TO_GOVERNERATE.keys()):
        return CODE_TO_GOVERNERATE[str(birth_governerate_code)]
    else:
        raise ValueError(f"Birth governerate code is not valid: {birth_governerate_code}")

def extract_birth_date_serial(nid: str):
    """extracts unique serial for the birth date from the national id number
        1- tenth, eleventh, twelfth, and Thirteenth digits are the birth date serial

    Args:
        nid (str): _description_
    Returns:
        _type_: str
    """
    return nid[9:13]

def extract_gender(nid: str):
    """extracts the gender from the national id number
        1- thirteenth digit signifies the gender:
            if it is even then Female
            if it is odd then Male

    Args:
        nid (str): national id number
    
    Returns:
        _type_: str
    
    Raises:
        ValueError if the digit is 0
    """
    gender_digit = int(nid[12])
    if gender_digit == 0:
        raise ValueError("Gender digit is not valid: 0")
    
    if gender_digit % 2 == 0:
        return Gender.FEMALE.value
    else:
        return Gender.MALE.value
    