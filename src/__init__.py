# Importar funciones principales para facilitar su acceso
from .q1_time import q1_time
from .q1_memory import q1_memory
from .q2_time import q2_time
from .q2_memory import q2_memory
from .q3_time import q3_time
from .q3_memory import q3_memory

# Definir __all__ para controlar las importaciones
__all__ = ['q1_time', 'q1_memory', 'q2_time', 'q2_memory', 'q3_time', 'q3_memory']