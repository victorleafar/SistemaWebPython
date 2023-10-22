oque precisamos ter no projeto
interface admin (ok)
migrations (ok)
rotas 
model. view e template

#ESTRUTURA PADRÃO UTILIZADA PELO DJANGO (MODELS, VIEWS, TEMPLATES)

# Motivo para Usar o SQLite:
O SQLite foi escolhido pela simplicidade e facilidade de uso. É leve, não requer configuração de servidor e é adequado para projetos pequenos, se adaptando perfeitamente 
para o proposito do trabalho.

## Vantagens de Usar o SQLite:
Zero Configuração: Não é necessário configurar um servidor separado.
Facilidade de Uso: Configuração direta e rápida.
Eficiente para Projetos Menores: Bom desempenho para projetos de tamanho moderado.
Facilidade de Backup: O banco de dados é um único arquivo, facilitando backup e movimentação.
Compatibilidade Ampla: Suportado em várias plataformas.
Ótimo para Desenvolvimento Local: Simples e rápido durante o desenvolvimento local.
Testes Simples: Facilita testes e experimentações.
Lembre-se de considerar requisitos de escalabilidade ao escolher um banco de dados para um projeto em crescimento.

nossa modelagem
produto (ID, DESCRICAO, PRECO);

criamos um super usuario
user: victor
pass: fernando123

Usuario teste que visualiza
User: luiz
Senha: 6MpDn.WKPDZnGV7

## comando necessaário
django-admin startproject crud
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
