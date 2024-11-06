from Libraries_Used import *

def write_to_file(filepath: str, content , how : str):
    """
    Writes content to a file based on the specified method.

    Parameters:
        filepath (str): The path to the file to write to.
        content (str or list): The content to write to the file. 
            - If `how` is 'w_b_str', content should be a string.
            - If `how` is 'w_b_element', content should be a list.
        how (str): The method to write the content.
            - 'w_b_str': Write the entire content as a single string, suitable for HTML files.
            - 'w_b_element': Write each element of the list on a new line, suitable for TXT files.

    Returns:
        None: This function does not return anything.
    """
    with open(filepath, 'w', encoding="utf-8") as file:
        try:
            if how == 'w_b_str':
                file.write(content)
            elif how == 'w_b_element':
                for line in content: 
                    file.write(str(line) + '\n')
        except Exception as err:
            print(f'{how} is not one of the supported values.')

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
    