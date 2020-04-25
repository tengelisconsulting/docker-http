import webapps
from webapps import ContainerConf


HANDLER_MAP = {
    b"restart_webapp": lambda webapp_name: webapps.restart_webapp_service(
        ContainerConf(
            image_name = "galleri/webapp",
            container_name = "galleri_webapp",
            vsn = "staging-latest",
            ports =[5000, 6000],
        )
    )
}
