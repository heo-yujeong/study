# 아래에 코드를 작성하시오.
import conf.settings
import utils.create_url

name = conf.settings.NAME
main_url = conf.settings.MAIN_URL

result = utils.create_url.create_url(name, main_url)
print(result)