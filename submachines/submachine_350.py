import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 203) - 512
    _mask = _data(532, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = 'Kbn[R`v-@S{sTynINEiCc{V#?nr|d~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
