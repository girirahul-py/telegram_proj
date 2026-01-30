#services/permission.py

"""Permission service module."""

def can_push(permissions: dict) -> bool:
    return permissions.get("push", False)

def can_admin(permissions: dict) -> bool:
    return permissions.get("admin", False)

def can_pull(permissions: dict) -> bool:
    return permissions.get("pull", False)
