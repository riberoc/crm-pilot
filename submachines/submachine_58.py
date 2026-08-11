import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 302) - 348
    _mask = _data(803, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'Ut>;tIt^.u@uR^EdeXm% T-c6#lTHG'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
