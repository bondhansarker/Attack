# Python Password Sprayer

Simple password sprayer written in Python

This is the Python 3.x version of the source code.

The following tool can be used to test one or more passwords
against multiple user accounts. 

Generally the  number of passwords tested per script run will
be enough to not trigger account lock out.

For example you may only wish to sue a single password and run
the script every 30 mins.

## Configuration

The script uses a YAML script for input parameters. This should be called user.yaml
and be located in the same folder as the script

Note: This will be made an input param in future releases. 

The input params should be:

* url - the target URL
* user_field - The name of the user input field the API accepts
* password_field - The name of the password input field 
* methods - a list of request methods to use
* valid_response - nested under response, the value returned that confirm the a successful login.
* users - a list of users
* passwords - a list of passwords to use

The following YAML demonstrates the above:

```
url: "http://some.website/api/v1/login"
user_field: "userName"
password_field: "passWord"

methods:
- POST
- GET
- PUT

data: null

users:
- bsmith@blah.com
- jbloggs@blah.com

passwords:
- passw0rd1234

```


## Operation

Clone the source code from git and create myconf.yaml with required information.
Run the script with:

```
python3 -m username_bruteforcer my_conf.yaml

```

Once complete two YAML output files will be generated.

valid_logins.yaml - a list of valid usernames/password logins

invalid_loginss - a list of usernames/passwords that failed
