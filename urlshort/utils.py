import base64
import hashlib

def shorten_url(full_url):
# 	hash_object = hashlib.sha1(b'Hello World')
# 	hex_dig = hash_object.hexdigest()
# 	print("hex_dig:", hex_dig, "hash_object:", hash_object)
# 	return hex_dig

	short_url = base64.b64encode(hashlib.sha1(full_url).digest())
	return short_url