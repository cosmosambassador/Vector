"""30 x 30 vortex sampling and an explicitly prescribed gravity baseline.

This checks circulation geometry. It contains no gravity-modification force law.
"""
import hashlib
import json
import math
from pathlib import Path


def velocity(x, y, circulation, core_radius):
    """Planar ideal-vortex velocity in SI, outside a positive finite core."""
    values = (x, y, circulation, core_radius)
    if not all(math.isfinite(v) for v in values) or core_radius <= 0:
        raise ValueError('Finite inputs and a positive core radius are required')
    radius = math.hypot(x, y)
    if radius < core_radius:
        raise ValueError('Point lies inside the excluded vortex core')
    factor = circulation/(2*math.pi*radius)/radius
    return -factor*y, factor*x


def _contour_integral(radius, circulation, core_radius, segments):
    # Midpoint quadrature over a closed polygon approximating a circle.
    # Increase segments to check convergence without inserting Gamma as a result.
    result = 0.
    for i in range(segments):
        theta1 = 2*math.pi*i/segments
        theta2 = 2*math.pi*(i+1)/segments
        x1, y1 = radius*math.cos(theta1), radius*math.sin(theta1)
        x2, y2 = radius*math.cos(theta2), radius*math.sin(theta2)
        vx, vy = velocity((x1+x2)/2, (y1+y2)/2,
                          circulation, core_radius)
        result += vx*(x2-x1)+vy*(y2-y1)
    return result


def run_check():
    circumference = 30*.3048
    outer_radius = circumference/(2*math.pi)
    # Illustrative parameters, unrelated to measured helium/Xe properties.
    core_radius = outer_radius/100
    circulation = 1.  # m^2/s, chosen numerical test value
    gravity = 9.80665  # prescribed conventional reference, not a site measurement
    rows = []
    max_reversal_error = max_speed_error = 0.
    for i in range(30):
        # Keep contours well outside the excluded core, including polygon chords.
        radius = 2*core_radius+(outer_radius-2*core_radius)*i/29
        for j in range(30):
            angle = 2*math.pi*j/30
            x, y = radius*math.cos(angle), radius*math.sin(angle)
            forward = velocity(x, y, circulation, core_radius)
            reverse = velocity(x, y, -circulation, core_radius)
            max_reversal_error = max(max_reversal_error,
                                     math.hypot(forward[0]+reverse[0],
                                                forward[1]+reverse[1]))
            max_speed_error = max(max_speed_error,
                                  abs(math.hypot(*forward)-math.hypot(*reverse)))
            rows.append(dict(radius_m=radius, angle_rad=angle,
                             forward_velocity_m_per_s=forward,
                             reversed_velocity_m_per_s=reverse))
    contours = []
    for radius in (2*core_radius, outer_radius/2, outer_radius):
        for signed_circulation in (-circulation, circulation):
            errors = [abs(_contour_integral(radius, signed_circulation,
                                           core_radius, n)-signed_circulation)
                      for n in (256, 512)]
            contours.append(dict(radius_m=radius,
                                 circulation_m2_per_s=signed_circulation,
                                 errors_m2_per_s=errors,
                                 passed=errors[1] < errors[0] and errors[1] < 2e-5))
    passed = (max_reversal_error < 1e-12 and max_speed_error < 1e-12
              and all(c['passed'] for c in contours))
    return dict(schema_version=1, grid=[30, 30], sample_count=len(rows),
                grid_meaning='30 radii x 30 azimuths; not a 30 ft x 30 ft enclosure',
                circumference_m=circumference, outer_radius_m=outer_radius,
                core_radius_m=core_radius,
                illustrative_circulation_m2_per_s=circulation,
                maximum_reversal_error_m_per_s=max_reversal_error,
                maximum_speed_change_m_per_s=max_speed_error,
                contour_segments=[256, 512], contour_checks=contours,
                numerical_checks_passed=passed,
                prescribed_gravity_baseline=dict(
                    upward_axis='z', acceleration_m_per_s2=-gravity,
                    applicable_to='positive inertial and gravitational mass, equal ratio',
                    force_per_mass_n_per_kg=-gravity,
                    assumption='no fluid, electromagnetic or anomalous force on test body'),
                antigravity_assessment=dict(
                    status='not testable with this model',
                    reason='no gravity-modifying coupling or force law supplied',
                    physical_measurements=0,
                    interpretation='numerical pass verifies vortex behavior only; '
                                   'it neither proves nor experimentally rules out antigravity'),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                requested_conditions=dict(
                    material='hot ice: identity and phase unresolved',
                    magnetic_field_tesla=[0., 0., 0.],
                    magnetic_field_scope='uniform, time-independent zero-field control',
                    requested_temperature_k=0.,
                    temperature_status='idealized target only; no thermal model',
                    status='B=0 and requested T=0 K recorded; material physics not modeled'))


def main():
    report = run_check()
    print(json.dumps(report, indent=2, allow_nan=False))
    raise SystemExit(0 if report['numerical_checks_passed'] else 1)


if __name__ == '__main__':
    main()
