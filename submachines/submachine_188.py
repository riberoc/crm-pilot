import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 689) - 799
    _mask = _data(369, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = 'iGo|O1^5.1fq<.hm@tZ7u3U>SeP7VO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
