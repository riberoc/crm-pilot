import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 789) - 683
    _mask = _data(49, None)
    _enc = 118
    return _mask, _enc

def run():
    matrix = 'Yfu_poPnWu8mM7*O|Vpikg%Y,AEi[g'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
