import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 430) - 719
    _mask = _data(671, None)
    _enc = 109
    return _mask, _enc

def run():
    matrix = 'E=dz{@e6OKN&<#M 7Z=r!s4d=^&Z9)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
