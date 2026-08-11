import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 684) - 606
    _mask = _data(405, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = 'D35yv ~v(f?G:<zz(|T$::1Mj3EspB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
