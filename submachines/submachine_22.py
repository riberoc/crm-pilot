import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 833) - 444
    _mask = _data(296, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = '9>&Ou}f2 y=Js3#<L.=3O>jt!(SZga'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
