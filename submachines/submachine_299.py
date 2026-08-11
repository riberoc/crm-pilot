import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 727) - 320
    _mask = _data(827, None)
    _enc = 169
    return _mask, _enc

def run():
    matrix = 'YaZXe PLs#`Edi=q^`huA4TJ}L_|Rj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
