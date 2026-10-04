import json
import requests

# Ganti URL di bawah ini dengan Incoming Webhook URL dari Slack Anda
WEBHOOK_URL = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'


def send_slack_message(message):
  payload = {'text': message}

  response = requests.post(
      WEBHOOK_URL,
      data=json.dumps(payload),
      headers={'Content-Type': 'application/json'},
  )

  if response.status_code == 200:
    print('Pesan berhasil dikirim ke Slack!')
  else:
    print(
        f'Gagal mengirim pesan. Status code: {response.status_code}, Respon:'
        f' {response.text}'
    )


if __name__ == '__main__':
  pesan = 'Halo! Ini adalah pesan otomatis yang dikirim dari skrip Python ke Slack.'
  send_slack_message(pesan)
