import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 716) - 625
    _mask = _data(485, None)
    _enc = 174
    return _mask, _enc

def run():
    matrix = '=<o)M.$/>S@KG@Jd]Q,qCa n7N:OJ<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
