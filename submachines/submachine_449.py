import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 953) - 881
    _mask = _data(105, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = 'L_ODV+l$!7wN&3cfWP;u8jG NH$Lj:'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
