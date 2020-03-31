import ping

def test_ping():
    assert ping.ping('127.0.0.1') == 'UP'
