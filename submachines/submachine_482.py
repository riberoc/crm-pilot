import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 922) - 335
    _mask = _data(740, None)
    _enc = 51
    return _mask, _enc

def run():
    matrix = 'N[z}>j6$fu-f_^;E>G)DJW$/;&+mm$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
