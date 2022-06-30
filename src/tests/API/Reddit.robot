*** Settings ***
Documentation    Поиск треда/Публикация комментария/Удаление комментария
Resource         ..${/}shared.resource
Force Tags       reddit
Suite Setup      others.Authenticate client

*** Test Cases ***
Testing Reddit API
    ${thread_id}=     Thread search      subreddit=learnpython
    ...                                  token=${user_access_token}

    ${comment_id}=    Publish comment    thread_id=${thread_id}
    ...                                  comment=My first comment
    ...                                  token=${user_access_token}

    Remove comment                       comment_id=${comment_id}
    ...                                  token=${user_access_token}

*** Keywords ***
Thread search
    [Arguments]    ${subreddit}    ${token}

    ${thread_data}=         RedditApi.thread_search      ${subreddit}
    ...                                                  ${token}

    BuiltIn.Should Be True                               ${thread_data}[data][children]
    ...                                                  Треды отсутствуют в субреддите

    ${thread_data_str}=     BuiltIn.Convert To String    ${thread_data}

    @{thread_subreddit}=    String.Get Regexp Matches    ${thread_data_str}
    ...                                                  [\"\']title[\"\']: [\"\']([\\w\\d\\s]*[\\D]*[\\w\\d\\s]*)[\"\'],
    ...                                                  1

    BuiltIn.Should Contain                               ${thread_subreddit}[0]
    ...                                                  ${subreddit}
    ...                                                  Текущая тема не содержит в себе ключ
    ...                                                  ignore_case=True

    @{thread_id}=           String.Get Regexp Matches    ${thread_data_str}
    ...                                                  [\"\']name[\"\']: [\"\'](t3_[\\w\\d]*)[\"\']
    ...                                                  1

    [Return]    ${thread_id}[0]

Publish comment
    [Arguments]    ${thread_id}    ${comment}    ${token}

    ${comment_data}=        RedditApi.publish_comment    ${thread_id}
    ...                                                  ${comment}
    ...                                                  ${token}

    ${comment_data_str}=    BuiltIn.Convert To String    ${comment_data}

    @{comment_body}=        String.Get Regexp Matches    ${comment_data_str}
    ...                                                  [\"\']body[\"\']: [\"\']([\\w\\d\\s]*)[\"\']
    ...                                                  1

    BuiltIn.Should Be Equal                              ${comment_body}[0]
    ...                                                  ${comment}
    ...                                                  Текущий комментарий не равен ожидаемому

    @{comment_id}=          String.Get Regexp Matches    ${comment_data_str}
    ...                                                  [\"\']name[\"\']: [\"\'](t1_[\\w\\d]*)[\"\']
    ...                                                  1

    [Return]    ${comment_id}[0]

Remove comment
    [Arguments]    ${comment_id}    ${token}

    ${method_result}=    RedditApi.remove_comment    ${comment_id}
    ...                                              ${token}

    BuiltIn.Should Not Be True                       ${method_result}
    ...                                              Комментарий не удалился
