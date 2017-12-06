class AdminData:
    admins = [
        {
            'admin_id':1,
            'user_id':1
        },
        {
            'admin_id':2,
            'user_id':2
        },
    ]

    def getAllAdmins(self):
        return self.admins

    def getAdminById(self,aid):
        for a in self.admins:
            if a['admin_id'] == aid:
                return a
        return 'No admin found'

    def getAdminByUserId(self,uid):
        for a in self.admins:
            if a['user_id'] == uid:
                return a
        return 'No admin found'
