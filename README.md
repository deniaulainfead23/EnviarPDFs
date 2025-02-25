Descrição do Código de Envio de Declarações por E-mail
O código desenvolvido tem como objetivo automatizar o envio de declarações personalizadas para alunos que participaram de um evento, palestra ou atividade acadêmica. Ele utiliza a biblioteca smtplib para o envio de e-mails e pandas para manipulação dos dados dos alunos contidos em um arquivo CSV.

Principais Funcionalidades:

♥ Leitura automática da planilha (dados.csv)

O código carrega os dados dos alunos, incluindo nome, e-mail e palestra assistida.
Verifica se todas as colunas estão corretamente estruturadas antes do processamento.

♥ Geração dinâmica do nome do arquivo da declaração


As declarações são armazenadas em uma pasta específica e são nomeadas seguindo um padrão (declaracao1.pdf, declaracao2.pdf, etc.).
O código associa cada declaração ao respectivo aluno com base na ordem do CSV.

♥ Envio automático de e-mails


Utiliza um servidor SMTP (exemplo: Gmail) para enviar as declarações.
Inclui um anexo PDF personalizado no e-mail.
O e-mail é formatado com uma mensagem padronizada, incluindo o nome do aluno e a palestra assistida.

♥ Validações para evitar erros


Antes de enviar, o código verifica se o arquivo da declaração existe.
Se o arquivo não for encontrado, exibe um aviso sem interromper o envio dos outros e-mails.
Possui um limite de 47 e-mails enviados por execução.

♥ Segurança e Autenticação

Para o envio pelo Gmail, é necessário gerar uma senha de aplicativo e evitar o uso da senha pessoal.
Suporta outras configurações de SMTP, como Outlook e Yahoo.
Benefícios da Automação

♥ Economia de tempo → Enviar manualmente dezenas de e-mails seria demorado e propenso a erros.

♥ Precisão → O código assegura que cada aluno recebe sua declaração correta.

♥ Escalabilidade → Pode ser facilmente adaptado para processar mais declarações.

♥ Redução de erros humanos → Garante que todos os e-mails sejam enviados corretamente e que arquivos não sejam esquecidos.


Esse código pode ser utilizado por instituições de ensino, organizadores de eventos e equipes acadêmicas que precisam distribuir certificados ou declarações de forma eficiente.
