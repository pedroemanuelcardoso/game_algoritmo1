import pygame
import sys
import time
pygame.init()
#altura e largura
LARGURA, ALTURA = 1000, 800
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Words And Dragons")
relogio = pygame.time.Clock()

# Cores 
COR_FUNDO = (30, 30, 40)       # Cinza escuro
COR_TEXTO = (240, 240, 240)    # Branco
COR_DESTAQUE = (255, 215, 0)   # Amarelo/Ouro para as letras dadas
COR_ALERTA = (220, 50, 50)     # Vermelho para erros e vida
COR_CAIXA = (10, 10, 20)       # Preto azulado para a caixa de texto
COR_AZUL  = (0, 100, 255)        # azul
COR_TITULO = (247, 55, 24)      # vermelho fogo 

# Fontes
fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_media = pygame.font.SysFont("Arial", 32)
fonte_pequena = pygame.font.SysFont("Arial", 24)
fonte_historia = pygame.font.Font(r"fontes/Eternalo.ttf", 47)
fonte_titulo = pygame.font.Font(r"fontes/chp-fire.ttf", 68)
fonte_game = pygame.font.Font(r"fontes/Nougat-ExtraBlack.ttf", 32)
fonte_nomeboss = pygame.font.Font(r"fontes/Enchanted Land.otf", 32)
#banco de dados
TEXTO_HISTORIA = [
            "No coração da floresta encantada",
            "existe uma dungeon que nunca foi conquistada",
            "prometendo riqueza inimaginavel a quem conquista-la",
            "diversos dos mais fortes guerreiros arriscaram-se",
            "mas todos fracassaram em suas missões",
            "voce terá oque é preciso pra completar a sua missão?",]
