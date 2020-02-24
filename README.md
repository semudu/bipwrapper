# bipwrapper
BIP Messenger API Wrapper

    pip install bipwrapper


usage:

    from bipwrapper import BipWrapper
    
    ...
    
    wrapper_test = BipWrapper("TEST","username", "password") # for test 
    wrapper_prod = BipWrapper("PROD","username", "password") # for prod
    
    ...
    
    wrapper_test.single.send_text_message("532xxxxxxx")
    
    ...


