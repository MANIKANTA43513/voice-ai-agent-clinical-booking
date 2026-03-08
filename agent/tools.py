import json
from scheduler.appointment_engine import (
    check_availability,
    book_appointment,
    cancel_appointment
)

def execute_tool(agent_json):

    try:
        data = json.loads(agent_json)
    except:
        return {"error": "invalid agent json"}

    intent = data.get("intent")

    # Check doctor availability
    if intent == "book":

        doctor = data.get("doctor")
        date = data.get("date")

        slots = check_availability(doctor, date)

        return {
            "action": "availability_check",
            "available_slots": slots
        }

    # Confirm appointment booking
    if intent == "confirm":

        doctor = data.get("doctor")
        date = data.get("date")
        time = data.get("time")

        return book_appointment(
            "patient1",
            doctor,
            date,
            time
        )

    # Cancel appointment
    if intent == "cancel":

        return cancel_appointment("patient1")

    return {"message": "no action executed"}