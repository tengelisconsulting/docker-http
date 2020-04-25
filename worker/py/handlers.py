import webapps




HANDLER_MAP = {
    b"restart_webapp": lambda webapp_name: webapps.restart_webapp_service(
        "galleri/webapp",
        "galleri_webapp_test",
        "staging-latest",
        [5000, 6000]
    )
}
