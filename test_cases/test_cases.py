import requests

url = "https://www.lhv.ee/et/liising/taotlus"


def test_get_successful_response():
    resp = requests.get(url)
    assert resp.status_code == 200


def test_lease_is_present():
    resp = requests.get(url)
    assert "Liisingutaotlus" in resp.text
