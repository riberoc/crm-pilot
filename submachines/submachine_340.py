import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 684) - 264
    _mask = _data(768, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = ']US#wOaIF(e@$=F5(to@U#f,R> >Ul'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
