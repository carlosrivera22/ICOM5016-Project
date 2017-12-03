from flask import jsonify
from data.user import UserData

class UserHandler:

    def getAllUsers(self):
        user_data = UserData()
        return jsonify(user_data.getAllUsers())

    def searchUsers(self, args):
        user_id = args.get('user_id')
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        email = args.get('email')
        phone = args.get('phone')
        password = args.get('password')

        if len(args) == 1 and user_id:
            if user_id:
                data = UserData()
                user = data.getUserById(user_id)
                return jsonify(user)
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400

        
