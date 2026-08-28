class PartidoEnVivo:
    def __init__(self, nombre_local, nombre_visitante, momio_pregame_local, momio_pregame_visitante):
        self.nombre_local =nombre_local
        self.nombre_visitante = nombre_visitante
        self.momio_pregame_local =momio_pregame_local
        self.momio_pregame_visitante = momio_pregame_visitante
        self.marcador_local = 0
        self.marcador_visitante = 0
        self.tiempo_restante = "Q1 15:00"
        self.momio_actual_local = self.momio_pregame_local
        self.momio_actual_visitante = self.momio_pregame_visitante
        self.ya_alertado = False
        
        
    def actualizar_datos(self, marcador_local_actualizado, marcador_visitante_actualizado, tiempo_restante_actualizado, 
                         momio_actualizado_local, momio_actualizado_visitante):
        
        self.marcador_local = marcador_local_actualizado
        self.marcador_visitante = marcador_visitante_actualizado
        self.tiempo_restante = tiempo_restante_actualizado
        self.momio_actual_local = momio_actualizado_local
        self.momio_actual_visitante = momio_actualizado_visitante
        
        
    def verificar_alerta_valor(self):
        
        
        if self.momio_pregame_local < self.momio_pregame_visitante:
            
            diferencia = self.marcador_visitante - self.marcador_local
            
            
            if diferencia >= 7 and diferencia <= 17 and self.momio_actual_local > 105 and self.momio_actual_local <= 400 and not self.ya_alertado:
                self.ya_alertado = True
                return True
            
            if diferencia < 7:
                self.ya_alertado = False
            
            
            
        elif self.momio_pregame_local > self.momio_pregame_visitante:
            
            diferencia = self.marcador_local - self.marcador_visitante
            
            if diferencia >= 7 and diferencia <= 17 and self.momio_actual_visitante > 105 and self.momio_actual_visitante <= 400 and not self.ya_alertado:
                self.ya_alertado = True
                return True
            
            if diferencia < 7:
                self.ya_alertado = False
            
        return False