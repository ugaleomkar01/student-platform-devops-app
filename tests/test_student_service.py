from services.student_service import (
    get_all_courses,
    get_all_students,
    get_student_by_id,
)


def test_get_all_students_returns_sample_students():
    students = get_all_students()

    assert len(students) >= 3
    assert students[0]["id"] == 1
    assert "AIML" in students[0]["course"]


def test_get_student_by_valid_id():
    student = get_student_by_id(1)

    assert student is not None
    assert student["name"] == "Ananya Rao"
    assert student["email"] == "ananya.rao@example.edu"


def test_get_non_existing_student_returns_none():
    student = get_student_by_id(999)

    assert student is None


def test_get_all_courses_returns_sample_courses():
    courses = get_all_courses()

    assert len(courses) >= 3
    assert courses[0]["name"] == "B.Tech AIML"


def test_missing_route_returns_json_when_requested():
    from app import app

    client = app.test_client()

    response = client.get("/missing", headers={"Accept": "application/json"})

    assert response.status_code == 404
    assert response.is_json
    assert response.get_json()["error"] == "The requested academic record could not be found."


def test_json_format_parameter_is_case_insensitive():
    from app import app

    client = app.test_client()

    response = client.get("/students?format=JSON")

    assert response.status_code == 200
    assert response.is_json
