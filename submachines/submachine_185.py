import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 301) - 560
    _mask = _data(987, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 'E>Eg/).}M*r4/=Sr<wofm=ScY{IPp%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
