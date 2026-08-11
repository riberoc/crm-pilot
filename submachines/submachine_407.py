import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 127) - 882
    _mask = _data(1012, None)
    _enc = 21
    return _mask, _enc

def run():
    matrix = 'HK$,RL}NyC[@wTgP~mkr;LgAp)O3Nj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
