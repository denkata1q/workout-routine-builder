# Workout Routine Builder

A Django web application for planning workouts. You build a library of exercises, group them into routines and keep a log of every workout you complete.

Individual project for the SoftUni Django Basics regular exam.

## Features

- **Exercises**: create, view, edit and delete exercises with a difficulty level and one or more muscle groups. Filter by muscle group and sort by name, difficulty or date.
- **Muscle groups**: list and create the muscle groups used to classify exercises.
- **Routines**: combine exercises into a routine with a goal (strength, endurance, fat loss). Full create, view, edit and delete. Filter by goal.
- **Workout log**: record when you performed a routine, for how long, and to add notes about your workout. Sort by date or duration.
- **Validation**: friendly error messages in forms and models (minimum name length, case-insensitive unique names, no future workout dates, duration limits, names that are only digits).
- **Custom template filter**: `duration_display` turns minutes into text such as `1h 15m`.
- **Custom 404 page** and a Bootstrap 5 layout with a shared navigation bar and footer.

Authentication and user management are intentionally not part of this project.

## Technologies

- Python 3.13
- Django 6.1
- SQLite
- Bootstrap 5 (loaded from a CDN, so an internet connection is needed to see the styling)

## Project structure

```
DjangoProject1/      project settings and root URLs
exercises/           Exercise and MuscleGroup models, forms, views, templates
routines/            Routine model, forms, views, templates
workouts/            WorkoutSession model, forms, views, templates, template filter
templates/           base template, home page, 404 page and shared partials
static/css/          project stylesheet
```

### Models and relationships

| Model | App | Main fields | Relationships |
| --- | --- | --- | --- |
| `MuscleGroup` | exercises | name | many-to-many with `Exercise` |
| `Exercise` | exercises | name, description, difficulty, created on | many-to-many with `MuscleGroup` |
| `Routine` | routines | name, goal, description, created on | many-to-many with `Exercise` |
| `WorkoutSession` | workouts | date, duration in minutes, notes | many-to-one with `Routine` |

Deleting a routine also deletes its logged workouts.

## Pages

| URL | Page |
| --- | --- |
| `/` | Home |
| `/exercises/` | Exercise list with filter and sort |
| `/exercises/create/` | Add exercise |
| `/exercises/<id>/` | Exercise details |
| `/exercises/<id>/update/` | Edit exercise |
| `/exercises/<id>/delete/` | Confirm and delete exercise |
| `/exercises/musclegroups/` | Muscle group list |
| `/exercises/musclegroups/create/` | Add muscle group |
| `/routines/` | Routine list with goal filter |
| `/routines/create/` | Add routine |
| `/routines/<id>/` | Routine details with its exercises and workouts |
| `/routines/<id>/update/` | Edit routine |
| `/routines/<id>/delete/` | Confirm and delete routine |
| `/workouts/` | Workout log with sorting |
| `/workouts/create/` | Log a workout |

Every page is reachable from the navigation bar.

## Setup

1. Clone the repository and open the project folder:
   ```
   git clone https://github.com/denkata1q/workout-routine-builder.git
   cd workout-routine-builder
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create the database:
   ```
   python manage.py migrate
   ```
5. Start the server:
   ```
   python manage.py runserver
   ```
6. Open http://127.0.0.1:8000/

The application starts with an empty database. Create data through the interface in this order: muscle groups, exercises, routines, then workouts.

## Configuration

No environment variables or credentials are required. The project runs with its default settings in `DjangoProject1/settings.py` (SQLite database file `db.sqlite3`, `DEBUG = True`). The secret key in the settings file is for development only.

### Viewing the custom 404 page

Django shows its own debug page for missing URLs while `DEBUG = True`. To see the custom 404 page, set `DEBUG = False` and `ALLOWED_HOSTS = ['localhost', '127.0.0.1']` in `DjangoProject1/settings.py`, restart the server and open any address that does not exist, for example `/missing/`. Restore the original values afterwards.
