from bipwrapper.api import BIP, MessageType

bip = BIP("http://tims.turkcell.com.tr/tes/rest/spi/sendmsgserv", "**", "***")

bip.send_text_message("5332108311", "test2")
