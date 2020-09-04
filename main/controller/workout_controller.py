from flask import request,Blueprint 
from main.service.workout_service import WorkoutService

workoutservice=WorkoutService()

workout = Blueprint('workout', __name__,url_prefix='/workout')
@workout.route('/<workout_id>/users/<user_id>', methods=['GET','POST'])
def workout_resource(workout_id,user_id):
    if request.method == 'GET':
        return {'key':'value'}
    if request.method == 'POST':
        workout=request.json
        workoutservice.save_new_workout(workout,workout_id,user_id)
        #executar um pedido para
        return {'status':201}
@workout.route('/<workout_id>', methods=['GET'])
def workout_s(workout_id):
    if request.method == 'GET':
        print(workout_id)
        w=workoutservice.get_workout(workout_id)
        return {'status':200,'data':w}

notification = Blueprint('notification', __name__,url_prefix='/notification')
@notification.route('/',methods=['POST'])
def notification_resource():
    if request.method == 'POST':
        notification=request.json
        print('Notification ',notification)
        return {'status':200}

        
