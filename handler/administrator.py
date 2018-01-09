from flask import jsonify
from dao.administrator import AdminData

class AdminHandler:
    def build_admin_dict(self,row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        result['password'] = row[5]
        return result

    #funciona
    def getAllAdmins(self):
        data = AdminData()
        admin_list = data.getAllAdministrators()
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    #funciona
    def getUserByAdminId(self,admin_id):
        data = AdminData()
        if not data.getAdministratorById(admin_id):
            return jsonify(Error="Administrator Not Found"),404
        row = data.getUserByAdministratorId(admin_id)
        admin = self.build_admin_dict(row)
        return jsonify(Administrator=admin)