DADOS_ESTAGIOS = {
    # ESTÁGIOS
    1: {
        "nome_inimigo": "Goblin, o vigilante",
        "vida_inicial": 25,
        "dano_inimigo": 3,
        "arquivo_fundo": "Cenarios/Estagio1.png",
        "errar":[
            "hahahah, tu é muito ruim paporeto",
            "entendi nada parceiro",
        ],
        "tempo":[
            "tu é uma tartaruga?",
            "talvez tu seja mais lento na real",
        ],
        "transicao":[
            "o goblin ficou tão encantado por suas palavras",
            "que agora decidiu se tornar bibliotecario!",
            "ele gosta de carregar livros agora!!!",
        ],
        "dialogos": [
            "//voce chegou na entrada da dungeon",
            "-zzzzzzzzzzzzzzzzz",
            "//o goblin parece esta dormindo com o olho aberto, voce tenta entrar sem acorda-lo",
            "-EII!!! OQUE VOCE PENSA QUE ESTA FAZENDO?",
            "-O GOBLIN VIGILANTE NUNCA VACILA EM SEU POSTO",
            "-que estranho voce não me parece um guerreiro, oque queres aqui viajante?",
            "-EI!, não sabe que é falta de educação não responder uma pergunta?",
            "-jovem,diversos guerreiros altamentes treinados ja tentaram conquistar essa dungeon", 
            "-como voce que nao carrega nem mesmo uma espada poderia conseguir?",
            "-e voce não tem porte de um soldado",
            "-bem,como estou num dia bom eu permito que voce de o primeiro ataque hahahaha",
            "-AI!!!!!!", 
            "-OXI, COMO TU CONSEGUIU ME DAR DANO APENAS DIZENDO UMA PALAVRA?",
            "-voce é algum tipo de bruxo ou coisa do tipo?", 
            "-PREPARE-SE PARA MORRER BRUXO", 
 ],
        "letras": ["O", "R", "A", "M"],
        "validas": {"AMO", "AMOR", "ROMA", "RAMO", "MAR", "ORAR", "MAO", "ROAM","AMAR","MORAR","MORRAR","ARMA","AMARRAR","MORRA","AMARRO","ARMAR","AMA"}
    },
    2: {
        "nome_inimigo": "cobra, a sagaz",
        "vida_inicial": 20,
        "dano_inimigo": 2,
        "arquivo_fundo": "Cenarios/Estagio2.png",
        "errar":[
            "que??????",
            "rrepete porrfavorr",
        ],
        "tempo":[
            "lerrdo demaiss",
            "você é a minha pressa haha",
        ],
        "transicao":[
            "pela primeira vez, ela conseguiu manter uma conversa",
            "ela ficou tão feliz com o bate papo",
            "que deixou o jogador passar",
            "e agora considera-o seu melhor amigo",
        ],
        "dialogos": [
            "vejo que derrotou o vigiass",  
            "logo no dia do pokerrss",  
            "devo inforrma-lo que não possui chance contrra mim jovem",  
            "mass devo admitirr que chegarr aqui ssem uma esspada é impressionante",  
            "//que estranho, a cobra puxa o R e o S pra falar",  
            "de todoss os chefess da massmorrass eu ssou a maiss rrápida" ,
            "bom, pra não falarr nada até agora deve estarr sse trremendo de medo",  
            "PRREPARRA-SSE",  
            "//pra ela falar assim, ela deve apenas entender dessa forma",  
            "//devo usar isso contra ela",  
 ],
        "letras": ["M", "S", "A", "R","E"],  
        "validas": {"MARRESS", "MESSASS", "REMASS", "MARRA", "MASSA", "MARRE", "AMARRA", "SERRA", "ERRASS", "ARRMASS", "AMARR", "MESSA", "RRAMA", "SSERA", "ERRASS", "ARRME", "SARRE", "MARR", "MASS", "SERR","MASSASS","MARRERR","ERRARR","ERRA","AMASSARR"}  
    },
    3:{
       "nome_inimigo": "troll, o americano",  
       "vida_inicial": 30,  
       "dano_inimigo": 4,  
       "arquivo_fundo": "Cenarios/Estagio3.png",
       "errar":[  
           "what??? Speak english pls ",  
           "OMG, is that spanish???", 
], 
       "tempo":[   
           "you are like a snail",  
           "get better kid looool",  
],  
        "transicao":[
            "o troll finalmente encontrou alguem bilingue",
            "ele achava que estava no mexico, mas voce o ajudou",
            "ele disse que agora que sabe onde encontra-se",
            "vai conseguir retornar a sua terra natal",
            "e assistir varios jogos de basquete presencialmente",
        ],
        "dialogos": [  
            "hello?",  
            "can you speak english?",  
            "brother, are you deaf?",  
            "nah, i hate this country ",  
            "my live in america its so much better bro",  
            "damn, i wish go back",
            "soooo, im gonna kill you lol",  
            "// acho que ele não fala português",  
            "// vou precisar falar de uma forma que ele entenda", 
],  
     "letras": ["L", "O", "R", "V","E"],  
     "validas": {"LOVE", "LOVER", "ROLE", "ROVE", "OVER", "VOLE", "ORE", "LEVEL","EVER","VEER","LORE","LEER", "VOTE","VOTER","VOTES","ROLES","REVOLVE","ROLLER","LOL","ROLL"}  
    },
    4:{
        "nome_inimigo": "Quimera, A princesa das bestas", 
        "vida_inicial": 25, 
        "dano_inimigo": 4,  
        "arquivo_fundo": "Cenarios/Estagio4.png",  
        "errar":[  
            "arim amissép amu met êcoV",  
            "eduja em rovafrop",
],  
        "tempo":[ 
           "odnumi res ues adomocni em eçirrub auT",
           "redrep ari oãn se !!!euqof",

],      
        "transicao":[ 
           "foi uma boa luta", 
           "OQUE? Como eu consigo falar normal?",
           "você... me libertaste da minha maldição jovem poeta?",  
           "saiba que para sempre eu serei grata", 
           "mas cuidado jovem poeta", 
           "o dragão sábio ti espera na próxima sala", 
           "vai ser sem duvidas, o seu inimigo mais mortal", 
           "ti desejo sorte em sua jornada!!!", 
],  
       "dialogos": [  
           "iuqa eta ragehc rop osoidnarg o ahca es euq orierutneva ortuO",   
           "!iuqa abaca adanroj aus a etnemzilefni ,arutairc erbop ",             
           "//estranhamente ela não passa sede de sangue",  
           "//na realidade, ela parece esta triste com algo", 
           "rohlem ragul mu arp mevel it sesueD so euq ",  
           "//pera, as falas delas parecem estar ao contrario",
           "!!!ARROM", 
],
       "letras": ["A", "M", "O", "R", "T"], 
"validas": {"ROMA","AMOR","RAM","OMAR","AMOT","ROMA","OTAM","AMOT","RAMOT","RAROM","AROM","OTAR","ORAP","OMA","OTA","ORA","RARO","ATROM","ATROT","ATOR","ROTA","AROT","OTOM","ROTOM","RATNOM","ORAT"}
    },
     5:{
        "nome_inimigo": "Dragão, O sábio ", 
        "vida_inicial": 45, 
        "dano_inimigo": 5,  
        "arquivo_fundo": "Cenarios/Estagio5.png",  
        "errar":[  
            "Tua motivação é falha assim como tu eres maldoso",  
            "tuas palavras não me afetam, o poeta perdido",
],  
        "tempo":[ 
           "Tua indecisão te matará pois o medo é o maior vilão dos heróis",
           "não possui a confiança necessária para me derrotar",

],      
        "transicao":[ 
           "tais palavras cortam mais profundo que qualquer lamina", 
           "por eras eu esperei por uma pessoa digna",
           "abra a porta, e faça seu pedido",  
           "//o poeta então entra na sala e realiza seu pedido aos deuses", 
           "-O masmorra infernal, me ensinaste a comunicar sem ferir",
            "-a amar sem exigir. Peço agora nesse momento de alegria",
            "-devolva ao antigo poeta a fala e a melodia",
            "-fui testado pelo dragão e consegui meu troféu",
            "-agora peço que me afaste desse meu destino cruel",
            "-para que eu possa falar sem machucar",
             "e que possa amar sem cessar",
],  
       "dialogos": [  
           "//o poeta finalmente se depara com seu desafio final",  
           "eu consigo ver o seu passado jovem poeta",  
           "Teu coração era soberbo e maligno, enganava a todos com tuas poesias ordinárias",             
           "os Deuses te puniram com essa maldição",  
           "Fostes amaldiçoado a causar dor, conforme tu falas", 
           "nunca mais tu irias se aproximar de alguém de novo",  
           "//o poeta sabe que sua punição é justa, mas ainda assim ele deve tentar",
           "Venha e seja meu oponente para que a masmorra liberte você da prisão de tuas palavras",
           "//Mas agora ele tinha aprendido como usar suas palavras para ajudar os outros",
           "//com o goblin, aprendeu a perseguir seus sonhos", 
           "//com a cobra, aprendeu que falar diferente não é errado",
           "//com o trol aprendeu que a linguagem não impedem a propagação de sentimentos",
           "//com a quimera aprendeu a dar valor a suas palavras pois poderiam salvar os outros",
           "//o poeta estava cheio de DETERMINAÇÃO",
],
       "letras": ["P", "O", "E", "T", "A", "S"], 
"validas": {"POETAS", "POETA", "SAPATO", "SAPATOS", "TAPETE", "TAPETES", "POSTA", "POSTAS", "PASTO", "PASTOS", "PATO", "PATOS", "POPA", "POPAS", "SOPA", "SOPAS", "POTE", "POTES", "TESA", "TESAS","POSE"}
    }
}
TEXTO_FINAL = [
            "e o poeta saiu recitando poesias",
            "e jurou que ia usar suas palavras apenas para o bem",
            "a torre continua lá ao fundo",
            "apenas esperando a próxima história a ser contada",
            "e o próximo desejo atendido",
            "como uma benção dos deuses",
            "aos pecadores profanos",
            ]

