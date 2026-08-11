import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 975) - 951
    _mask = _data(2007, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'WJB j#7|M7I)~1]$zvmu;N=^VzqQ,N'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
