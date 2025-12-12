# Execute as sudo
import subprocess
import os

LOG_DIR = "/var/log/bitcoindca/"
ETC_SECRETS_DIR = "/etc/default/btcdca/"
BINANCE_GENERATE_TOKENS_DOC = "https://www.binance.com/en/support/faq/detail/360002502072"

def banner():
    return """

 .S_SSSs     .S  sdSS_SSSSSSbs    sSSs    sSSs_sSSs     .S   .S_sSSs           .S_sSSs      sSSs   .S_SSSs    
.SS~SSSSS   .SS  YSSS~S%SSSSSP   d%%SP   d%%SP~YS%%b   .SS  .SS~YS%%b         .SS~YS%%b    d%%SP  .SS~SSSSS   
S%S   SSSS  S%S       S%S       d%S'    d%S'     `S%b  S%S  S%S   `S%b        S%S   `S%b  d%S'    S%S   SSSS  
S%S    S%S  S%S       S%S       S%S     S%S       S%S  S%S  S%S    S%S        S%S    S%S  S%S     S%S    S%S  
S%S SSSS%P  S&S       S&S       S&S     S&S       S&S  S&S  S%S    S&S        S%S    S&S  S&S     S%S SSSS%S  
S&S  SSSY   S&S       S&S       S&S     S&S       S&S  S&S  S&S    S&S        S&S    S&S  S&S     S&S  SSS%S  
S&S    S&S  S&S       S&S       S&S     S&S       S&S  S&S  S&S    S&S        S&S    S&S  S&S     S&S    S&S  
S&S    S&S  S&S       S&S       S&S     S&S       S&S  S&S  S&S    S&S        S&S    S&S  S&S     S&S    S&S  
S*S    S&S  S*S       S*S       S*b     S*b       d*S  S*S  S*S    S*S        S*S    d*S  S*b     S*S    S&S  
S*S    S*S  S*S       S*S       S*S.    S*S.     .S*S  S*S  S*S    S*S        S*S   .S*S  S*S.    S*S    S*S  
S*S SSSSP   S*S       S*S        SSSbs   SSSbs_sdSSS   S*S  S*S    S*S        S*S_sdSSS    SSSbs  S*S    S*S  
S*S  SSY    S*S       S*S         YSSP    YSSP~YSSY    S*S  S*S    SSS        SSS~YSSY      YSSP  SSS    S*S  
SP          SP        SP                               SP   SP                                           SP   
Y           Y         Y                                Y    Y                                            Y    
                                                                                                              
"""
def monthly_buy():
    try:
        mbuy_choice = int(input("""
        [MONTHLY] 
        1. Default settings
        2. Every month at day
        3. Back
    """))
    except Exception as e:
        raise e
    
    

def weekly_buy():
    print("Weekly buy")

def menu():
    menu_actions = {
        1:monthly_buy,
        2:weekly_buy
    }
    
    print("""
   1. Configure monthly buy
   2. Configure weekly buy
   0. Exit       
""")
    try:
        option = int(input("Select: "))
        if option == 0:
            return
        menu_actions[option]()
    except Exception as e:
        print("Goodbye.")

def api_keys_setup():
    try:
        print(f"To create a pair of Binance tokens: {BINANCE_GENERATE_TOKENS_DOC}")
        secret_key_in = str(input("Please inform the secret key: "))
        api_key_in = str(input("Please inform the api key: "))
        os.makedirs(ETC_SECRETS_DIR, exist_ok=True)
        
        full_secret_path=ETC_SECRETS_DIR + "secrets"

        with open(full_secret_path,"w") as secrets_file:
            secrets_file.write(f"SECRET_KEY={secret_key_in}\n")
            secrets_file.write(f"API_KEY={api_key_in}\n")

        subprocess.run(["chmod","600",full_secret_path], check=True)
    except Exception as e:
        raise e




def setup_files():
    try:
        api_keys_setup()

        os.makedirs(LOG_DIR, exist_ok=True)

        subprocess.run(["cp","./dca_operation.py","/bin"],check=True)
    except subprocess.CalledProcessError as e:
        raise e;
    
    

# Run as sudo
if __name__ == '__main__':
    try:
        setup_files()
        print(banner())
        menu()
    except Exception as e:
        print(f"Failed to setup configuration: {e}")


