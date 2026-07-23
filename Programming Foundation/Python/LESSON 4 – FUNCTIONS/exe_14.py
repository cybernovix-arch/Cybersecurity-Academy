def system_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
system_info(
    OS="Linux",
    version="Ubuntu 24.04",
    kernel="6.8",
    architecture="x64" 
)