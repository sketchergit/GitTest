import ping

def test_ping():
    assert ping.ping('www.yahoo.com') == 'UP'
