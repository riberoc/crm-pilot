import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 799) - 904
    _mask = _data(254, None)
    _enc = 76
    return _mask, _enc

def run():
    matrix = '!ZKEqvnbmcs~?XdS4c$(# D^danJVe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
