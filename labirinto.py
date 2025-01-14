import time

class Labirinto:
    def __init__(self, tempo_real_minutos, tempo_jogo_horas):
        self.tempo_real_segundos = tempo_real_minutos * 60
        self.tempo_jogo_horas = tempo_jogo_horas
        self.tempo_restante = self.tempo_real_segundos
        self.labirinto_fechado = False

    def iniciar_tempo(self):
        print("\n\033[1;93mO labirinto começa a se fechar! Você tem 3 horas no jogo (30 minutos na vida real) para encontrar a saída!\033[m")
        start_time = time.time()
        while self.tempo_restante > 0:
            current_time = time.time()
            elapsed = current_time - start_time
            self.tempo_restante = max(self.tempo_real_segundos - elapsed, 0)

            if int(self.tempo_restante) % 300 == 0 and int(self.tempo_restante) != 0:
                print(f"Tempo restante: {int(self.tempo_restante // 60)} minutos (vida real).")
            time.sleep(0.5)  # Pequenos intervalos para evitar excesso de uso de CPU

        self.labirinto_fechado = True
        print("\033[1;91mO labirinto se fechou! Prepare-se para o desafio final.\033[m")
