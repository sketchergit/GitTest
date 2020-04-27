import ping

def test_ping():
    assert ping.ping('www.google.com') == 'UP'
