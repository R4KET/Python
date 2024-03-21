from admin_class_2 import Admin

privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin("Adam", "Lopez", "SuperAdmin", "11-11-1985", privileges)
admin.describe_user()
admin.privileges.show_privileges()