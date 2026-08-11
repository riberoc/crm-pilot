import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 529) - 220
    _mask = _data(816, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = 'V%.UT{QNdPBh)SDg^}wV(>@b~5>0-_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
