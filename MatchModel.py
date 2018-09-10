import re


IP_PATTERN='[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'+'\\.'+'[0-9]{1,3}'
COMMON_PICTURE_JPG=r'class="BDE_Image"\s+src="([.*\S]*\.jpg)"'
COMMON_PICTURE_PNG=r'class="BDE_Image"\s+src="([.*\S]*\.png)"'



#class="BDE_Image"\s+