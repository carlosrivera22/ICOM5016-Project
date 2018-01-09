from flask import jsonify
from dao.user import UserDAO


class UserHandler:

    def build_user_dict(self,row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['password'] = row[5]
        result['confirm_password'] = row[6]
        return result

    def build_user_attributes(self, user_id, first_name, last_name, email, phone, password, confirm_password):
        result = {}
        result['user_id'] = user_id
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['email'] = email
        result['phone'] = phone
        result['password'] = password
        result['confirm_password'] = confirm_password
        return result

    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, user_id):
        dao = UserDAO
        row = dao.getUserByUserId(user_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def searchUsers(self, args):
        first_name = args.get("first_name")
        last_name = args.get("last_name")
        email = args.get("email")
        phone = args.get("phone")
        dao = UserDAO()
        users_list = []

        if(len(args) == 1) and first_name:
            users_list = dao.getUserByFirstName(first_name)
        elif(len(args) == 1) and last_name:
            users_list = dao.getUserByLastName(last_name)
        elif(len(args) == 1) and email:
            users_list = dao.getUserByEmail(email)
        elif(len(args) == 1) and phone:
            users_list = dao.getUserByPhone(phone)
        elif(len(args) == 2) and first_name and last_name:
            users_list =  dao.getUserByFirstNameAndLastName(first_name, last_name)
        elif(len(args) == 2) and email and phone:
            users_list = dao.getUserByEmailAndPhone(email, phone)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=users_list)