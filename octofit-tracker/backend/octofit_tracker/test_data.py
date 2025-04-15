# Test data for Octofit app

def get_test_data():
    return {
        "users": [
            {"username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"username": "jane_smith", "email": "jane@example.com", "password": "password123"}
        ],
        "teams": [
            {"name": "Team Alpha", "description": "A competitive team."},
            {"name": "Team Beta", "description": "A fun and casual team."}
        ],
        "activities": [
            {"name": "Running", "calories_burned_per_minute": 10},
            {"name": "Cycling", "calories_burned_per_minute": 8}
        ],
        "leaderboard": [
            {"user": "john_doe", "points": 150},
            {"user": "jane_smith", "points": 200}
        ],
        "workouts": [
            {"name": "Morning Run", "duration_minutes": 30, "activity": "Running"},
            {"name": "Evening Cycle", "duration_minutes": 45, "activity": "Cycling"}
        ]
    }
