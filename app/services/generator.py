import random


def generate_stars(count: int):
    """
    Generate random coordinates for stars in 3D space.

    :param count: Number of stars to generate.
    :return: List of stars with coordinates.
    """
    stars = []
    for _ in range(count):
        star = {
            "x": random.uniform(-1000, 1000),
            "y": random.uniform(-1000, 1000),
            "z": random.uniform(-1000, 1000),
        }
        stars.append(star)
    return stars
