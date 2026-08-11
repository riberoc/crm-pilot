import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 233) - 385
    _mask = _data(288, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = '7{9a<4+wE/i]2riht^L.HP&OhqiDNu'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
