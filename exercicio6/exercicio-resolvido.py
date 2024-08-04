# Exercicio 6 - Crie um programa que solicite ao usuário um login e uma senha. O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123", caso contrário imprima uma mensagem de erro.

print('==== Login ====')

# variáveis para login
usuario = str(input('Usuário: '))
senha = str(input('Senha: '))

#verificação se usuário e senha estão corretos
if(usuario == 'admin' and senha == 'admin123'):
    print('Login bem sucedido!')
else:
    print('Usuário e/ou senha incorretos!')