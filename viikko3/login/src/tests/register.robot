*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  petri
    Set Password  petri1985
    Set Password Confirmation  petri1985
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  1
    Set Password  petri1985
    Set Password Confirmation  petri1985
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  petri
    Set Password  a1
    Set Password Confirmation  a1
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  petri
    Set Password  makkararakastaja
    Set Password Confirmation  makkararakastaja
    Click Button  Register
    Register Should Fail With Message  Password can't contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  petri
    Set Password  petri1985
    Set Password Confirmation  petri1986
    Click Button  Register
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  petri1985
    Set Password Confirmation  petri1985
    Click Button  Register
    Register Should Fail With Message  Username already taken


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page