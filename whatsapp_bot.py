from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import json
import time
from datetime import datetime

app = Flask(__name__)

# Dicionário para armazenar sessões dos clientes
sessoes = {}

# Cardápio (copiado do seu código)
cardapio = {
    1: {"nome": "🍔 Hambúrguer Artesanal", "preco": 33.90, "tempo": 15},
    2: {"nome": "🍔 X-tudo", "preco": 45.90, "tempo": 35},
    3: {"nome": "🍔 X-Salada", "preco": 20.90, "tempo": 15},
    4: {"nome": "🍔 X-Bacon Egg", "preco": 35.90, "tempo": 30},
    5: {"nome": "🍔 X-Egg", "preco": 28.90, "tempo": 20},
    6: {"nome": "🥤 Refrigerante", "preco": 6.90, "tempo": 1}
}

@app.route("/webhook", methods=['POST'])
def webhook():
    # Pega os dados da mensagem recebida
    numero_cliente = request.values.get('From', '')
    mensagem = request.values.get('Body', '').strip().lower()
    
    # Inicializa sessão do cliente se não existir
    if numero_cliente not in sessoes:
        sessoes[numero_cliente] = {
            'pedido': [],
            'total': 0,
            'estagio': 'menu',
            'dados_cliente': {}
        }
    
    sessao = sessoes[numero_cliente]
    resp = MessagingResponse()
    
    # Processa a mensagem baseada no estágio
    if mensagem == 'cardapio' or mensagem == 'menu':
        texto_cardapio = "🍽️ *HADSON LANCHONETE* 🍽️\n\n"
        texto_cardapio += "📋 *CARDÁPIO:*\n"
        texto_cardapio += "=" * 30 + "\n\n"
        
        for codigo, item in cardapio.items():
            texto_cardapio += f"*{codigo}* - {item['nome']}\n"
            texto_cardapio += f"   R$ {item['preco']:.2f}\n\n"
        
        texto_cardapio += "\n📝 *Como pedir:*\n"
        texto_cardapio += "Digite o *número* do item para adicionar\n"
        texto_cardapio += "Digite *carrinho* para ver seu pedido\n"
        texto_cardapio += "Digite *finalizar* para enviar o pedido\n"
        texto_cardapio += "Digite *limpar* para limpar o carrinho\n"
        texto_cardapio += "Digite *ajuda* para ver os comandos"
        
        resp.message(texto_cardapio)
    
    elif mensagem == 'carrinho':
        if not sessao['pedido']:
            resp.message("🛒 Seu carrinho está vazio!\n\nDigite *cardapio* para ver as opções.")
        else:
            texto_carrinho = "🛒 *SEU CARRINHO:*\n\n"
            for i, item in enumerate(sessao['pedido'], 1):
                texto_carrinho += f"{i}. {item['nome']}\n"
                texto_carrinho += f"   R$ {item['preco']:.2f}\n\n"
            texto_carrinho += f"*Total: R$ {sessao['total']:.2f}*"
            resp.message(texto_carrinho)
    
    elif mensagem == 'limpar':
        sessao['pedido'] = []
        sessao['total'] = 0
        resp.message("🗑️ Carrinho limpo com sucesso!\n\nDigite *cardapio* para ver as opções.")
    
    elif mensagem == 'finalizar':
        if not sessao['pedido']:
            resp.message("❌ Seu carrinho está vazio!\n\nDigite *cardapio* para adicionar itens.")
        else:
            sessao['estagio'] = 'endereco'
            resp.message("📋 *Vamos finalizar seu pedido!*\n\nPor favor, digite seu *nome completo*:")
    
    elif mensagem == 'ajuda' or mensagem == 'help':
        texto_ajuda = "🤖 *COMANDOS DISPONÍVEIS:*\n\n"
        texto_ajuda += "📋 *cardapio* - Ver o cardápio\n"
        texto_ajuda += "🛒 *carrinho* - Ver seu pedido\n"
        texto_ajuda += "🗑️ *limpar* - Limpar o carrinho\n"
        texto_ajuda += "✅ *finalizar* - Enviar o pedido\n"
        texto_ajuda += "❓ *ajuda* - Ver estes comandos"
        resp.message(texto_ajuda)
    
    # Processa números (adicionar itens ao carrinho)
    elif mensagem.isdigit() and int(mensagem) in cardapio:
        codigo = int(mensagem)
        item = cardapio[codigo]
        sessao['pedido'].append(item)
        sessao['total'] += item['preco']
        sessao['total'] = round(sessao['total'], 2)
        resp.message(f"✅ *Adicionado:* {item['nome']}\n💰 Total: R$ {sessao['total']:.2f}")
    
    # Processa o estágio de coleta de dados
    elif sessao['estagio'] == 'endereco':
        # Salva o nome do cliente
        sessao['dados_cliente']['nome'] = mensagem.title()
        sessao['estagio'] = 'telefone'
        resp.message(f"👤 Nome salvo: *{mensagem.title()}*\n\nAgora, digite seu *endereço completo*:")
    
    elif sessao['estagio'] == 'telefone':
        sessao['dados_cliente']['endereco'] = mensagem
        sessao['estagio'] = 'confirmar'
        
        # Mostra resumo para confirmar
        resumo = "✅ *CONFIRME SEUS DADOS:*\n\n"
        resumo += f"👤 *Nome:* {sessao['dados_cliente']['nome']}\n"
        resumo += f"📍 *Endereço:* {sessao['dados_cliente']['endereco']}\n\n"
        resumo += "📦 *Seu pedido:*\n"
        for item in sessao['pedido']:
            resumo += f"• {item['nome']}\n"
        resumo += f"\n💰 *Total: R$ {sessao['total']:.2f}*\n\n"
        resumo += "Digite *confirmar* para enviar ou *cancelar* para desistir"
        resp.message(resumo)
    
    elif sessao['estagio'] == 'confirmar':
        if mensagem == 'confirmar':
            resp.message("🎉 *PEDIDO CONFIRMADO!*\n\n"
                        f"👤 *Cliente:* {sessao['dados_cliente']['nome']}\n"
                        f"📍 *Entrega:* {sessao['dados_cliente']['endereco']}\n\n"
                        "🚚 Seu pedido está sendo preparado!\n"
                        "Aguardamos sua avaliação após a entrega!")
            
            # Reseta a sessão após finalizar
            sessao['pedido'] = []
            sessao['total'] = 0
            sessao['estagio'] = 'menu'
            sessao['dados_cliente'] = {}
            
        elif mensagem == 'cancelar':
            sessao['pedido'] = []
            sessao['total'] = 0
            sessao['estagio'] = 'menu'
            sessao['dados_cliente'] = {}
            resp.message("❌ Pedido cancelado.\n\nDigite *cardapio* para fazer um novo pedido.")
        else:
            resp.message("❌ Digite *confirmar* para enviar ou *cancelar* para desistir.")
    
    else:
        resp.message("❌ Comando não reconhecido!\n\n"
                    "Digite *cardapio* para ver o menu\n"
                    "Digite *ajuda* para ver todos os comandos")
    
    return Response(str(resp), mimetype='text/xml')

@app.route("/", methods=['GET'])
def home():
    return "🤖 Bot WhatsApp - Hadson Lanchonete está rodando!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)