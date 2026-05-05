# pyAsteroids

A classic **Asteroids** arcade game clone built with Python and pygame.

Navigate your spaceship through an endless field of asteroids, shoot them down, and survive as long as you can. Large asteroids split into smaller ones when hit — stay sharp!

---

## Features

- Classic Asteroids gameplay loop
- Asteroids that split into smaller fragments when destroyed
- Smooth player movement and rotation
- Projectile shooting mechanics
- Randomized asteroid field generation
- Built-in logging via a dedicated logger module

---

## Requirements

- Python **3.13** or higher
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

---

## Installation

### Using uv (recommended)

```bash
git clone https://github.com/FPovolato/pyAsteroids.git
cd pyAsteroids
uv sync
```

### Using pip

```bash
git clone https://github.com/FPovolato/pyAsteroids.git
cd pyAsteroids
pip install pygame==2.6.1
```

---

## Running the Game

### With uv

```bash
uv run python main.py
```

### With pip / standard Python

```bash
python main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| `W` / `↑` | Thrust forward |
| `A` / `←` | Rotate left |
| `D` / `→` | Rotate right |
| `Space` | Shoot |

---

## Project Structure

```
pyAsteroids/
├── main.py            # Entry point — game loop and initialization
├── player.py          # Player spaceship logic (movement, shooting)
├── asteroid.py        # Asteroid entity (movement, splitting on hit)
├── asteroidfield.py   # Asteroid field spawner and manager
├── shot.py            # Projectile logic
├── circleshape.py     # Base class for circular game objects (collision detection)
├── constants.py       # Game-wide constants (screen size, speeds, radii…)
├── logger.py          # Logging utility
├── pyproject.toml     # Project metadata and dependencies
└── uv.lock            # Locked dependency tree
```

---

## Dependencies

| Package | Version |
|---------|---------|
| [pygame](https://www.pygame.org/) | 2.6.1 |

---

## License

This project does not currently specify a license. All rights reserved by the author unless otherwise stated.

---

## Author

**FPovolato** — [github.com/FPovolato](https://github.com/FPovolato)
