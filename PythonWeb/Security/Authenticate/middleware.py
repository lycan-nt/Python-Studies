from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key

app = FastAPI()

# Caminho para o arquivo .pem da chave privada
PEM_KEY_PATH = './owl.pem'

# Senha da chave privada
PRIVATE_KEY_PASSWORD = '131216'

# Middleware para verificar e autorizar o token JWT
def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    print('TOKEN: ' + token)

    try:
        # Carregar a chave privada no formato PEM com senha
        with open(PEM_KEY_PATH, 'rb') as pem_key_file:
            pem_key_data = pem_key_file.read()
            private_key = load_pem_private_key(pem_key_data, password=PRIVATE_KEY_PASSWORD.encode(), backend=default_backend())

        # Verificar a validade e decodificar o token JWT usando a chave privada PEM
        payload = jwt.decode(token, key=private_key.public_key(), algorithms=['RS256'])
        # Verificar se o token contém as informações necessárias para a autorização
        # (por exemplo, verificar permissões do usuário)
        # ...
        # Aqui você pode implementar a lógica para verificar as permissões do usuário
        # com base nas informações contidas no token, se necessário.

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expirado')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Erro interno do servidor')

# Restante do código permanece o mesmo...

# Rota protegida que requer autenticação com token JWT
@app.get('/protegido', dependencies=[Depends(verify_jwt_token)])
def rota_protegida():
    return {'message': 'Esta é uma rota protegida por token JWT'}

# Rota para autenticação e obtenção do token JWT (do lado do Spring Boot)
@app.post('/login')
def fazer_login():
    # Implemente aqui a lógica de autenticação e geração do token JWT (do lado do Spring Boot)
    # ...

    # Exemplo: token gerado pelo lado do Spring Boot
    token = jwt.encode({'user_id': 123, 'role': 'admin'}, private_key, algorithm='RS256')
    return {'token': token}
