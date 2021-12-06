from typing import List

from . import crud
from .enums import Roles, Permissions
from .schemas import AccountRoleCreate


async def is_have_permission(account_id: int, required_permissions: List[Permissions]) -> bool:
    """Проверка наличия прав."""
    account_role = await crud.account_role.get_by_account(account_id)
    if not account_role:
        return False

    user_permissions = [x.permission.name for x in account_role.role.role_permissions.related_objects]

    return set(required_permissions).issubset(set(user_permissions))


async def create_account_role(account_id: int, role_type: Roles) -> int:
    """Присваивание роли к определенному аккаунту."""
    role = await crud.role.get_by_role(role_type)
    if not role:
        raise ValueError("Role is not found")

    account_role_id = await crud.account_role.create(
        AccountRoleCreate(account_id=account_id, role_id=role.id)
    )

    return account_role_id
