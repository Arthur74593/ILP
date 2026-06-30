
import pygame
import random
import math
from enum import Enum
 
print("📦 Carregando bibliotecas...")
 
# Inicializar Pygame
pygame.init()
print("✅ Pygame inicializado!")
 
# Configurações da Tela
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
 
# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (200, 0, 255)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
 
# Estados do Jogo
class GameState(Enum):
    PLAYING = 1
    GAME_OVER = 2
    WIN = 3
    MENU = 4
 
class Particle:
    """Efeito visual de partículas"""
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        self.vy += 0.1  # Gravidade
    
    def draw(self, surface):
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        size = int(5 * (self.lifetime / self.max_lifetime))
        if size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), size)
    
    def is_alive(self):
        return self.lifetime > 0
 
class Thief:
    """Personagem Ladrão - Controlado pelo jogador"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.speed = 5
        self.vx = 0
        self.vy = 0
        self.mega_brain_active = False
        self.mega_brain_cooldown = 0
        self.mega_brain_duration = 0
        self.dash_cooldown = 0
        self.score = 0
        self.health = 100
        self.treasure_collected = 0
    
    def update(self, keys, cop, coins):
        # Movimento básico
        self.vx = 0
        self.vy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = self.speed
        
        # Mega Brain - Inteligência Máxima (Espaço)
        if keys[pygame.K_SPACE] and self.mega_brain_cooldown == 0:
            self.mega_brain_active = True
            self.mega_brain_duration = 300
            self.mega_brain_cooldown = 500
            self.speed = 8
        
        # Dash (Shift)
        if keys[pygame.K_LSHIFT] and self.dash_cooldown == 0:
            self.x += self.vx * 5
            self.y += self.vy * 5
            self.dash_cooldown = 120
        
        # Atualizar Mega Brain
        if self.mega_brain_active:
            self.mega_brain_duration -= 1
            self.speed = 8
            if self.mega_brain_duration <= 0:
                self.mega_brain_active = False
                self.speed = 5
        else:
            self.speed = 5
        
        # Cooldowns
        if self.mega_brain_cooldown > 0:
            self.mega_brain_cooldown -= 1
        if self.dash_cooldown > 0:
            self.dash_cooldown -= 1
        
        # Aplicar movimento
        self.x += self.vx
        self.y += self.vy
        
        # Limites da tela
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))
        
        # Coletar moedas (tesouro)
        for coin in coins[:]:
            if self.check_collision(coin):
                coins.remove(coin)
                self.treasure_collected += 1
                self.score += 100
    
    def check_collision(self, obj):
        """Verifica colisão com outro objeto"""
        return (self.x < obj.x + obj.width and
                self.x + self.width > obj.x and
                self.y < obj.y + obj.height and
                self.y + self.height > obj.y)
    
    def draw(self, surface):
        # Corpo do ladrão
        if self.mega_brain_active:
            color = PURPLE
            pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))
            # Aura do Mega Brain
            pygame.draw.circle(surface, (150, 0, 255), 
                              (int(self.x + self.width//2), int(self.y + self.height//2)), 
                              30, 3)
        else:
            pygame.draw.rect(surface, YELLOW, (self.x, self.y, self.width, self.height))
        
        # Olhos
        pygame.draw.circle(surface, BLACK, (int(self.x + 8), int(self.y + 12)), 3)
        pygame.draw.circle(surface, BLACK, (int(self.x + 22), int(self.y + 12)), 3)
        
        # Máscara
        pygame.draw.line(surface, BLACK, (int(self.x + 8), int(self.y + 15)), 
                        (int(self.x + 22), int(self.y + 15)), 2)
 
class Cop:
    """Personagem Policial - IA inteligente"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 35
        self.height = 40
        self.speed = 3.5
        self.vx = 0
        self.vy = 0
        self.mode = "patrol"  # patrol, chase
        self.patrol_direction = 1
        self.last_thief_x = None
        self.last_thief_y = None
    
    def update(self, thief, walls):
        # Mega Brain do Cop - Inteligência aumentada
        distance_to_thief = math.sqrt((self.x - thief.x)**2 + (self.y - thief.y)**2)
        
        # Se o ladrão está visível e próximo
        if distance_to_thief < 300:
            self.mode = "chase"
            # IA inteligente - rastreia o ladrão
            dx = thief.x - self.x
            dy = thief.y - self.y
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist > 0:
                self.vx = (dx / dist) * self.speed
                self.vy = (dy / dist) * self.speed
            
            # Aumenta velocidade se o ladrão usar Mega Brain
            if thief.mega_brain_active:
                self.speed = 5
            else:
                self.speed = 3.5
        else:
            self.mode = "patrol"
            self.speed = 2
            # Patrulha
            self.x += self.patrol_direction * self.speed
            if self.x <= 50 or self.x >= SCREEN_WIDTH - 50:
                self.patrol_direction *= -1
            self.vy = 0
        
        # Aplicar movimento
        self.x += self.vx
        self.y += self.vy
        
        # Limites
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))
    
    def check_collision(self, obj):
        """Verifica colisão"""
        return (self.x < obj.x + obj.width and
                self.x + self.width > obj.x and
                self.y < obj.y + obj.height and
                self.y + self.height > obj.y)
    
    def draw(self, surface):
        # Corpo do policial
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.width, self.height))
        
        # Distintivo
        pygame.draw.circle(surface, YELLOW, (int(self.x + self.width//2), int(self.y + 20)), 5)
        
        # Olhos
        pygame.draw.circle(surface, WHITE, (int(self.x + 10), int(self.y + 12)), 3)
        pygame.draw.circle(surface, WHITE, (int(self.x + 25), int(self.y + 12)), 3)
        pygame.draw.circle(surface, BLACK, (int(self.x + 10), int(self.y + 12)), 1)
        pygame.draw.circle(surface, BLACK, (int(self.x + 25), int(self.y + 12)), 1)
        
        # Chapéu
        pygame.draw.polygon(surface, BLACK, [
            (int(self.x + 5), int(self.y)),
            (int(self.x + 30), int(self.y)),
            (int(self.x + 32), int(self.y - 5)),
            (int(self.x + 3), int(self.y - 5))
        ])
 
class Coin:
    """Moedas/Tesouro para coletar"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.rotation = 0
    
    def update(self):
        self.rotation += 5
    
    def draw(self, surface):
        pygame.draw.circle(surface, ORANGE, (int(self.x + self.width//2), int(self.y + self.height//2)), 8)
        pygame.draw.circle(surface, YELLOW, (int(self.x + self.width//2), int(self.y + self.height//2)), 5)
 
class Game:
    """Classe principal do jogo"""
    def __init__(self):
        print("🎮 Criando janela do jogo...")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🎮 COP vs THIEF - Mega Brain Edition 🧠")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 20)
        print("✅ Janela criada com sucesso!")
        
        self.reset_game()
    
    def reset_game(self):
        """Reinicia o jogo"""
        self.state = GameState.PLAYING
        self.thief = Thief(100, 100)
        self.cop = Cop(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100)
        self.coins = []
        self.particles = []
        self.spawn_coins(15)
        self.game_timer = 0
    
    def spawn_coins(self, count):
        """Cria moedas aleatórias na tela"""
        for _ in range(count):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            self.coins.append(Coin(x, y))
    
    def create_particles(self, x, y, color, count=10):
        """Cria efeito de partículas"""
        for _ in range(count):
            vx = random.uniform(-3, 3)
            vy = random.uniform(-3, 3)
            self.particles.append(Particle(x, y, vx, vy, color, 30))
    
    def handle_events(self):
        """Trata eventos"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.state != GameState.PLAYING:
                    self.reset_game()
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        """Atualiza lógica do jogo"""
        if self.state != GameState.PLAYING:
            return
        
        self.game_timer += 1
        keys = pygame.key.get_pressed()
        
        # Atualizar personagens
        self.thief.update(keys, self.cop, self.coins)
        self.cop.update(self.thief, None)
        
        # Atualizar moedas
        for coin in self.coins:
            coin.update()
        
        # Atualizar partículas
        for particle in self.particles[:]:
            particle.update()
            if not particle.is_alive():
                self.particles.remove(particle)
        
        # Gerar novas moedas
        if len(self.coins) < 10 and self.game_timer % 60 == 0:
            self.spawn_coins(1)
        
        # Verificar colisão: Cop vs Thief
        if self.cop.check_collision(self.thief):
            if self.thief.mega_brain_active:
                # Ladrão escapa com Mega Brain
                self.create_particles(self.thief.x, self.thief.y, PURPLE, 20)
                self.thief.x = random.randint(50, SCREEN_WIDTH - 50)
                self.thief.y = random.randint(50, SCREEN_HEIGHT - 50)
                self.thief.score += 200
            else:
                # Policial captura
                self.state = GameState.GAME_OVER
                self.create_particles(self.cop.x, self.cop.y, BLUE, 30)
        
        # Condição de vitória
        if self.thief.treasure_collected >= 15:
            self.state = GameState.WIN
    
    def draw(self):
        """Desenha tudo na tela"""
        self.screen.fill(BLACK)
        
        # Grade de fundo
        for x in range(0, SCREEN_WIDTH, 50):
            pygame.draw.line(self.screen, (30, 30, 30), (x, 0), (x, SCREEN_HEIGHT), 1)
        for y in range(0, SCREEN_HEIGHT, 50):
            pygame.draw.line(self.screen, (30, 30, 30), (0, y), (SCREEN_WIDTH, y), 1)
        
        if self.state == GameState.PLAYING:
            # Desenhar moedas
            for coin in self.coins:
                coin.draw(self.screen)
            
            # Desenhar partículas
            for particle in self.particles:
                particle.draw(self.screen)
            
            # Desenhar personagens
            self.thief.draw(self.screen)
            self.cop.draw(self.screen)
            
            # Interface HUD
            self.draw_hud()
        
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()
        
        elif self.state == GameState.WIN:
            self.draw_win()
        
        pygame.display.flip()
    
    def draw_hud(self):
        """Desenha interface do jogo"""
        # Score
        score_text = self.font_medium.render(f"Score: {self.thief.score}", True, YELLOW)
        self.screen.blit(score_text, (10, 10))
        
        # Tesouro coletado
        treasure_text = self.font_medium.render(f"Tesouro: {self.thief.treasure_collected}/15", True, ORANGE)
        self.screen.blit(treasure_text, (10, 50))
        
        # Status Mega Brain
        if self.thief.mega_brain_cooldown > 0:
            cooldown_percent = (self.thief.mega_brain_cooldown / 500) * 100
            cooldown_text = self.font_small.render(f"Mega Brain Cooldown: {int(cooldown_percent)}%", True, PURPLE)
        else:
            cooldown_text = self.font_small.render("Mega Brain: PRONTO! (Espaco)", True, CYAN)
        self.screen.blit(cooldown_text, (10, 90))
        
        # Status Dash
        if self.thief.dash_cooldown > 0:
            dash_text = self.font_small.render("Dash: Em Cooldown", True, RED)
        else:
            dash_text = self.font_small.render("Dash: PRONTO! (Shift)", True, GREEN)
        self.screen.blit(dash_text, (10, 115))
        
        # Modo do Cop
        mode_color = CYAN if self.cop.mode == "chase" else GREEN
        mode_text = self.font_small.render(f"Policial: {self.cop.mode.upper()}", True, mode_color)
        self.screen.blit(mode_text, (SCREEN_WIDTH - 250, 10))
        
        # Controles
        help_text = self.font_small.render("WASD/Setas: Mover | Espaco: Mega Brain | Shift: Dash", True, WHITE)
        self.screen.blit(help_text, (SCREEN_WIDTH - 500, SCREEN_HEIGHT - 30))
    
    def draw_game_over(self):
        """Tela de Game Over"""
        # Overlay escuro
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Textos
        game_over_text = self.font_large.render("VOCE FOI CAPTURADO!", True, RED)
        score_text = self.font_medium.render(f"Score Final: {self.thief.score}", True, YELLOW)
        treasure_text = self.font_medium.render(f"Tesouro Coletado: {self.thief.treasure_collected}/15", True, ORANGE)
        restart_text = self.font_small.render("Pressione R para Recomecar ou ESC para Sair", True, WHITE)
        
        self.screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 150))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 280))
        self.screen.blit(treasure_text, (SCREEN_WIDTH//2 - treasure_text.get_width()//2, 340))
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 480))
    
    def draw_win(self):
        """Tela de Vitória"""
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        win_text = self.font_large.render("VOCE ESCAPOU COM O TESOURO!", True, GREEN)
        score_text = self.font_medium.render(f"Score Final: {self.thief.score}", True, YELLOW)
        mega_text = self.font_medium.render("Mega Brain foi essencial para sua vitoria!", True, PURPLE)
        restart_text = self.font_small.render("Pressione R para Jogar Novamente ou ESC para Sair", True, WHITE)
        
        self.screen.blit(win_text, (SCREEN_WIDTH//2 - win_text.get_width()//2, 150))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 280))
        self.screen.blit(mega_text, (SCREEN_WIDTH//2 - mega_text.get_width()//2, 340))
        self.screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 480))
    
    def run(self):
        """Loop principal do jogo"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        print("✅ Jogo encerrado!")
 
# Executar jogo
if __name__ == "__main__":
    try:
        print("\n" + "="*50)
        print("🎮 COP vs THIEF - Mega Brain Edition")
        print("="*50 + "\n")
        game = Game()
        print("✅ Tudo pronto! Iniciando jogo...\n")
        game.run()
    except Exception as e:
        print(f"\n❌ ERRO ao executar o jogo: {e}")
        import traceback
        traceback.print_exc()
        input("\nPressione ENTER para fechar...")
 