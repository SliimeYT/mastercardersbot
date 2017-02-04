#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8
import re, sys, markdown, time, split, simplejson, json, threading, base64, requests, traceback,time, random, datetime, androidhelper
from PythonColorize import * 
import telepot, os
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from functools import partial
from telepot.namedtuple import InlineQueryResultArticle
from pprint import pprint

os.system("clear")

reload(sys)
sys.setdefaultencoding('utf8')

droid = androidhelper.Android()
## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:]")
tm= today.strftime("%H:%M:")
uptime = datetime.datetime.today()
hora = uptime.strftime("%H:%M")
data = uptime.strftime("%d/%m/%Y")
M = uptime.strftime("%m")
D = uptime.strftime("%d")
A = uptime.strftime("%Y")
NomeBot = 'Rob么 Mastercards'
bot = telepot.Bot('284762175:AAHtNIoXPQ2PYupcY8OocXnIZKCWKhxUSqM')





## BOT LANG
info_id = u'''
Nome: {}
Usu谩rio: {}
ID: {}
______________
Nome do Grupo: {}

ID do Grupo: {} .'''
dados = "O Dado parou no n煤mero: 馃幉 *{}*"
info_start= u'''
Ol谩 {}, o que deseja?'''
info_oi = u'ol谩! *{}*!\n'
info_s = u'Ol谩 *{}*!\n, como posso ajudar?'
tm_info= u'De acordo com o meu rel贸gio agora s茫o {}.'
info_data= "Hoje 茅 dia `{}` do `{}` de `{}`, de acordo com o meu rel贸gio agora s茫o `{}` ."
senha = "Senha gerada `{}` ."
bem_vindo= "Ol谩 {} seja bem vindo(a) ao grupo {} ."
info_h = "de acordo com o meu rel贸gio, agora s茫o: `{}`"
is_chatting = True
kikad = 'O usu谩rio *{}* foi banido.'
notificacao = u'''
馃洝Nova Notifica莽茫o馃洝
grupo: *{}*
usu谩rio: `{}`'''
banid = u"O usu谩rio @{} foi banido."
button1 = InlineKeyboardMarkup(inline_keyboard=[[dict(text='馃挗Mundo Oi馃挗', url='https://telegram.me/joinchat/AAAAAEDDzyPty3sfOaYmjQ')]])
hp2 ='''
馃敯*Deseja ajuda em que?*馃敯
鉃栤灃鉃栤灃鉃栤灃鉃栤灃鉃栤灃
1- comandos.
2- n茫o responde.
3- outro.
鉃栤灃鉃栤灃鉃栤灃鉃栤灃鉃栤灃
clique no bot茫o para obter a ajuda desejada.'''




message_with_inline_keyboard = None



# funcao handle
def on_handle(msg):
    def response(id, response):
        bot.sendMessage(id, response, reply_to_message_id=chat_msgid, parse_mode='Markdown')
    
    
       
### BOT PARAMTS
    reply_to_message_id= msg['from']['id']
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    msg_id = msg['message_id']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    sender = msg['from']['id']
    message = msg['text'].split()
    len_msg = len(message)
    command_reply = ['/star+', '/star-', '/report', '/ban', '', ]
    adm_id = [259979813, 240658195, 262950505, 247930460, 259979813, 267379042, 305623192, 212718132]
    nome = msg['from']['first_name']
    txt = msg['text'].split(' ')
    command = msg['text']
    sender = msg['from']['id']
    
    stars = 'registro.txt'
    command_reply = ['/star+', '/star-', '/report', '/queima', '/unban', '/pull']
    commands_rp = ['/star+', '/star-', '/report', '/queima', '/unban', '/pull']   

    
    
    message_with_inline_keyboard = None


   
    
    
    
