import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 486) - 563
    _mask = _data(861, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = '.|E)Wz~$E*S C^%@#;WEqye8B7&;=l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
