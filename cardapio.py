import time
import os
import random
from datetime import datetime

class PedidoIfood:
    def __init__(self):
        self.cardapio = {
            1: {"nome": "🍔 Hambúrguer Artesanal", "preco": 33.90, "tempo": 15},
            2: {"nome": "🍔 X-tudo", "preco": 45.90, "tempo": 35},
            3: {"nome": "🍔 X-Salada", "preco": 20.90, "tempo": 15},
            4: {"nome": "🍔 X-Bacon Egg", "preco": 35.90, "tempo": 30},
            5: {"nome": "🍔 X-Egg", "preco": 28.90, "tempo": 20},
            6: {"nome": "🥤 Refrigerante", "preco": 6.90, "tempo": 1}
        }
        self.pedido = []
        self.total = 0
        self.status = "Aguardando pedido..."
        self.historico_status = []
        self.tempo_inicio = None
        # Adicionando dicionário para dados do cliente
        self.dados_cliente = {
            "nome": "",
            "endereco": "",
            "telefone": "",
            "observacao": ""
        }
    
    def limpar_tela(self):
        """Limpa o terminal para melhor visualização"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_cardapio(self):
        """Exibe o cardápio formatado"""
        self.limpar_tela()
        print("=" * 60)
        print("🍽️  Hadson Lanchonete - CARDÁPIO  🍽️")
        print("=" * 60)
        print(f"{'Código':^10} {'Item':^30} {'Preço':^20}")
        print("-" * 60)
        
        for codigo, item in self.cardapio.items():
            print(f"{codigo:^10} {item['nome']:^30} R${item['preco']:>17.2f}")
        print("=" * 60)
    
    def coletar_dados_cliente(self):
        """Coleta os dados do cliente antes de finalizar o pedido"""
        self.limpar_tela()
        print("=" * 60)
        print("📋 DADOS DO CLIENTE 📋")
        print("=" * 60)
        
        print("\nPor favor, preencha seus dados para entrega:")
        print("-" * 60)
        
        # Coleta dos dados com validação
        while True:
            nome = input("\n👤 Nome completo: ").strip()
            if nome:
                self.dados_cliente["nome"] = nome
                break
            else:
                print("❌ Nome é obrigatório! Tente novamente.")
        
        while True:
            endereco = input("📍 Endereço completo (Rua, Número, Bairro): ").strip()
            if endereco:
                self.dados_cliente["endereco"] = endereco
                break
            else:
                print("❌ Endereço é obrigatório! Tente novamente.")
        
        while True:
            telefone = input("📱 Telefone para contato (com DDD): ").strip()
            if telefone:
                self.dados_cliente["telefone"] = telefone
                break
            else:
                print("❌ Telefone é obrigatório! Tente novamente.")
        
        # Observação opcional
        observacao = input("📝 Observação (ponto de referência, etc.): ").strip()
        if observacao:
            self.dados_cliente["observacao"] = observacao
        
        # Confirmação dos dados
        print("\n" + "=" * 60)
        print("✅ CONFIRME SEUS DADOS:")
        print("-" * 60)
        print(f"👤 Nome: {self.dados_cliente['nome']}")
        print(f"📍 Endereço: {self.dados_cliente['endereco']}")
        print(f"📱 Telefone: {self.dados_cliente['telefone']}")
        if self.dados_cliente['observacao']:
            print(f"📝 Observação: {self.dados_cliente['observacao']}")
        
        print("\n" + "=" * 60)
        confirmacao = input("Todos os dados estão corretos? (S/N): ").upper().strip()
        
        if confirmacao == "S":
            print("\n✅ Dados confirmados! Enviando pedido...")
            time.sleep(1)
            return True
        else:
            print("\n🔄 Vamos corrigir os dados...")
            time.sleep(1)
            # Limpa os dados para recolher novamente
            self.dados_cliente = {
                "nome": "",
                "endereco": "",
                "telefone": "",
                "observacao": ""
            }
            return self.coletar_dados_cliente()
    
    def fazer_pedido(self):
        """Permite ao usuário fazer o pedido"""
        while True:
            self.mostrar_cardapio()
            print("\n📝 Seu pedido atual:")
            if self.pedido:
                for item in self.pedido:
                    print(f"  - {item['nome']} (R${item['preco']:.2f})")
                print(f"  Total: R${self.total:.2f}")
            else:
                print("  (Carrinho vazio)")
            
            print("\n" + "-" * 60)
            print("Opções:")
            print("  [1-6] - Adicionar item ao pedido")
            print("  [7]   - Remover último item")
            print("  [8]   - Limpar carrinho")
            print("  [9]   - Finalizar pedido e enviar")
            print("  [0]   - Cancelar e sair")
            
            try:
                opcao = int(input("\n👉 Escolha uma opção: "))
                
                if opcao == 0:
                    print("\n❌ Pedido cancelado. Volte sempre!")
                    return False
                
                elif opcao == 9:
                    if not self.pedido:
                        print("\n⚠️ Carrinho vazio! Adicione itens primeiro.")
                        time.sleep(2)
                    else:
                        # Antes de finalizar, coleta os dados do cliente
                        print("\n📋 Antes de finalizar, precisamos dos seus dados...")
                        time.sleep(1)
                        if self.coletar_dados_cliente():
                            return True
                        # Se os dados não foram confirmados, volta ao menu
                        continue
                
                elif opcao == 8:
                    self.pedido = []
                    self.total = 0
                    print("\n🗑️ Carrinho limpo!")
                    time.sleep(1)
                
                elif opcao == 7:
                    if self.pedido:
                        removido = self.pedido.pop()
                        self.total -= removido['preco']
                        self.total = round(self.total, 2)
                        print(f"\n➖ Removido: {removido['nome']}")
                        time.sleep(1)
                    else:
                        print("\n⚠️ Carrinho vazio!")
                        time.sleep(1)
                
                elif opcao in self.cardapio:
                    item = self.cardapio[opcao]
                    self.pedido.append(item)
                    self.total += item['preco']
                    self.total = round(self.total, 2)
                    print(f"\n✅ Adicionado: {item['nome']} - R${item['preco']:.2f}")
                    print(f"   Total atual: R${self.total:.2f}")
                    time.sleep(1)
                
                else:
                    print("\n❌ Opção inválida!")
                    time.sleep(1)
                    
            except ValueError:
                print("\n❌ Digite um número válido!")
                time.sleep(1)
    
    def calcular_tempo_entrega(self):
        """Calcula o tempo estimado baseado nos itens e endereço"""
        tempo_total = sum(item['tempo'] for item in self.pedido)
        # Adiciona tempo de preparo baseado no número de itens
        tempo_total += len(self.pedido) * 2
        
        # Adiciona tempo baseado na localização (simulação mais realista)
        if "centro" in self.dados_cliente['endereco'].lower():
            tempo_total += 3  # Trânsito no centro
        if "apartamento" in self.dados_cliente['endereco'].lower():
            tempo_total += 2  # Tempo extra para apartamento
        
        # Variabilidade aleatória (simula trânsito)
        return random.randint(tempo_total, tempo_total + 5)
    
    def simular_entrega(self, tempo_estimado):
        """Simula o acompanhamento em tempo real"""
        self.tempo_inicio = datetime.now()
        self.status = "🟡 Pedido recebido"
        self.historico_status.append(self.status)
        
        # Mostra confirmação do pedido com dados do cliente
        print("\n" + "=" * 60)
        print("📦 PEDIDO RECEBIDO COM SUCESSO!")
        print("=" * 60)
        print(f"\n👤 Cliente: {self.dados_cliente['nome']}")
        print(f"📍 Entrega: {self.dados_cliente['endereco']}")
        print(f"📱 Contato: {self.dados_cliente['telefone']}")
        if self.dados_cliente['observacao']:
            print(f"📝 Obs: {self.dados_cliente['observacao']}")
        print("\n" + "=" * 60)
        time.sleep(3)
        
        # Define os estágios da entrega
        estagios = [
            ("🟡 Pedido recebido", f"Olá {self.dados_cliente['nome']}! Seu pedido foi confirmado!", 20),
            ("🟠 Em preparo", "Estamos preparando seu pedido, aguarde alguns instantes...", 40),
            ("🟢 Pronto para entrega", "Pedido pronto! Aguardando entregador...", 60),
            ("🟣 Entregador a caminho", f"Entregador {random.choice(['João', 'Maria', 'Carlos', 'Ana'])} saiu para entrega!", 80),
            ("🔵 Próximo do destino", "Entregador está próximo! 🚗", 90),
            ("🟢 Entregue", "Pedido entregue com sucesso! ✅", 100)
        ]
        
        progresso = 0
        estagio_atual = 0
        
        while progresso < 100:
            self.limpar_tela()
            print("=" * 60)
            print("🚚 ACOMPANHAMENTO EM TEMPO REAL 🚚")
            print("=" * 60)
            
            # Mostra dados do cliente
            print(f"\n👤 Cliente: {self.dados_cliente['nome']}")
            print(f"📍 Destino: {self.dados_cliente['endereco']}")
            
            # Mostra o pedido
            print("\n📦 Seu pedido:")
            for i, item in enumerate(self.pedido, 1):
                print(f"  {i}. {item['nome']}")
            print(f"  Total: R${self.total:.2f}")
            
            # Mostra status atual
            status_atual, mensagem, progresso_alvo = estagios[estagio_atual]
            
            print(f"\n📊 Status: {status_atual}")
            print(f"📝 {mensagem}")
            
            # Calcula tempo decorrido
            tempo_decorrido = (datetime.now() - self.tempo_inicio).seconds
            minutos_restantes = max(0, tempo_estimado - tempo_decorrido)
            
            # Barra de progresso
            print(f"\n{'=' * 60}")
            print(f"Progresso: [{self.criar_barra_progresso(progresso)}] {progresso}%")
            print(f"⏱️ Tempo estimado restante: {minutos_restantes} minuto(s)")
            print(f"📍 Distância: {self.calcular_distancia(progresso)} km")
            
            print("\n" + "=" * 60)
            print("Pressione Ctrl+C para sair do acompanhamento")
            
            # Atualiza progresso
            progresso += random.randint(1, 4)
            progresso = min(progresso, 100)
            
            # Avança para próximo estágio
            if estagio_atual < len(estagios) - 1 and progresso >= estagios[estagio_atual + 1][2]:
                estagio_atual += 1
                self.status = estagios[estagio_atual][0]
                self.historico_status.append(self.status)
                
                # Efeito sonoro visual
                if "Entregador" in self.status:
                    print("\n" + "🔔" * 5 + " ENTREGADOR A CAMINHO! " + "🔔" * 5)
                    print(f"   O entregador está indo para: {self.dados_cliente['endereco']}")
                    time.sleep(1)
                elif "Próximo" in self.status:
                    print("\n" + "📍" * 5 + " ENTREGADOR ESTÁ PRÓXIMO! " + "📍" * 5)
                    time.sleep(1)
            
            # Verifica se chegou ao destino
            if progresso >= 100:
                self.status = "✅ Entregue!"
                self.historico_status.append(self.status)
                print("\n" + "🎉" * 10 + " PEDIDO ENTREGUE! " + "🎉" * 10)
                print(f"\n🌟 Obrigado por pedir na Hadson Lanchonete, {self.dados_cliente['nome']}! 🌟")
                print(f"\n⏱️ Tempo total: {tempo_decorrido} minuto(s)")
                break
            
            time.sleep(random.randint(2, 4))
    
    def criar_barra_progresso(self, progresso):
        """Cria uma barra de progresso visual"""
        largura = 30
        preenchido = int(largura * progresso / 100)
        vazio = largura - preenchido
        return "█" * preenchido + "░" * vazio
    
    def calcular_distancia(self, progresso):
        """Simula a distância restante"""
        distancia_total = 10.0
        distancia_restante = distancia_total * (100 - progresso) / 100
        return round(distancia_restante, 1)
    
    def mostrar_resumo(self):
        """Mostra resumo final do pedido"""
        self.limpar_tela()
        print("=" * 60)
        print("📋 RESUMO DO PEDIDO 📋")
        print("=" * 60)
        
        # Mostra dados do cliente
        print("\n👤 Dados do cliente:")
        print(f"  Nome: {self.dados_cliente['nome']}")
        print(f"  Endereço: {self.dados_cliente['endereco']}")
        print(f"  Telefone: {self.dados_cliente['telefone']}")
        if self.dados_cliente['observacao']:
            print(f"  Observação: {self.dados_cliente['observacao']}")
        
        print("\n📦 Itens pedidos:")
        for i, item in enumerate(self.pedido, 1):
            print(f"  {i}. {item['nome']} - R${item['preco']:.2f}")
        
        print(f"\n💰 Total: R${self.total:.2f}")
        
        print("\n📊 Histórico de status:")
        for status in self.historico_status:
            print(f"  • {status}")
        
        print("\n" + "=" * 60)
        print(f"🌟 Obrigado por usar a Hadson Lanchonete, {self.dados_cliente['nome']}! 🌟")
        print("=" * 60)

def main():
    """Função principal do programa"""
    pedido_ifood = PedidoIfood()
    
    print("=" * 60)
    print("🍽️ BEM-VINDO À HADSON LANCHONETE 🍽️")
    print("=" * 60)
    print("\nFaça seu pedido e acompanhe em tempo real!")
    print("= " * 30)
    time.sleep(2)
    
    # Fazer o pedido
    if pedido_ifood.fazer_pedido():
        # Calcular tempo de entrega
        tempo_estimado = pedido_ifood.calcular_tempo_entrega()
        
        print(f"\n⏱️ Tempo estimado: {tempo_estimado} minutos")
        print("\n🔄 Iniciando acompanhamento...")
        time.sleep(2)
        
        # Simular entrega
        try:
            pedido_ifood.simular_entrega(tempo_estimado)
            pedido_ifood.mostrar_resumo()
        except KeyboardInterrupt:
            print("\n\n⏹️ Acompanhamento interrompido pelo usuário.")
            print("📦 Último status: " + pedido_ifood.status)
            pedido_ifood.mostrar_resumo()
    else:
        print(f"\n👋 Até logo, {pedido_ifood.dados_cliente['nome'] if pedido_ifood.dados_cliente['nome'] else 'cliente'}!")

if __name__ == "__main__":
    main()