import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 346) - 802
    _mask = _data(740, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = 'yBoS=Wtkt!+#] L~Q-0Tu-_$P--*dA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
