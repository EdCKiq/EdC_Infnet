## Casos de Uso
|| Caso de Uso 01 |
|------------------|:-----------------------:|
|            |  Criar conta na rede. | |
| **Atores**       | Usuário <br/> Sistema | 
| **Pré-condições**| Nenhuma             | 
| **Fluxo básico** | **1.**  O usuário fornece e-mail, senha e confirmações.<br/> **2.**  Os dados do usuário são validados, encriptados e persistidos pelo sistema.<br/>**3.**  O sistema gera e envia um link, com prazo de expiração, para que o usuário confirme seu e-mail.<br/>**4.**  O usuário confirma seu e-mail, clicando no link, antes do prazo de expiração.<br/>**5.**  O sistema confirma que a conta do usuário foi criada com sucesso.<br/>  **6.** O sistema redireciona o usuário para a página principal.|
|**Fluxos alternativos:** | **2a.** O e-mail ou a senha do usuário não são válidos. <br/> **2a1.** O sistema exibe uma mensagem para o usuário.<br/>**4a.** O usuário tenta confirmar o e-mail depois do prazo de expiração.<br/>**4a1**. O sistema sugere que o usuário realize um novo cadastro.|
| **Regras de validação:** |Confirmação de e-mail e senha: o usuário deve fornecer os dados duas vezes para minimizar o risco de erro.<br/>Validação de e-mail: verificar se o e-mail está em um formato válido, se o e-mail já consta na base de dados.<br/>Validação de senha: verificar se a senha respeita os requisitos de segurança (quais?).|
|**Pós-condições:**|   Nenhuma|

|| Caso de Uso 02 |
|------------------|:-----------------------:|
|            |  Adicionar fotos | |
| **Atores**       | Usuário <br/> Sistema | 
| **Pré-condições**| Usuário devidamente cadastrado na rede.             | 
| **Fluxo básico** | **1.** O usuário deve fornecer a foto desejada ao sistema.<br/> **2.**  A foto é enviada ao sistema para verificação de tamanho e tipo.<br/>**3.**  O sistema envia por email/notificação com uma confirmação que a foto subiu com sucesso<br/>**4.** O sistema redireciona o usuário para a página anterior.|
|**Fluxos alternativos:** | **2a.** Tamanho ou tipo fora dos padrões. <br/> **2a1.** O sistema exibe uma mensagem para o usuário, informando o erro e sua causa.|
| **Regras de validação:** |Verificação de imagem com formato e tamanho aceitáveis.<br/> Verificação de foto com conteúdo improprio e/ou sensível.|
|**Pós-condições:**|   Nenhuma|

|| Caso de Uso 03 |
|------------------|:-----------------------:|
|            |  Interação entre usuários | |
| **Atores**       | Usuário <br/> Sistema | 
| **Pré-condições**| Usuário devidamente cadastrado na rede e sem problemas de má conduta.             | 
| **Fluxo básico** | **1.** O usuário escolhe quais tipos e níveis de interação deseja ter com outros usuários.<br/> **2.** O sistema verifica se o usuário tem alguma flag de má comportamento.<br/>**3.** O sistema da as opções de interação de acordo com as privacidade dos outros usuários.<br/>**4.** O sistema faz o intermédio das comunicações dentro da plataforma para evitar fraudes e roubos online.|
|**Fluxos alternativos:** | **2a.** Usuário com flag de má comportamento. <br/> **2a1.** O sistema limita o uso desse usuário a apenas ler/ver postagens dependendo do nível de sua flag, podendo até resultar em expulsão da plataforma.|
| **Regras de validação:** |Verificação de comportamento dos usuários.<br/> Verificação de periculosidade em interações dentro da plataforma.|
|**Pós-condições:**|   Nenhuma|

|| Caso de Uso 04 |
|------------------|:-----------------------:|
|            |  Perfis acadêmicos | 
| **Atores**       | Usuário <br/> Sistema | 
| **Pré-condições**| Usuário devidamente cadastrado na rede.             | 
| **Fluxo básico** | **1.**O usuário deve fornecer informações sobre sua vida acadêmica e feitos<br/> **2.** O sistema valida a veracidade dessas informações de forma geral.<br/>**3.**O O sistema disponibiliza ao usuário um questionário para validação do interesse em perfil acadêmico.<br/>**4.** O sistema envia um email de confirmação da solicitação com um N° de protocolo.<br/>**5.** O sistema redireciona para a página principal.|
|**Fluxos alternativos:** | **2a.** Informações falsas. <br/> **2a1.** Ao se comprovar que a informação é falsa logo na primeira verificação, o sistema gera uma flag de má comportamento ao usuário e que por sua vez se torna inválido de se submeter a um perfil acadêmico pelos próximos 6 meses.|
| **Regras de validação:** |Verificação geral de veracidade.<br/> Verificação posterior mais detalhada do perfil requerente.|
|**Pós-condições:**|   Nenhuma|

|| Caso de Uso 05 |
|------------------|:-----------------------:|
|            |  Banimento | |
| **Atores**       | Usuário <br/> Sistema | 
| **Pré-condições**| Usuário devidamente cadastrado na rede.<br/> Acumulo de 5 flags de má comportamento.             | 
| **Fluxo básico** | **1.** O sistema válida a quantidade de flags.<br/> **2.**  O sistema bloqueia a conta do usuário a rede.<br/>**3.**  O sistema envia por email/notificação com as informações obre o banimento e seu motivo.<br/>**4.** O sistema gera um cronometro com base no grau de má comportamento do usuário, possibilitando que o mesmo possa voltar ao finalizar esse tempo.|
|**Fluxos alternativos:** | **1a.** Banimento injusto. <br/> **1a1.** O usuário ao verificar um banimento injusto, entra em contato com o nosso atendimento para verificação dos fatos e caso proceda, ganha as nossas devidas desculpas e o acesso a sua conta novamente.|
| **Regras de validação:** |Validação das flags.|
|**Pós-condições:**|   Bloqueio e/ou Retorno do usuário.|

