import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.units as u

def exosky(data, planet):
    data['dist'] = 1000 / data['parallax']
    data['abs_mag'] = data['mag'] - 5 * np.log10(data['dist'] / 10.)
    
    a = SkyCoord(data['ra'], data['dec'], data['dist'], unit=(u.deg, u.deg, u.pc))
    b = SkyCoord(planet['ra'], planet['dec'], planet['sy_dist'], unit=(u.deg, u.deg, u.pc))
    
    stars_from_planet = pd.DataFrame()
    stars_from_planet['abs_mag'] = data['abs_mag'].copy()
    stars_from_planet['x'] = (a.cartesian.x - b.cartesian.x).value
    stars_from_planet['y'] = (a.cartesian.y - b.cartesian.y).value
    stars_from_planet['z'] = (a.cartesian.z - b.cartesian.z).value
    stars_from_planet['distance'] = np.sqrt(stars_from_planet['x']**2 + stars_from_planet['y']**2 + stars_from_planet['z']**2)
    stars_from_planet['Vmag'] = stars_from_planet['abs_mag'] + 5 * np.log10(stars_from_planet['distance'] / 10)
    stars_from_planet['name'] = data['identifier'].copy()
    
    filtered_stars = stars_from_planet.drop(stars_from_planet[stars_from_planet.Vmag > 6].index)
    new_coords = SkyCoord(filtered_stars['x'], filtered_stars['y'], filtered_stars['z'], unit=u.pc, representation_type='cartesian')
    new_coords.representation_type = 'spherical'
    
    filtered_stars['RA'] = new_coords.ra.to(u.deg).value
    filtered_stars['DEC'] = new_coords.dec.to(u.deg).value
    
    return filtered_stars

