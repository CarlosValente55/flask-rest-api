import uuid
import datetime
import os
import json
from .. model.workout_session import Workout


class WorkoutService():
    def __init__(self):
        self.workout_model = Workout()

    # Do stuff here

    def save_new_workout(self, workout, workout_id, user_id):
        workout_session = dict(
            user_id=user_id,
            workout_id=workout_id,
            measures=dict(
                duration=workout["Duration"],
                energy=workout["Energy"],
                distance=workout["Distance"],
                avgMeasures=dict(
                    avg_hr=workout["AvgHR"],
                    avg_cadence=workout["AvgCadence"],
                    avg_speed=workout["AvgSpeed"]
                ),
                maxMeasures=dict(
                    max_speed=workout["MaxSpeed"],
                    max_cadence=workout["MaxCadence"]

                )

            )

        )
        self.workout_model.create_workout(workout_session)

    def get_workout(self, workout_id):
        return self.workout_model.get_workout(workout_id)
