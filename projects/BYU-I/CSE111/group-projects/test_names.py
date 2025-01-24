import names as nm
import pytest

def test_make_full_name():
    assert nm.make_full_name('Charles', 'Cantonna') == 'Cantonna; Charles'
    assert nm.make_full_name('Quejo', 'Tonnah') == 'Tonnah; Quejo'
    assert nm.make_full_name('Jacob', 'Schumann') == 'Schumann; Jacob'
    assert nm.make_full_name('Nathan', 'Stokes') == 'Stokes; Nathan'

def test_extract_family_name():
    assert nm.extract_family_name('Cantonna; Charles') == 'Cantonna'
    assert nm.extract_family_name('Tonnah; Quejo') == 'Tonnah'
    assert nm.extract_family_name('Schumann; Jacob') == 'Schumann'
    assert nm.extract_family_name('Stokes; Nathan') == 'Stokes'

def test_extract_given_name():
    assert nm.extract_given_name('Cantonna; Charles') == ' Charles'
    assert nm.extract_given_name('Tonnah; Quejo') == ' Quejo'
    assert nm.extract_given_name('Schumann; Jacob') == ' Jacob'
    assert nm.extract_given_name('Stokes; Nathan') == ' Nathan'

pytest.main(["-v", "--tb=line", "-rN", __file__])