import allure


@allure.step("Building API client")
def build_api_client():
    with allure.step("Get user auth token"): # для вложенных шагов
        ...

    with allure.step("Create new API client"): # для вложенных шагов
        ...

@allure.step("Create course with title {title}") # использование шаблонизатора в названии шага
def create_course(title: str):
    ...

@allure.step("Deleting course")
def delete_course():
    ...

def test_feature():
    # если без декораторов:
    # with allure.step("Building API client"):
    #     ...
    #
    # with allure.step("Create course"):
    #     ...
    #
    # with allure.step("Deleting course"):
    #     assert False


    # если с декораторами:
    build_api_client()
    create_course(title="4444")
    create_course(title="fsdfsd")
    create_course(title="!!!!!!!!!!!")
    delete_course()

