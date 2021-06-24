import os
import base64, binascii
import codecs
# This is the JWT format of Body and Header
userInput = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZW1vLnNqb2VyZGxhbmdrZW1wZXIubmxcLyIsImlhdCI6MTU0NzcyOTY2MiwiZXhwIjoxNTQ3Nzk5OTk5LCJkYXRhIjp7Ik5DQyI6InRlc3QifX0"
pkey = os.popen('cat ~/key.pem').read().replace('-----BEGIN PUBLIC KEY-----','')

# The hexKey will store the value of the Public Key converted into ASCII format.
hexKey = os.popen('cat ~/key.pem | xxd -p | tr -d "\\n"').read()
# The HMAC_Signature will store the Signature.
HMAC_Signature = os.popen(
    'echo -n "' + userInput + '" | openssl dgst -sha256 -mac HMAC -macopt hexkey:' + hexKey).read()
#HMAC_Signature = HMAC_Signature.replace("(stdin)=",'')
# This line of code is to convert the HMAC_Signature to ASCII Hex format.
print(base64.urlsafe_b64encode(binascii.a2b_hex(HMAC_Signature[9::].strip())).replace(b'=',b''))