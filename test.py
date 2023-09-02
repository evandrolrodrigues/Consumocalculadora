import bcrypt

# Coletar a senha do usuário durante o registro
user_password = input("Digite a senha do usuário durante o registro: ")

# Gerar um hash bcrypt para a senha
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(user_password.encode(), salt)

# Armazenar 'hashed_password' no campo 'user_password' do banco de dados
