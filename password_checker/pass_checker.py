import requests #allows us to make a request like a browser
import hashlib #secure hashes library
import sys

def request_api_data(query_char): #it will request our data and give us a response
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA' #only the first 5 characters of the hash
    res = requests.get(url) 
    print(res) #we will get as a response all the passwords that begin with that hash
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines()) #loops through each item of the list
    for h, count in hashes:
        if h == hash_to_check: #if the hash has been leaked return it to us how many times it was leaked
            return count 
    return 0 #otherwise return 0

def pwned_api_check(password):
    #check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #converts the password in sha1
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response,tail) #prints all the entries that match the beginning of our password.

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should problably changes your password')
        else:
            print(f'{password} was not found. Carry on!')
    return 'done!'

if __name__ == '__main__': #only run this file if this is in the command line and not if it has been exported
    sys.exit(main(sys.argv[1:])) #exits out of the file