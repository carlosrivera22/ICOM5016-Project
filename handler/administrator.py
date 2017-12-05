from flask import jsonify
from data.administrator import AdminData

class AdminHandler:

    def getAllAdmins(self):
        admin_data = AdminData()
        return jsonify(admin_data.getAllAdmins())

    def getAdminById(self,aid):
        admin_data = AdminData()
        return jsonify(admin_data.getAdminById(aid))

    def getAdminByUserId(self,uid):
        admin_data = AdminData()
        return jsonify(admin_data.getAdminByUserId(uid))

    def searchAdmins(self, args):
        admin_id = args.get('admin_id')
        user_id = args.get('user_id')

        if len(args) == 1 and admin_id:
            if admin_id:
                return self.getVictimById(int(admin_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        elif len(args) == 1 and user_id:
            if user_id:
                return self.getAdminByUserId(int(user_id))
            else:
                return jsonify(Error="Malformed search string"), 400
        else:
            return jsonify(Error="Malformed search string"), 400
