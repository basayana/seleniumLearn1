import pandas as pd
from typing import List, Dict

def get_credentials_from_excel(filepath: str, sheet_name: str = None) -> List[Dict[str, str]]:
    """
    Reads user credentials from an Excel file and returns a list of dictionaries.
    Each dictionary contains keys like 'userid' and 'password'.
    :param filepath: Path to the Excel file.
    :param sheet_name: Sheet name to read from. If None, reads the first sheet.
    :return: List of dictionaries with credentials.
    """
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    # Normalize column names to lower for consistency
    df.columns = [col.lower() for col in df.columns]
    # Expect columns like 'userid' and 'password' (case-insensitive)
    required_cols = {'userid', 'password'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Excel must contain columns: {required_cols}")
    return df[list(required_cols)].to_dict(orient='records')

def get_employee_details_from_excel(filepath: str, sheet_name: str = None) -> List[Dict[str, str]]:
    """
    Reads employee details from an Excel file and returns a list of dictionaries.
    Each dictionary contains keys like 'firstname', 'middlename', 'lastname'.
    :param filepath: Path to the Excel file.
    :param sheet_name: Sheet name to read from. If None, reads the first sheet.
    :return: List of dictionaries with employee details.
    """
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    # Normalize column names to lower for consistency
    df.columns = [col.lower() for col in df.columns]
    required_cols = {'firstname', 'middlename', 'lastname'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Excel must contain columns: {required_cols}")
    return df[list(required_cols)].to_dict(orient='records')
