from Library_Used import *

#HÀM ĐỌC DỮ LIỆU TỪ FILE
def read_from_file(filepath: str, how : str):
    """
    Reads a file based on the specified method.

    Parameters:
        filepath (str): The path to the file to read.
        how (str): The method to read the file.
            - 'r_b_str': Read the entire file as a single string. Recommended for HTML files.
            - 'r_b_line': Read the file line-by-line, returning a list of lines. Recommended for TXT files.

    Returns:
        Union[str, List[str]]: 
            - If `how` is 'r_b_str', returns the file content as a single string.
            - If `how` is 'r_b_line', returns the file content as a list of lines.

    Raises:
        ValueError: If `how` is not one of the supported values.
    """
    with open(filepath, 'r', encoding="utf-8") as file:
        try :
            if how == 'r_b_str':
                content = ''
                content = file.read()
                return content
            elif how == 'r_b_line':
                content = []
                content = file.read().splitlines()  
                return content
        except Exception as err:
            print(f'{how} is not one of the supported values.')
