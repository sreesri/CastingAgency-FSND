import json
from flask import request, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = 'sri59776.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'user'


class AuthError(Exception):

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def getTokenFromHeader():
    authHeader = request.headers.get("Authorization", None)

    if authHeader is None:
        raise AuthError({
            "code": "Gen-Auth-404",
            "description": "Authorization Header is missing."
        }, 401)

    token = authHeader.split(" ")
    if len(token) != 2:
        raise AuthError({
            "code": "Gen-Auth-400",
            "description": "Malformed Authorization Header."
        }, 401)

    elif token[0].lower() != "bearer":
        raise AuthError({
            "code": "Gen-Auth-402",
            "description": "Authorization Header must start with 'Bearer'."
        }, 401)

    return token[1]


def checkPermission(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'Gen-Auth-Claim-404',
            'description': 'Permissions not included in JWT.'
        }, 401)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'Gen-Auth-401',
            'description': 'User unauthorized to perform this request.'
        }, 401)

    return True

def verify_decode_jwt(token):
    url_string = "https://{}/.well-known/jwks.json".format(AUTH0_DOMAIN)

    json_url = urlopen(url_string)
    jwks = json.loads(json_url.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_authorization_header',
            'description': 'Authorization Header is malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://{}/'.format(AUTH0_DOMAIN)
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'Gen-Auth-Exp-401',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'Gen-Auth-Claim-400',
                'description':
                    'Invalid claims.'
            }, 401)

        except Exception:
            raise AuthError({
                'code': 'Gen-Auth-500',
                'description': 'Unable to parse authentication token.'
            }, 401)

    raise AuthError({
        'code': 'Gen-Auth-key-400',
        'description': 'Invalid Auth Key.'
    }, 401)

def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = getTokenFromHeader()
                payload = verify_decode_jwt(token)
                checkPermission(permission, payload)
            except AuthError as authError:
                raise abort(authError.status_code,
                            authError.error["description"])
            
            return f(*args, **kwargs)
        return wrapper
    return requires_auth_decorator
