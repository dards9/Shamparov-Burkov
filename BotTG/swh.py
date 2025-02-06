import requests

TG_API='7790178826:AAHzJIiCi9i6nS2-4xIqm74K6CuAcSPcJuY'
whook=''    #а сюда нада сервак


r= requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{whook}/')

print(r.json())