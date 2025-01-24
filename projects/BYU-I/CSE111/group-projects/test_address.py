import address as ad
import pytest

def test_extract_city():
    assert ad.extract_city('123 S Highway 12, Detroit, Michigan 12345') == 'Detroit'
    assert ad.extract_city('123 S Highway 12, Las Vegas, Nevada 12345') == 'Las Vegas'
    assert ad.extract_city('123 S Highway 12, Hobbiton, Idaho 12345') == 'Hobbiton'

def test_extract_state():
    assert ad.extract_state('123 S Highway 12, Detroit, Michigan 12345') == 'Michigan'
    assert ad.extract_state('123 S Highway 12, Las Vegas, Nevada 12345') == 'Nevada'
    assert ad.extract_state('123 S Highway 12, Hobbiton, Idaho 12345') == 'Idaho'

def test_extract_zipcode():
    assert ad.extract_zipcode('123 S Highway 12, Detroit, Michigan 12345') == '12345'
    assert ad.extract_zipcode('123 S Highway 12, Las Vegas, Nevada 68759') == '68759'
    assert ad.extract_zipcode('123 S Highway 12, Hobbiton, Idaho 54321') == '54321'

pytest.main(["-v", "--tb=line", "-rN", __file__])