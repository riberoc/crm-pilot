import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 209) - 407
    _mask = _data(662, None)
    _enc = 169
    return _mask, _enc

def run():
    matrix = 'eH@7<qxL=L}{58zG^5G<-2%[m y!@]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
