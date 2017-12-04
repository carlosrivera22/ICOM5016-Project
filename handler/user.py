from flask import jsonify
from data.user import UserData

class UserHandler:

    def getAllUsers(self):
        user_data = UserData()
        return jsonify(user_data.getAllUsers())

    def getUserById(self,uid):
        user_data = UserData()
        return jsonify(user_data.getUserById(uid))

    def getUserByFirstName(self,fname):
        user_data = UserData()
        return jsonify(user_data.getUserByFirstName(fname))

    def getUserByLastName(self,lname):
        user_data = UserData()
        return jsonify(user_data.getUserByLastName(lname))

    def getUserByFirstNameAndLastName(self,fname,lname):
        user_daa = UserData()
        return jsonify(user_data.getUserByFirstNameAndLastName(fname,lname))

    def getUserByEmail(self,email):
        user_data = UserData()
        return jsonify(user_data.getUserByEmail(email))

    def getUserByPhone(self,phone):
        user_data = UserData()
        return jsonify(user_data.getUserByPhone(phone))

    def searchUsers(self, args):
        user_id = args.get('user_id')
        first_name = args.get('first_name')
        last_name = args.get('last_name')
        email = args.get('email')
        phone = args.get('phone')
        password = args.get('password')

        if len(args) == 1 and user_id:
            if user_id:
                return self.getUserById(int(user_id))
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and first_name:
            if first_name:
                return self.getUserByFirstName(first_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and last_name:
            if last_name:
                return self.getUserByLastName(last_name)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 2 and first_name and last_name:
                return self.getUserByFirstNameAndLastName(first_name,last_name)
        elif len(args) == 1 and email:
            if email:
                return self.getUserByEmail(email)
            else:
                return jsonify(Error="Malformed search string."), 400
        elif len(args) == 1 and phone:
            if phone:
                return self.getUserByPhone(phone)
            else:
                return jsonify(Error="Malformed search string."), 400
        else:
            return jsonify(Error="Malformed search string"), 400
