import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 982) - 360
    _mask = _data(464, None)
    _enc = 157
    return _mask, _enc

def run():
    matrix = 'Kl$ l{|/O%dnMVAChJnm/4ip0X9j2P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
