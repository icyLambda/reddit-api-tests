*** Settings ***
Resource    tests/shared.resource

*** Keywords ***
Authenticate Client
    [Arguments]    ${script_id}=${SCRIPT_ID}    ${secret_key}=${SECRET_KEY}
    ...            ${user_name}=${USER_NAME}    ${password}=${PASSWORD}
    ...            ${user_agent}=${USER_AGENT}

    ${data_token}=    AuthApi.login_by_password    script_id=${script_id}
    ...                                            secret_key=${secret_key}
    ...                                            user_name=${user_name}
    ...                                            password=${password}
    ...                                            user_agent=${user_agent}

    BuiltIn.Should Not Be Equal                    ${data_token}[access_token]
    ...                                            ${EMPTY}
    ...                                            Токен не сгенерировался

    BuiltIn.Set Suite Variable                     ${user_access_token}    ${data_token}[access_token]
