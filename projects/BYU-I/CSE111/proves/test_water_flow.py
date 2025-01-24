import water_flow as wf
from pytest import approx
import pytest

def test_water_column_height():
    assert wf.water_column_height(0.0, 0.0) == approx(0.0)
    assert wf.water_column_height(0.0, 10.0) == approx(7.5)
    assert wf.water_column_height(25.0, 0.0) == approx(25.0)
    assert wf.water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert wf.pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert wf.pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert wf.pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert wf.pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert wf.pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    assert wf.pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert wf.pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert wf.pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert wf.reynolds_number(0.048692, 0.00) == approx(0.00, abs=1)
    assert wf.reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert wf.reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert wf.reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert wf.reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert wf.pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert wf.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert wf.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

def test_vert_kpa_psi():
    assert wf.vert_kpa_psi(0.00) == approx(0.00, abs=0.001)
    assert wf.vert_kpa_psi(12.18) == approx(1.766, abs=0.001)
    assert wf.vert_kpa_psi(22.00) == approx(3.191, abs=0.001)
    assert wf.vert_kpa_psi(9.05) == approx(1.313, abs=0.001)
    assert wf.vert_kpa_psi(152.258) == approx(22.083, abs=0.001)
    assert wf.vert_kpa_psi(69.52) == approx(10.083, abs=0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])