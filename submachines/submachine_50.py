import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 510) - 644
    _mask = _data(788, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = 'Oi7WIM~}taY+C$;yJ+ie}x+)]XT{Wd'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
