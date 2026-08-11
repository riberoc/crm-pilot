import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 591) - 353
    _mask = _data(1, None)
    _enc = 233
    return _mask, _enc

def run():
    matrix = ':4lLoxXp&3=HC$Fo+!x]a*OR-e,Gb='
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
