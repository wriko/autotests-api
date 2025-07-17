from enum import Enum

class AllureStory(str, Enum):
    LOGIN = "Login"

    GET_ENTITY = "Get Entity"
    GET_ENTITIES = "Get Entities"
    CREATE_ENTITY = "Create Entity"
    UPDATE_ENTITY = "Update Entity"
    DELETE_ENTITY = "Delete Entity"
    VALIDATE_ENTITY = "Validate Entity"