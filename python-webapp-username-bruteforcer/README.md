
# Python WebApp Username Brute Forcer


The following tool can be used to brute force for valid user names
where a web application gives some indication if a user is valid
regardless if the password was wrong.

## Configuration

The script uses a YAML script for input parameters.

The input params should be:

* url - the target URL
* user_field - The name of the user input field the API accepts
* methods - a list of request methods to use
* data - a list of other parameters that may be required by the API/App
* valid_response - nested under response, the value returned that confirm the a successful guess of a username.
* users - a list of users

The following YAML demonstrates the above:

```
url: "http://some.website/api/v1/login"
user_field: "userName"

data: null

methods:
- POST
- GET
- PUT

users:
- bsmith@blah.com
- jbloggs@blah.com

```


## Operation

Clone the source code from git and create myconf.yaml with required information.

Run the script with:

```
python3 -m username_bruteforcer my_conf.yaml
```


Once complete two YAML output files will be generated.

`valid_users.yaml` - a list of valid usernames

`invalid_users` - a list of usernames where no match was found
