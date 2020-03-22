from rolepermissions.roles import AbstractUserRole


class Teacher(AbstractUserRole):
    available_permissions = {
        'create_topic_record': True,
        'edit_topic_record': True,
    }

    @staticmethod
    def get_cls_name():
        return "教师"


class Student(AbstractUserRole):
    available_permissions = {
        # 'edit_patient_file': True,
    }

    @staticmethod
    def get_cls_name():
        return "学生"


class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'create_topic_record': True,
        'edit_topic_record': True,
        'delete_topic_record': True,
    }
