import random as rand

def test_input(message):
    """Takes a message and ask the user to enter the appropriate response based on the message. 

    Args:
        message (str): takes the string message to instruct user what to input.

    Returns:
        str: returns the user's input to the program.
    """ 
    return input(message)

def is_integer(number):
    """Takes a string that contains a number and checks if it is a positive integer. 

    Args:
        number (str): string containing a number that will be checked.

    Returns:
        bool: returns whether or not the number is an integer.
    """
    try:
        x = int(number)
        return True and x >=0 and number.count(".") == 0
    except ValueError:
        return False

def return_encoder_number(encoder):
    """returns a string representation of the encoder number that will be appended to an encoded string.

    Args:
        encoder (int): an int number that will be converted to its string representation.

    Returns:
        str: the string representation of number.
    """
    if encoder < 10 and encoder >= 0:
        return "0"+str(encoder)
    else:
        return str(encoder)

def encode(original, encoding_list, encoding, start_message):
    """Encodes a message provided by the user.

    Args:
        original ([str]): contains the original list.
        encoding_list ([str]): contains the list that message will be converted to. 
        encoding (int): the key number of the list that was used.
        start_message (str): the message provided by the user. 

    Returns:
        str: returns the encoded message to the user.
    """
    message = ""
    for i in start_message:
        if i in original:
            a = original.index(i)       #returns the pos of the char in list
            message += encoding_list[a] #adds the encoded character to the message.
        else:
            message += i
    message += return_encoder_number(encoding-1)
    return message     

def decode(original,encryption_list, encoded_message):
    """decodes a an encrypted message provided by the user.

    Args:
        original ([str]]): original key to convert to.
        encryption_list ([str]]): the key that the message has been converted in.
        encoded_message (str): encoded message provided by the user.

    Returns:
        str: returns decoded string to user.
    """
    message = ""
    for i in encoded_message:
        if i in encryption_list:
            a = encryption_list.index(i)    #returns the position of the letter or number in the list
            message += original[a]
        else:
            message += i
    return message

def to_encode(total_list,start_message, encoding=None):
    """encodes a given message.

    Args:
        total_list ([[str]]): contains all possible keys.
        start_message (str): contains the message to encode. 
        encoding (int, optional): contains the key number for the encryption. Defaults to None.

    Returns:
        str: returns an encoded string.
    """
    if encoding is None:
        encoding = rand.randint(1, len(total_list)-1)
    return encode(total_list[0],total_list[encoding], encoding, start_message)

def to_decode(total_list, start_message):
    """decodes a message inputted by the user.`

    Args:
        total_list ([[str]]): contains all possible keys for encryption.
        start_message (str): contains the decoded message.

    Returns:
        str: returns decoded message.
    """
    f = int(start_message[-2:])+1
    m = total_list[f]
    return decode(total_list[0], m,start_message[:-2])

def main(file_name):
    """runs the program.

    Args:
        file_name (str): contains the name of the file that stores all the keys. 
    """
    x = get_lists(file_name)
    print("Hello!")
    check_password(x)
    dashboard(x)

def get_lists(file_name):
    """gets all possible keys for encryption from the file specified.

    Args:
        file_name (str): contains the name of the file which contains the keys.

    Returns:
        [[str]]: returns all possible keys.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            temp = [line.strip().split(",") for line in file]
            for x in temp:
                m = x.index("01234")
                x[m] = ","
        return temp
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{file_name}'.")
        return []
    except UnicodeDecodeError:
        print(f"Error: The file '{file_name}' contains invalid characters for the specified encoding.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def dashboard(lists):
    """runs the main loop for the command line interface.

    Args:
        lists ([[str]]): contains all possible keys.
    """
    while True:
        number = input("1) Encode\n2) Decode\n3) Exit\nPlease type your choice: ")
        if is_integer(number):
            number = int(number)
            if number == 1:
                start_message = test_input("Please enter a message to encode: ")
                print("Encoded message is: "+to_encode(lists, start_message))
            elif number == 2:
                start_message = test_input("Please enter a message to decode: ")
                print("Decoded message is: "+to_decode(lists, start_message))
            elif number == 3:
                print("Bye!")
                break
            else:
                print("Please enter answer of either 1 or 2!")

def check_password(lists):
    """checks the password to authenticate the user.

    Args:
        lists ([[str]]): contains all possible keys.
    """
    while True:
        password = input("Please enter user password: ")
        actual_password = "C644cYc`4Sy23"
        if to_encode(lists,password,int(actual_password[-2:])+1) == actual_password:
            break
        else:
            continue

main("EncryptionKey.txt")
