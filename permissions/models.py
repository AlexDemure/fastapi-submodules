from tortoise import models, fields

from backend.submodules.permissions.enums import Permissions, Roles


class Role(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharEnumField(Roles, max_length=128)
    description = fields.CharField(max_length=128)


class Permission(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharEnumField(Permissions, max_length=128)
    description = fields.CharField(max_length=128)


class RolePermission(models.Model):
    id = fields.IntField(pk=True)
    role = fields.ForeignKeyField('models.Role', related_name="role_permissions", on_delete=fields.CASCADE)
    permission = fields.ForeignKeyField('models.Permission', related_name="role_permissions", on_delete=fields.CASCADE)


class AccountPermission(models.Model):
    id = fields.IntField(pk=True)
    account = fields.ForeignKeyField('models.Account', related_name='account_permissions', on_delete=fields.CASCADE)
    permission = fields.ForeignKeyField('models.Permission', related_name="account_permissions", on_delete=fields.CASCADE)


class AccountRole(models.Model):
    id = fields.IntField(pk=True)
    account = fields.OneToOneField('models.Account', related_name='account_role', on_delete=fields.CASCADE)
    role = fields.ForeignKeyField('models.Role', related_name='account_role', on_delete=fields.CASCADE)
