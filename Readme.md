
<h1> O r c l e !</h1>

<h2>Um sistema simples de gestão de empréstimo de intens</h2>

<p>Este projeto foi realizado como parte dos critérios necessários para aprovação na disciplina de Tópicos Especiais em Informática, ministrada pelo Prof. Fabrício Henrique na FATEC - Ribeirão Preto
</p>

<h3>Objetivo</h3>
<p>Desenvolver uma aplicação utilizando a linguagem de programação Python de acordo com o tema escolhido em Sala de Aula.</p>

<h3> Requisitos </h3>
<strong><p>Implementar uma aplicação que contenha pelo menos dez interfaces gráficas (UI)</p></strong>
<p>O sistema desenvolvido conta com as seguintes interfaces:
<ul>
    <li> Index: Esta tela apresenta apenas o logo e os botões de login e de criar conta</li>
    <li> Criar Conta: tela com formulário a ser preenchido por novos usuários</li>
    <strong><li> Login: tela com formulário a ser preenchido por usuários já cadastrados para acesso ao sistema</li></strong>
    <strong><li> Sobre: tela com informações do Projeto</li></strong>
    <li>Meu Orcle
        <ul>
            <li>Meu Perfil: Tela com informaçõs do Usuário
                <ul>
                    <li>Editar Perfil: Formulário para edição de informações do Usuário</li>
                    <li>Baixar meus itens: Botão para dowload dos itens cadastrados em formato ZIP (com um JSON dentro)</li>
                    <li>Excluir Conta: Botão para exclusão do perfil</li>
                </ul>
            </li>
            <li>Meus Itens: Tela de listagem dos itens de propriedade do Usuário logado
                <ul>
                    <li>Alterar: Formulário para alteração dos dados do item</li>
                    <li>Excluir: Formulário para exclusão do item</li>
                </ul>
            </li>
            <li>Meus Empréstimos: listagem de todos os empréstimos feito pelo usuário
                <ul>
                    <li>Alterar data de Devolução: formulário para cadastrar nova data de devolução</li>
                    <li>Cadastrar Devolução: formulário para registrar devolução</li>
                    <li>Confirmar: formulário para aceitar empréstimo solicitado por outro usuário</li>
                </ul>
            </li>
            <li>Sair: faz o logout do sistema</li>
    </ul></li>
    <li>Pessoas: lista os usuários cadastrados no Orcle!</li>
    <li>Itens
        <ul>
            <li>Listar Itens: lista de todos os itens cadastrados pelos usuários
                <ul><li>Pedir emprestado: formulário para solicitação de empréstimo do item</li></ul>
            </li>
            <li>Criar item: formulário para cadastro do item</li>
            <li>Listar Tipos de Item: lista dos tipos cadastrados</li>
            <li>Criar Tipo de Item: formulário para criar um novo tipo de item</li>
        </ul>
    </li>
    <li>Detalhes do item: tela que mostra os dados completos do item cadastrado alcançada clicando em qualquer item de 'Listar itens'</li>
    <li>Detalhes do Usuário: tela que mostra os dados do usuário, é alcançada clicando em qualquer usuário da lista 'Pessoas'</li>
</ul>
</p>
<strong> <p>Armazenar dados de maneira persistente utilizando o SGBD da sua preferência</p>
    <ul>
        <li>Os dados precisam ser armazenados em pelo menos três tabelas</li>
        <li>Para cada tabela codificar na UI no mínimo três operações, dentre elas: Insert, Update, Delete e/ou Select</li>
    </ul></strong>
    
<p>Os dados foram armazenados no banco de dados SQLite e foram implementados CRUDs para 4 trabelas (Perfil, Item, TipoItem e Empréstimos)</p>
<p>Elaborar, necessariamente, as seguintes UI
<ul>
<li>Login: em que o usuário deverá fornecer um nome de usuário e uma senha. O acesso as funcionalidades do sistema ocorrem apenas para usuários previamente cadastrados.</li>
<li>Sobre: que apresente dados do projeto {tema escolhido e objetivo} e dos desenvolvedores: {nome completo e código de matrícula}.</li>
<li>Menu: em que o usuário poderá escolher a opção desejada da aplicação.</li>
</ul></p>
<p>Todas as UI citadas foram implementadas, o menu não foi implementada em uma url específica, mas sim em um componente HTML que é iportado em todas as UIs em que o usuário acessa após logar-se</p>
<strong><p>Implementar uma funcionalidade que exporta todos os dados da aplicação no formato JSON. O arquivo deve ser compactado no formato zip.</p></strong>
<p>Foi implementada uma função para baixar todos os dados do banco em arquivos JSONs zipados, esta funcionalidade encontra-se na aba 'Sobre' além disso foi implementada uma funcionalidade que exporta os itens cadastrados pelo usuário que econtra-se na aba 'Meu Perfil'</p>
<strong><p>Implementar uma funcionalidade para importar dados.</p></strong>
<ul>
<strong><li>Os dados devem ser disponibilizados em um endereço da web.</li></strong>
    <li>Os dados foram importados do <a href="https://viacep.com.br/">VIACEP</a></li>
<strong><li>Usar o módulo Requests ou URLlib.</li></strong>
        <li>Foi utilizado o modulo Requests</li>
<strong><li>Armazenar os dados importados em uma tabela.</li></strong>
        <li>Os dados foram armazenados na tabela Profile (perfil)</li>
<strong><li>Apresentar os dados importados em uma UI da aplicação.</li></strong>
        <li>Os dados são apresentados na tela Meu Perfil</li>
</ul>
    
   

