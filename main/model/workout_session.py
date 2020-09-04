from main.common.db import db
class Workout():
    
    def __init__(self):
        self.workout_collection=db["workouts"]

    def get_workout(self,workout_id):
        return list(self.workout_collection.find({"workout_id":workout_id}))

    def create_workout(self,session):
        self.workout_collection.insert_one(session)



    
