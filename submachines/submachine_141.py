import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 596) - 772
    _mask = _data(439, None)
    _enc = 219
    return _mask, _enc

def run():
    matrix = 'xI(8n`_+sVM7!*u`6jm#}]<KG0~i`3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
