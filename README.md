# Phase 4 Code Challenge: Late Show API

This repository contains the implementation of a Flask API for managing episodes and guest appearances on a late-night show. The API allows for the retrieval of episodes and guests, as well as the creation of guest appearances linked to episodes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Validations](#validations)
- [Setup](#setup)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Challenge-Late-Show.git
   cd Challenge-Late-Show
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set the environment variables:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

2. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

3. Seed the database if necessary using the provided CSV file.

4. Run the application:
   ```bash
   flask run
   ```

## API Endpoints

### GET /episodes
Returns a list of all episodes.

**Response:**
```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
```

### GET /episodes/:id
Returns details of a specific episode along with its appearances.

**Response on Success:**
```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}
```

**Response on Failure (Episode not found):**
```json
{
  "error": "Episode not found"
}
```

### GET /guests
Returns a list of all guests.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "comedian"
  }
]
```

### POST /appearances
Creates a new appearance for a guest in an episode.

**Request Body:**
```json
{
  "rating": 5,
  "episode_id": 100,
  "guest_id": 123
}
```

**Response on Success:**
```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 3,
  "episode_id": 2,
  "episode": {
    "date": "1/12/99",
    "id": 2,
    "number": 2
  },
  "guest": {
    "id": 3,
    "name": "Tracey Ullman",
    "occupation": "television actress"
  }
}
```

**Response on Failure:**
```json
{
 "errors": ["validation errors"]
}
```

## Models

- **Episode**: Represents an episode of the show.
- **Guest**: Represents a guest who appears on the show.
- **Appearance**: Represents the appearance of a guest in an episode, including a rating.

### Relationships
- An `Episode` has many `Guest`s through `Appearance`.
- A `Guest` has many `Episode`s through `Appearance`.
- An `Appearance` belongs to both a `Guest` and an `Episode`.

## Validations

- The `Appearance` model requires a rating between 1 and 5 (inclusive).

## Setup

To set up the database and run the application, ensure that you have Flask and Flask-SQLAlchemy installed. Follow the steps in the [Usage](#usage) section for detailed instructions on initializing and running the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
