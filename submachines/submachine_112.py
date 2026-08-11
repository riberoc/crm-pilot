import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 724) - 892
    _mask = _data(362, None)
    _enc = 65
    return _mask, _enc

def run():
    matrix = 'ltgktS#0nPK3p$V&54R6-COGu%?Am!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
