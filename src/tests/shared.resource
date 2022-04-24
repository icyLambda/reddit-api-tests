*** Settings ***
Documentation    Подключение общих для всех тестов ресурсов
Library          library.AuthApi      WITH NAME    AuthApi
Library          library.RedditApi    WITH NAME    RedditApi
Library          String

Resource         common/others.resource

Variables        variables.data
