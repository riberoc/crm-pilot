import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 696) - 541
    _mask = _data(125, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'd98^8D$j/go!@`ej=s C-b6^u(KG&$'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