### BOT COMANDOS
    
    if texto == '/dados' or texto== "/dados@MasterCardersBot":
        bot.sendMessage(chat_id, dados.format(random.randint(1,6)), parse_mode="Markdown")
    elif txt[0] == '/diz' or texto== "/diz@MasterCardersBot":
        if len_msg > 1:
            texto = msg[u'text'].split(' ', 1)[1]
            bot.sendMessage(chat_id, texto)
    elif texto == '/total' or texto == '/total@MasterCardersBot':
        bot.sendMessage(chat_id, 'O total de menssagens deste chat 茅 *{}*'.format(msg_id), parse_mode="Markdown")
    elif  texto== '/adm' or texto== "/adm@MasterCardersBot":
        admins = bot.getChatAdministrators(chat_id)
        ListAdm= ["@%s"%adm['user']['username'] for adm in admins]
        print("lista s贸 com os usernames \n%s\n\n" %ListAdm)
        cria = ['@%s'%adm['user']['username'] for creator in admins]
        criador = " ".join(cria)
        adm_msg = "\n".join(ListAdm)
        bot.sendMessage(chat_id, """
Admins馃懃

{}

""".format(adm_msg), reply_to_message_id=msg_id)
      
        
        
    elif texto == '/game':
            try:
                msg['reply_to_message']
            except:
                r = random.randint(0,6)
                if r == 0:
                    bot.sendMessage(chat_id, 'Bang馃敨!\nUsu谩rio {} foi banido!'.format(from_username), reply_to_message_id=msg_id)
                    bot.kickChatMember(chat_id, msg['reply_to_message']['from']['id'] )
                else:
                    bot.sendMessage(chat_id, '*Click!* 馃敨')
    
    
    elif texto== "/link" or texto == "/link@MasterCardersBot":
        button1 = InlineKeyboardMarkup(inline_keyboard=[[dict(text='馃挗Mundo Oi馃挗', url='https://telegram.me/joinchat/AAAAAEDDzyPty3sfOaYmjQ')]+[dict(text='馃懃grupo oi馃懃', url='https://telegram.me/joinchat/AAAAAEBCYzxICTU2uqXwGA')]])
        bot.sendMessage(chat_id, "O nosso Canal tem suporte oficial dos nossos adms e de mim ^^", reply_markup=button1)
        bot.sendMessage(chat_id, "teste", reply_markup=button2)
    elif texto == "/guia" or texto == "/guia@MasterCardersBot":
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='馃摂| ENEM', url='http://guiadoestudante.abril.com.br/enem/')]+[dict(text='馃摍| Estudo', url='http://guiadoestudante.abril.com.br/estudo/')],[dict(text='馃摋| Profiss玫es', url='http://guiadoestudante.abril.com.br/profissoes/')]+[dict(text='馃摌| Vestibulares', url='http://guiadoestudante.abril.com.br/universidades/')],[dict(text='馃摀| GE Bolsas', url='https://bolsas.guiadoestudante.com.br/')]+[dict(text='馃摃| FIES ProUni', url='http://guiadoestudante.abril.com.br/fies-prouni/')]])
        bot.sendMessage(chat_id, "neste guia vo莽锚 encontra alguns sites de estudos...", reply_markup=markup)
    elif txt[0] == '/calcule':
        try:bot.sendMessage(chat_id, eval(txt[1]), reply_to_message_id=msg_id)
        except:bot.sendMessage(chat_id, "por favor verifique os param锚tros do c贸digo, algo n茫o est谩 certo...", reply_to_message_id=msg_id)
    elif texto == '/gensenha' or texto== "/gensenha@MasterCardersBot":
        bot.sendMessage(chat_id, senha.format(random.randint(0000,99999999)), parse_mode="Markdown")
    elif texto == '/hora' or texto== "/hora@MasterCardersBot":
        bot.sendMessage(chat_id, info_h.format(hora), parse_mode="Markdown")
    elif texto == "/data" or texto== "/data@MasterCardersBot":
        bot.sendMessage(chat_id, info_data.format(D, M, A, hora), parse_mode="Markdown")
    elif texto == "/lib" or texto == "/lib@MasterCardersBot":
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='github馃摉', url='https://github.com/nickoala/telepot')]])
        bot.sendMessage(chat_id, "Lib telepot", reply_markup=markup)
    
    
    elif texto == '/jota':
        bot.sendSticker(chat_id, "BQADAQADugUAAiXV3gaRGA4ir4SCuwI")
    elif texto == '/stop':
        bot.sendMessage(chat_id, "bot parado.")
    elif texto == '/getme' or texto== "/getme@Taylor_robot":
        bot.sendMessage(chat_id, info_id.format(from_first_name, from_username, str(from_id), msg['chat'][u'title'], chat_id))
    elif texto == "/id" or texto == "/id@MasterCardersBot":
        bot.sendMessage(chat_id, "`{}`".format(from_id), parse_mode="Markdown")
    elif texto.lower() == 'comprar':
        bot.sendMessage(chat_id, info_s.format(from_first_name), parse_mode="Markdown")
    elif texto.lower() == 'fdp':
        bot.sendMessage(chat_id, "meu pau te ama...", reply_to_message_id=msg_id)
    
    elif texto.lower() == 'vsf':
        bot.sendMessage(chat_id, "nossa! o que eu fiz pra voc锚 falar assim comigo?")
    elif texto == 'oi?':
        bot.sendMessage(chat_id, "oi! estou aqui!")
    elif texto.lower() == 'desligar':
        bot.sendMessage(chat_id, "u茅?,desligar? agora que a brincadeira tava ficando boa! ;-;")
    elif texto.lower() == 'ehis':
        bot.sendMessage(chat_id, "Aconsenho a entrar em um canal...")
    elif texto.lower() == 'porra':
        bot.sendMessage(chat_id, "Fala direito comigo,voc锚 n茫o 茅 meu pai!")
    elif texto.lower() == 'quero netflix':
        bot.sendMessage(chat_id, "N茫o estou programado para falar sobre isso")
    elif texto.lower() == 'quero ehis':
        bot.sendMessage(chat_id, "Vai ficar querendo 馃槀馃幎")
    elif texto.lower() == 'idiota':
        bot.sendMessage(chat_id, "ha ha ha,voc锚 que 茅馃檮")
    elif texto.lower() == 'kkk':
        bot.sendMessage(chat_id, "馃槀馃槀馃槀")
    elif texto.lower() == 'viado':
        bot.sendMessage(chat_id, "Vamos parar ok? voc锚 n茫o tem educa莽茫o!")
    elif texto.lower() == 'tudo bem?':
        bot.sendMessage(chat_id, "tudo sim! e com voc锚?")
    elif texto.lower() == 'como vc ta?':
        bot.sendMessage(chat_id, "estou bem rsrs,e com voc锚?")
    elif re.match(r'\bmanda ehi\b', texto.lower()):
        bot.sendMessage(chat_id, "N茫o馃槡")
    elif texto.lower() == 'nao':
        bot.sendMessage(chat_id, "...")
    elif texto == 'ki':
        bot.sendMessage(chat_id, "馃")
    elif texto.lower() == 'sim':
        bot.sendMessage(chat_id, "que bom!")
    elif texto.lower() == 'tudo bem':
        bot.sendMessage(chat_id, "que bom!")
    elif texto.lower() == 'cu' or texto == "caralho" or texto == "otario":
        bot.sendMessage(chat_id, "N茫o quero falar sobre isso,vamos mudar de assunto?")
    elif texto.lower() == 'vai tomar no cu':
        bot.sendMessage(chat_id, "Nossa! sua m茫e nao lhe deu educa莽茫o?")
    elif texto.lower() == 'Nao':
        bot.sendMessage(chat_id, "poxa,que pena.")
    elif texto.lower() == 'festa':
        bot.sendMessage(chat_id, "obaaaa! eu adoro festa!")
    elif texto.lower() == 'voce nao e bem vindo':
        bot.sendMessage(chat_id, "wow! que bad!")
    elif texto.lower() == 'quantos anos voce tem?':
        bot.sendMessage(chat_id, "eu? nem um ano ainda.")
    elif texto.lower() == 'cala a boca':
        bot.sendMessage(chat_id, "Nossa! Que grosseria! A sua m茫e n茫o lhe deu educa莽茫o?")
    elif ("merda" in texto) == 'merda':
        bot.sendMessage(chat_id, "Eitha! que maneira feia de se expressar!?")
    elif texto == '...':
        bot.sendMessage(chat_id, "馃憖")
    elif texto.lower() == 'Sexo': 
        bot.sendMessage(chat_id, "Vamos mudar de assunto?isso n茫o est谩 na minha programa莽茫o")
    elif texto.lower() == 'huehue':
        bot.sendMessage(chat_id, "Que risada escrota馃槤")
    elif texto == 'bem':
        bot.sendMessage(chat_id, "que bom!")
    elif texto.lower() == 'obg':
        bot.sendMessage(chat_id, "por nada!,estou sempre as ordens! ^^")
    elif texto.lower() == 'obrigado':
        bot.sendMessage(chat_id, "Por nada! ^^")
    elif texto == 'nada':
        bot.sendMessage(chat_id, "hum....ok!")
    elif texto.lower() == 'Bem':
        bot.sendMessage(chat_id, "que bom!")
    elif texto == 'Rs':
        bot.sendMessage(chat_id, "馃槀")
    elif texto == 'loko':
        bot.sendMessage(chat_id, "馃槀")
    
    sender = msg['from']['id']
    
    if texto == '/report':
                if msg['reply_to_message']['from']['id'] not in adm_id:
                    bot.sendMessage(chat_id, u'''
馃懁Usu谩rio %s reportado para os administradores.

馃洝ID: %s''' % ('@' + msg['reply_to_message']['from']['username'], msg['reply_to_message']['from']['id']))
                    reply_msg = msg['reply_to_message']['text']
                    bot.sendMessage(-1001096550309, u'''
馃懁O usu谩rio %s foi reportado


馃洝ID: %s ''' % ('@' + msg['reply_to_message']['from']['username'], msg['reply_to_message']['from']['id']))
                    bot.sendMessage(-1001096550309, u'''
馃洝Mensagem reportada馃洝

馃搩Mensagem: _%s_

馃懃Grupo: *%s*''' % (reply_msg, msg['chat']['title']), parse_mode="Markdown")
                else:
                    bot.sendMessage(chat_id, 'Voc锚 n茫o pode reportar administradores!')
    
    
    
    elif texto.lower() 
