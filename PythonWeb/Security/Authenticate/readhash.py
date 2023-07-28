from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def get_cert_hashes_from_pem_file(pem_file):
    with open(pem_file, 'rb') as f:
        pem_data = f.read()

    cert = x509.load_pem_x509_certificate(pem_data, default_backend())

    cert_hashes = []
    hash_algorithm = cert.signature_hash_algorithm
    cert_hash = cert.fingerprint(hash_algorithm).hex()
    cert_hashes.append((hash_algorithm.name, cert_hash))

    return cert_hashes

pem_file = './argospy.pem'
cert_hashes = get_cert_hashes_from_pem_file(pem_file)

for hash_algorithm, cert_hash in cert_hashes:
    print(f"Hash do certificado (algoritmo {hash_algorithm}): {cert_hash}")


