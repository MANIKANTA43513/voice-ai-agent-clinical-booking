import datetime

# in-memory appointment storage
appointments = []

# available doctors
available_doctors = ["cardiologist", "dermatologist", "general"]

# available slots
available_slots = ["10:00", "14:00", "16:00"]


# ---------------------------
# CHECK AVAILABILITY
# ---------------------------

def check_availability(doctor, date):

    if doctor not in available_doctors:
        return {
            "status": "error",
            "message": "Doctor not available",
            "available_doctors": available_doctors
        }

    booked_slots = [
        appt["time"]
        for appt in appointments
        if appt["doctor"] == doctor and appt["date"] == date
    ]

    free_slots = [slot for slot in available_slots if slot not in booked_slots]

    return {
        "action": "availability_check",
        "available_slots": free_slots
    }


# ---------------------------
# BOOK APPOINTMENT
# ---------------------------

def book_appointment(doctor, date, time):

    if doctor not in available_doctors:
        return {
            "status": "error",
            "message": "Doctor not available"
        }

    if time not in available_slots:
        return {
            "status": "error",
            "message": "Invalid time slot"
        }

    # prevent past booking
    today = datetime.date.today().isoformat()
    if date < today:
        return {
            "status": "error",
            "message": "Cannot book appointment in the past"
        }

    # check double booking
    for appt in appointments:
        if appt["doctor"] == doctor and appt["date"] == date and appt["time"] == time:
            return {
                "status": "conflict",
                "message": "Slot already booked",
                "available_slots": check_availability(doctor, date)["available_slots"]
            }

    # add appointment
    appointments.append({
        "doctor": doctor,
        "date": date,
        "time": time
    })

    return {
        "status": "confirmed",
        "doctor": doctor,
        "date": date,
        "time": time
    }


# ---------------------------
# CANCEL APPOINTMENT
# ---------------------------

def cancel_appointment(doctor, date, time):

    global appointments

    for appt in appointments:
        if appt["doctor"] == doctor and appt["date"] == date and appt["time"] == time:
            appointments.remove(appt)

            return {
                "status": "cancelled",
                "doctor": doctor,
                "date": date,
                "time": time
            }

    return {
        "status": "error",
        "message": "Appointment not found"
    }


# ---------------------------
# RESCHEDULE APPOINTMENT
# ---------------------------

def reschedule_appointment(doctor, date, old_time, new_time):

    for appt in appointments:

        if appt["doctor"] == doctor and appt["date"] == date and appt["time"] == old_time:

            # check if new slot already booked
            for a in appointments:
                if a["doctor"] == doctor and a["date"] == date and a["time"] == new_time:
                    return {
                        "status": "conflict",
                        "message": "New slot already booked"
                    }

            appt["time"] = new_time

            return {
                "status": "rescheduled",
                "doctor": doctor,
                "date": date,
                "time": new_time
            }

    return {
        "status": "error",
        "message": "Original appointment not found"
    }