#VARIÁVEIS 
estagio_atual = 1
estado_jogo = "MENU"  
indice_dialogo = 0       # Qual frase do monstro está passando na tela
indice_erro = 0          # qual frase de error o monstro vai falar
indice_tempo = 0         # qual frase de tempo o monstro vai falar
indice_frase = 0
monstro_erro = 0
monstro_tempo = 0
vida_jogador = 20
vida_permanente = 20
# TEMPOS
# historia
tempo_frase =  3.0
troca_frase = 3
#combate
tempo_limite = 20.0
tempo_tela =  20
inicio_turno = 0
# Pegando os dados do primeiro monstro para começar
vida_monstro = DADOS_ESTAGIOS[estagio_atual]["vida_inicial"]
imagem_fundo = pygame.image.load("Cenarios/menu.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
imagem_menu = pygame.image.load("Cenarios/menu.png")
imagem_menu = pygame.transform.scale(imagem_menu, (LARGURA, ALTURA))
imagem_fundofinal = pygame.image.load("Cenarios/telafinal.png")
imagem_fundofinal = pygame.transform.scale(imagem_fundofinal, (LARGURA, ALTURA))
dano_inimigo = DADOS_ESTAGIOS[estagio_atual]["dano_inimigo"]
palavra_digitada = ""
palavras_usadas = set()
texto_feedback = "Digite uma palavra com as letras acima e aperte ENTER!"
cor_feedback = COR_TEXTO

#LOOP PRINCIPAL
#musica menu/historia
pygame.mixer.music.load(r"trilha/musica_menu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3) 
while True:
    tela.fill(COR_FUNDO)
    

    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  
            pygame.quit()
            sys.exit()
            
        elif evento.type == pygame.KEYDOWN:
            if estado_jogo == "MENU": #jogo esta no menu
                if evento.key == pygame.K_RETURN:  # Apertou Enter
                    estado_jogo = "HISTORIA"
                    indice_dialogo = 0
                    troca_frase = time.time() 
                    pygame.event.clear()
             
            elif estado_jogo == "DIALOGO": #jogo esta no dialogo
                if evento.key == pygame.K_RETURN:  # Apertou Enter pra passar as falas
                    indice_dialogo += 1
                    # Se acabarem as falas desse monstro começa a luta
                    if indice_dialogo >= len(DADOS_ESTAGIOS[estagio_atual]["dialogos"]):
                        indice_dialogo = 0
                        estado_jogo = "BATALHA"
                        texto_feedback = "A batalha comecou! Forme palavras!"
                        cor_feedback = COR_TEXTO
                        inicio_turno = time.time()
                        pygame.event.clear()  # Limpa o teclado para evitar pulos rápidos
                        pygame.mixer.music.load(r"trilha/musica_batalha.mp3")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(0.3)
            
            # modo luta
            elif estado_jogo == "BATALHA":
                dano_inimigo = DADOS_ESTAGIOS[estagio_atual]["dano_inimigo"] 
                if evento.key == pygame.K_RETURN:  # Apertou Enter para enviar palavra
                    palavra = palavra_digitada.upper().strip()
                    # Verifica se a palavra está na lista de palavras válidas do monstro e vai verificar se o jogador ja usou ela
                    if palavra in DADOS_ESTAGIOS[estagio_atual]["validas"]:
                     if not(palavra in palavras_usadas): 
                        dano = len(palavra)
                        vida_monstro -= dano
                        texto_feedback = f"Acertou! '{palavra}' causou {dano} de dano!"
                        palavras_usadas.add(palavra)
                        cor_feedback = COR_DESTAQUE
                        inicio_turno = time.time()
                        
                        # verifica se o monstor morreu
                        if vida_monstro <= 0:
                            estado_jogo = "TRANSICAO"
                            palavras_usadas.clear()
                            pygame.mixer.music.load(r"trilha/musica_dialogos.mp3")
                            pygame.mixer.music.play(-1)
                         
                    else:
                        texto_feedback = DADOS_ESTAGIOS[estagio_atual]["errar"][indice_erro]
                        cor_feedback = COR_ALERTA
                        vida_jogador = vida_jogador - dano_inimigo
                        indice_erro += 1
                        inicio_turno = time.time()
                        if indice_erro >= len(DADOS_ESTAGIOS[estagio_atual]["errar"]):
                            indice_erro = 0
 
                        
                    palavra_digitada = ""  # Limpa o que foi digitado após o Enter
                    
                elif evento.key == pygame.K_BACKSPACE:  # Apertou Backspace para apagar
                    palavra_digitada = palavra_digitada[:-1]
                else:
                    # Se for uma letra normal do teclado, adiciona ao texto digitado
                    if evento.unicode.isalpha() and len(palavra_digitada) < 10:
                        palavra_digitada += evento.unicode.upper()
            elif estado_jogo == "TRANSICAO":
                if evento.key == pygame.K_RETURN:  # Apertou Enter pra passar as falas
                    indice_frase += 1
                   # Se passou do nível 5 acaba, 
                    if indice_frase >= len(DADOS_ESTAGIOS[estagio_atual]["transicao"]):
                        # Carrega os dados do próximo monstro e volta pro diálogo
                        indice_frase = 0
                        estagio_atual += 1
                        if estagio_atual > 5:
                         estado_jogo = "VITORIA"
                         troca_frase = time.time()
                         pygame.mixer.music.load(r"trilha/musica_final.mp3")
                         pygame.mixer.music.play(-1)
                        else:
                         estado_jogo = "DIALOGO"
                         vida_monstro = DADOS_ESTAGIOS[estagio_atual]["vida_inicial"]
                         imagem_fundo = pygame.image.load(DADOS_ESTAGIOS[estagio_atual]["arquivo_fundo"])
                         imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
                         texto_feedback = ""
                         vida_jogador = vida_permanente
            elif estado_jogo == "DERROTA":
                if evento.key == pygame.K_RETURN:  # Apertou Enter pra voltar
                    estado_jogo = "MENU"
                    estagio_atual = 1
                    vida_jogador = vida_permanente
                    pygame.mixer.music.load(r"trilha/musica_menu.mp3")
                    pygame.mixer.music.play(-1)
    # tempos                
    if estado_jogo == "HISTORIA":
        tempo_atual = time.time()
        if tempo_atual - troca_frase >= tempo_frase:
         indice_dialogo += 1
         troca_frase = time.time()
         if indice_dialogo >= len(TEXTO_HISTORIA):
            indice_dialogo = 0
            estagio_atual = 1
            estado_jogo = "DIALOGO"
            vida_monstro = DADOS_ESTAGIOS[estagio_atual]["vida_inicial"]
           #acaba a historia e entra no primeiro inimigo da masmorra
            imagem_fundo = pygame.image.load("Cenarios/Estagio1.png")
            imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))
            # musica dialogo
            pygame.mixer.music.load(r"trilha/musica_dialogos.mp3")
            pygame.mixer.music.play(-1)
    if estado_jogo == "VITORIA":
       tempo_atual = time.time()
       if tempo_atual - troca_frase >= tempo_frase:
         indice_dialogo += 1
         troca_frase = time.time()
         if indice_dialogo >= len(TEXTO_FINAL):
            estado_jogo = "TELAFINAL"
    elif estado_jogo == "BATALHA":
        tempo_atual = time.time()
        tempo_passado = tempo_atual - inicio_turno
        tempo_tela = max(0, int(tempo_limite - tempo_passado))
        if vida_jogador <= 0:
         estado_jogo = "DERROTA"
        if tempo_passado >= tempo_limite:
            # Monstro ataca o jogador por demorar dms
         texto_feedback = DADOS_ESTAGIOS[estagio_atual]["tempo"][indice_tempo]
         indice_tempo+= 1
         if indice_tempo == len(DADOS_ESTAGIOS[estagio_atual]["tempo"]):
          indice_tempo = 0
         cor_feedback = COR_ALERTA
         vida_jogador = vida_jogador - dano_inimigo
         # Reseta o cronômetro dando mais 10 segundos
         inicio_turno = time.time()
    
    # DESENHAR NA TELA (Mostrando as coisas para o jogador)
   


    if estado_jogo == "MENU":
         
        tela.blit(imagem_menu, (0, 0))
        txt_titulo = fonte_titulo.render("WORDS AND DRAGONS", True, COR_TITULO)
        txt_jogar = fonte_game.render("Pressione ENTER para Iniciar", True, (100, 255, 100))
        
        # Centralizando os textos na tela
        tela.blit(txt_titulo, (130, 180))
        tela.blit(txt_jogar, (260, 400))
    elif estado_jogo == "HISTORIA":
        tela.fill((15, 15, 20))  # Fundo escuro 
        
        # Pega a frase atual do seu enredo
        frase_atual = TEXTO_HISTORIA[indice_dialogo]
        
        # Transforma o texto em imagem (centralizado na largura, e no topo Y=220)
        txt_narrativa = fonte_historia.render(frase_atual, True, COR_TEXTO)
        
        # Carimba na tela bem no começo/centro superior
        tela.blit(txt_narrativa, (LARGURA // 2 - txt_narrativa.get_width() // 2, 220))
    elif estado_jogo == "DIALOGO":
        tela.blit(imagem_fundo, (0, 0))
        pygame.draw.rect(tela, COR_CAIXA, (0, 700, 1000, 250))
        
        nome = DADOS_ESTAGIOS[estagio_atual]["nome_inimigo"]
        fala = DADOS_ESTAGIOS[estagio_atual]["dialogos"][indice_dialogo]
        
        # Transforma o texto em imagem para colar na tela
        txt_nome = fonte_media.render(f"[{nome}]", True, COR_DESTAQUE)
        txt_fala = fonte_pequena.render(fala, True, COR_TEXTO)
        txt_instrucao = fonte_pequena.render("(ENTER para continuar)", True, (120, 120, 120))
        
        # Coloca as imagens de texto nas posições (X, Y) da tela
        tela.blit(txt_nome, (0, 660))
        tela.blit(txt_fala, (0, 700))
        tela.blit(txt_instrucao, (600, 770))

    elif estado_jogo == "TRANSICAO":
        frase_monstro = DADOS_ESTAGIOS[estagio_atual]["transicao"][indice_frase]    
        frase_monstro = fonte_historia.render(frase_monstro, True, COR_TEXTO)
        txt_instrucao = fonte_pequena.render("(ENTER para continuar)", True, (120, 120, 120))
        tela.blit(frase_monstro, (LARGURA // 2 - frase_monstro.get_width() // 2, 220))
        tela.blit(txt_instrucao,( 500, 620))
    #  SE ESTIVER EM BATALHA 
    elif estado_jogo == "BATALHA":
        # Mostra o nome do inimigo e a vida dele no topo
        nome_monstro = DADOS_ESTAGIOS[estagio_atual]["nome_inimigo"]
        txt_topo = fonte_nomeboss.render(f"{nome_monstro} - Nivel {estagio_atual}", True, COR_TEXTO)  
        if vida_jogador <= dano_inimigo:
            COR_VIDA = COR_ALERTA
        elif vida_jogador <= vida_permanente // 2:
            COR_VIDA = (244,244,0)
        else:
            COR_VIDA = (0,0,244)
        txt_vida_personagem = fonte_media.render(f"Personagem: {vida_jogador}", True, COR_VIDA)
        txt_tempo = fonte_media.render(f"Tempo: {tempo_tela}s", True, COR_TEXTO)
        pygame.draw.rect(tela, (50, 50, 50), (50, 100, 300, 20))
        
        # Calcula o tamanho proporcional do retângulo vermelho com base na vida atual
        vida_maxima_monstro = DADOS_ESTAGIOS[estagio_atual]["vida_inicial"]
        largura_vida_monstro = int((vida_monstro / vida_maxima_monstro) * 300)
        largura_vida_monstro = max(0, largura_vida_monstro) # Proteção para nao passar de 0
        pygame.draw.rect(tela, COR_ALERTA, (50, 100, largura_vida_monstro, 20))

        tela.blit(txt_topo, (45, 60))
        tela.blit(txt_vida_personagem,(50,600))
        tela.blit(txt_tempo,(800,600))
        
        # Junta as letras dadas separadas por espaços (Ex: "A   M   O   R")
        letras_separadas = "   ".join(DADOS_ESTAGIOS[estagio_atual]["letras"])
        txt_letras = fonte_grande.render(letras_separadas, True, COR_DESTAQUE)
        tela.blit(txt_letras, (LARGURA // 2 - txt_letras.get_width() // 2, 220))
        
        # Mostra o que o jogador está digitando na barra de digitação
        txt_digitado = fonte_grande.render(palavra_digitada, True, COR_TEXTO)
        tela.blit(txt_digitado, (LARGURA // 2 - txt_digitado.get_width() // 2, 350))
        # Linha decorativa embaixo do texto digitado
        pygame.draw.line(tela, COR_TEXTO, (LARGURA // 2 - 150, 410), (LARGURA // 2 + 150, 410), 3)
        
        # Mostra a mensagem se ele errou ou acertou a palavra
        txt_feed = fonte_pequena.render(texto_feedback, True, cor_feedback)
        tela.blit(txt_feed, (LARGURA // 2 - txt_feed.get_width() // 2, 460))
    elif estado_jogo == "VITORIA":
        frase_atual = TEXTO_FINAL[indice_dialogo]
        
        txt_narrativa = fonte_historia.render(frase_atual, True, COR_TEXTO)
        
        # Carimba na tela bem no começo/centro superior
        tela.blit(imagem_fundofinal,(0,0))
        tela.blit(txt_narrativa, (LARGURA // 2 - txt_narrativa.get_width() // 2, 220))
        
    #desenho caso tenha vencido ou perdido
    elif estado_jogo == "TELAFINAL":
        tela.fill((15, 15, 20))
        txt_vitoria = fonte_game.render("ATÉ A PROXIMA", True, COR_DESTAQUE)
        txt_sub = fonte_pequena.render("OBRIGADO POR JOGAR", True, COR_TEXTO)
        tela.blit(txt_vitoria, (LARGURA // 2 - txt_vitoria.get_width() // 2, 250))
        tela.blit(txt_sub, (LARGURA // 2 - txt_sub.get_width() // 2, 320))
    elif estado_jogo == "DERROTA":
        tela.fill((0, 0, 0))
        txt_derrota = fonte_game.render("O INIMIGO NÃO FOI CONVENCIDO COM SUAS PALAVRAS!!!", True, COR_ALERTA)
        txt_sub = fonte_pequena.render("VOCE FRACASSOU EM SUA MISSÃO", True, COR_TEXTO)
        txt_jogar = fonte_pequena.render("Pressione ENTER para reiniciar", True, (244, 255, 244))
        tela.blit(txt_derrota, (LARGURA // 2 - txt_derrota.get_width() // 2, 250))
        tela.blit(txt_sub, (LARGURA // 2 - txt_sub.get_width() // 2, 320))
        tela.blit(txt_jogar,(300, 500))
    pygame.display.flip()
    relogio.tick(30)