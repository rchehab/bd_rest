import uuid
import hashlib
class password():

	def hash_this(password):
	    # uuid gera um nymero aleatorio quase impossivel de ser igual a outro
	    salt = uuid.uuid4().hex # In cryptography, a salt is random data that is used as an additional input to a one-way function that "hashes" a password or passphrase
	    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

	def check_this(hashed_password, user_password):
	    password, salt = hashed_password.split(':')
	    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
